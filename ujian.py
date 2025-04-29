# ujian.py

import tkinter as tk
from tkinter import messagebox, ttk
import random
from soal import soal_ujian

def tampil_menu_ujian(frame_utama, nama_peserta):
    # Bersihkan frame
    for widget in frame_utama.winfo_children():
        widget.destroy()

    # Style configuration
    style = ttk.Style()
    style.configure('TFrame', background='#f0f0f0')
    style.configure('TLabel', background='#f0f0f0', foreground='black', font=('Helvetica', 11))
    style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'))
    style.configure('Submit.TButton', font=('Helvetica', 12, 'bold'), foreground='Black', background='#4CAF50')

    # Main container
    main_container = ttk.Frame(frame_utama)
    main_container.pack(fill='both', expand=True, padx=20, pady=10)

    # Canvas and scrollbar setup
    canvas = tk.Canvas(main_container, highlightthickness=0, bg='#f0f0f0')
    scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    # Perbaikan di bagian ini
    def configure_scroll_region(e):
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    scrollable_frame.bind("<Configure>", configure_scroll_region)
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Mouse wheel scrolling
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Header section
    header_frame = ttk.Frame(scrollable_frame)
    header_frame.pack(fill='x', pady=(0, 20))
    
    ttk.Label(header_frame, 
             text=f"Selamat mengerjakan, {nama_peserta}!",
             style='Title.TLabel').pack(pady=(10, 5))
    ttk.Label(header_frame, 
             text="Silakan jawab semua soal berikut:",
             style='TLabel').pack()

    # Soal section
    soal_acak = random.sample(soal_ujian, len(soal_ujian))
    jawaban_peserta = {}

    for idx, soal in enumerate(soal_acak[:20], start=1):
        question_frame = ttk.Frame(scrollable_frame, relief=tk.GROOVE, borderwidth=1, padding=10)
        question_frame.pack(fill='x', pady=8, padx=5)
        
        ttk.Label(question_frame, 
                 text=f"Soal {idx}: {soal['soal']}",
                 wraplength=600,
                 justify='left').pack(anchor='w')
        
        var = tk.StringVar(value="")
        jawaban_peserta[idx] = {"var": var, "jawaban_benar": soal['jawaban']}
        
        pilihan_acak = random.sample(soal['pilihan'], len(soal['pilihan']))
        for pilihan in pilihan_acak:
            rb = tk.Radiobutton(
                question_frame,
                text=pilihan,
                variable=var,
                value=pilihan,
                bg='#f0f0f0',
                fg='#000000',
                activebackground='#f0f0f0',
                selectcolor='#f0f0f0',
                relief=tk.FLAT,
                highlightthickness=0,
                padx=5,
                pady=2
            )
            rb.pack(anchor='w', padx=15, pady=2)

    # Submit button
    submit_frame = ttk.Frame(scrollable_frame)
    submit_frame.pack(fill='x', pady=20)
    
    submit_btn = ttk.Button(submit_frame, 
                          text="Kirim Jawaban",
                          command=lambda: submit_jawaban(jawaban_peserta, frame_utama),
                          style='Submit.TButton')
    submit_btn.pack(pady=10)

def submit_jawaban(jawaban_peserta, frame_utama):
    benar = 0
    total = len(jawaban_peserta)

    for idx, data in jawaban_peserta.items():
        if data["var"].get() == data["jawaban_benar"]:
            benar += 1

    nilai = int((benar / total) * 100)
    messagebox.showinfo("Hasil Ujian", 
                       f"Ujian selesai!\n\nJawaban benar: {benar}/{total}\nNilai Anda: {nilai}")
    
    # Kembali ke login
    from main import tampil_login_wrapper
    tampil_login_wrapper(frame_utama)