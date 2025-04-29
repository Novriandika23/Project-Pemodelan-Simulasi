import tkinter as tk
from tkinter import ttk, messagebox
from database import simpan_peserta

def tampil_pendaftaran(frame_utama, tampil_login):
    for widget in frame_utama.winfo_children():
        widget.destroy()

    # Styling
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TLabel", font=("Segoe UI", 10))
    style.configure("TButton", padding=6, font=("Segoe UI", 10, "bold"))
    style.configure("TEntry", padding=4)

    # Frame container lebih besar
    container = ttk.Frame(frame_utama, padding=30)
    container.pack(expand=True, fill="both")

    # Gunakan frame tengah agar form terpusat dan lebih lebar
    form_frame = ttk.Frame(container)
    form_frame.pack(expand=True)

    ttk.Label(form_frame, text="Form Pendaftaran", font=("Segoe UI", 16, "bold")).pack(pady=(0, 15))

    def buat_form(label_text, entry_widget):
        ttk.Label(form_frame, text=label_text).pack(anchor="w")
        entry_widget.pack(fill="x", pady=5, ipady=4, ipadx=10)

    nama_entry = ttk.Entry(form_frame, width=50)
    kelas_entry = ttk.Entry(form_frame, width=50)
    umur_entry = ttk.Entry(form_frame, width=50)
    tahun_lahir_entry = ttk.Entry(form_frame, width=50)
    password_entry = ttk.Entry(form_frame, show="*", width=50)

    jenis_kelamin_var = tk.StringVar()
    jenis_kelamin_var.set("")

    buat_form("Nama:", nama_entry)
    buat_form("Kelas:", kelas_entry)
    buat_form("Umur:", umur_entry)
    buat_form("Tahun Lahir:", tahun_lahir_entry)

    ttk.Label(form_frame, text="Jenis Kelamin:").pack(anchor="w")
    jk_frame = ttk.Frame(form_frame)
    jk_frame.pack(anchor="w", pady=5)
    ttk.Radiobutton(jk_frame, text="Laki-laki", variable=jenis_kelamin_var, value="Laki-laki").pack(side="left", padx=5)
    ttk.Radiobutton(jk_frame, text="Perempuan", variable=jenis_kelamin_var, value="Perempuan").pack(side="left", padx=5)

    buat_form("Password:", password_entry)

    # Fungsi daftar
    def daftar():
        nama = nama_entry.get()
        kelas = kelas_entry.get()
        umur = umur_entry.get()
        tahun_lahir = tahun_lahir_entry.get()
        jenis_kelamin = jenis_kelamin_var.get()
        password = password_entry.get()

        if "" in [nama, kelas, umur, tahun_lahir, jenis_kelamin, password]:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return

        simpan_peserta(nama, kelas, int(umur), int(tahun_lahir), jenis_kelamin, password)
        messagebox.showinfo("Sukses", "Pendaftaran berhasil! Silakan login.")
        tampil_login()

    # Tombol
    ttk.Button(form_frame, text="Daftar", command=daftar).pack(pady=(20, 5), fill="x")
    ttk.Button(form_frame, text="Sudah Punya Akun? Login", command=tampil_login).pack(fill="x")
