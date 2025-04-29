# main.py

import tkinter as tk
from pendaftaran import tampil_pendaftaran
from login import tampil_login
from database import buat_database
from ujian import tampil_menu_ujian

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi Ujian Monte Carlo")
root.geometry("600x700")

frame_utama = tk.Frame(root)
frame_utama.pack(expand=True, fill="both")

# Inisialisasi Database
buat_database()

# Fungsi untuk membersihkan frame_utama
def bersihkan_frame():
    for widget in frame_utama.winfo_children():
        widget.destroy()

# Wrapper untuk form login
def tampil_login_wrapper():
    bersihkan_frame()
    tampil_login(frame_utama, tampil_menu_ujian, tampil_pendaftaran_wrapper)

# Wrapper untuk form pendaftaran
def tampil_pendaftaran_wrapper():
    bersihkan_frame()
    tampil_pendaftaran(frame_utama, tampil_login_wrapper)

# Wrapper untuk menu ujian
def tampil_menu_ujian(frame_utama, nama_peserta):
    print(f"Menampilkan menu ujian untuk {nama_peserta}")
    from ujian import tampil_menu_ujian as tampil_ujian
    tampil_ujian(frame_utama, nama_peserta)


# Tampilkan form LOGIN pertama kali
tampil_login_wrapper()

# Mulai aplikasi
root.mainloop()
