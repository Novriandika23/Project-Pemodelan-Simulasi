import tkinter as tk
from tkinter import ttk, messagebox
from database import cek_login

def tampil_login(frame_utama, tampil_menu_ujian, tampil_pendaftaran):
    # Mengosongkan frame
    for widget in frame_utama.winfo_children():
        widget.destroy()

    # Styling
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", font=("Segoe UI", 10))
    style.configure("TButton", padding=6, font=("Segoe UI", 10, "bold"))
    style.configure("TEntry", padding=4)

    # Frame container
    container = ttk.Frame(frame_utama, padding=30)
    container.pack(expand=True, fill="both")

    form_frame = ttk.Frame(container)
    form_frame.pack()

    ttk.Label(form_frame, text="Form Login", font=("Segoe UI", 20, "bold")).pack(pady=(0, 15))

    username_entry = ttk.Entry(form_frame, width=50)
    password_entry = ttk.Entry(form_frame, show="*", width=50)

    def buat_form(label, entry):
        ttk.Label(form_frame, text=label).pack(anchor="w")
        entry.pack(fill="x", pady=5, ipady=4)

    buat_form("Username:", username_entry)
    buat_form("Password:", password_entry)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":
            messagebox.showwarning("Peringatan", "Username dan Password tidak boleh kosong!")
            return

        if cek_login(username, password):
            messagebox.showinfo("Sukses", "Login Berhasil!")
            tampil_menu_ujian(frame_utama, username)
        else:
            messagebox.showerror("Gagal", "Username atau Password salah!")

    ttk.Button(form_frame, text="Login", command=login).pack(pady=(20, 5), fill="x")
    ttk.Button(form_frame, text="Belum Punya Akun? Daftar", command=tampil_pendaftaran).pack(fill="x")
