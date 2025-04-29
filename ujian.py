import tkinter as tk
from tkinter import ttk, messagebox
import random
from soal import soal_ujian

def tampil_menu_ujian(frame_utama, nama_peserta):
    for widget in frame_utama.winfo_children():
        widget.destroy()

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TButton", padding=10, font=("Segoe UI", 12, "bold"))
    style.configure("TLabel", font=("Segoe UI", 15,))
    style.configure("TFrame", background="#f2f2f2")

    canvas = tk.Canvas(frame_utama, bg="#f2f2f2", highlightthickness=0)
    scrollbar = ttk.Scrollbar(frame_utama, orient="vertical", command=canvas.yview)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    scrollable_container = ttk.Frame(canvas, style="TFrame")  # container utama di canvas
    canvas.create_window((0, 0), window=scrollable_container, anchor="n")

    canvas.configure(yscrollcommand=scrollbar.set)

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # WRAPPER TENGAH
    wrapper = ttk.Frame(scrollable_container, style="TFrame")
    wrapper.pack(anchor="center", pady=20)  # PUSATKAN SECARA HORIZONTAL

    # BATASI LEBAR agar tidak terlalu lebar
    inner_frame = ttk.Frame(wrapper, style="TFrame")
    inner_frame.pack()

    ttk.Label(inner_frame, text=f"Selamat datang, {nama_peserta}!", font=("Segoe UI", 16, "bold")).pack(pady=(20, 5))
    ttk.Label(inner_frame, text="Silakan jawab soal berikut:", font=("Segoe UI", 12)).pack(pady=(0, 20))

    soal_acak = random.sample(soal_ujian, len(soal_ujian))
    jawaban_peserta = {}

    for idx, soal in enumerate(soal_acak[:20], start=1):
        ttk.Label(inner_frame, text=f"{idx}. {soal['soal']}", wraplength=700, justify="left").pack(anchor="w", padx=30, pady=(10, 0))

        var = tk.StringVar(value="")
        jawaban_peserta[idx] = {"var": var, "jawaban_benar": soal['jawaban']}

        pilihan_acak = random.sample(soal['pilihan'], len(soal['pilihan']))
        for pilihan in pilihan_acak:
            ttk.Radiobutton(inner_frame, text=pilihan, variable=var, value=pilihan).pack(anchor="w", padx=50, pady=2)

    def submit_jawaban():
        benar = 0
        total = len(jawaban_peserta)

        for idx, data in jawaban_peserta.items():
            if data["var"].get() == data["jawaban_benar"]:
                benar += 1

        nilai = int((benar / total) * 100)
        messagebox.showinfo("Hasil Ujian", f"Ujian selesai!\nJawaban benar: {benar}/{total}\nNilai Anda: {nilai}")

        from main import tampil_login_wrapper
        tampil_login_wrapper()

    ttk.Button(inner_frame, text="Kirim Jawaban", command=submit_jawaban).pack(pady=20, ipadx=20, ipady=8)

    # Pastikan canvas bisa scroll
    scrollable_container.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
