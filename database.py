# database.py
import sqlite3

# Fungsi untuk membuat database dan tabel peserta
def buat_database():
    conn = sqlite3.connect('ujian.db')  # Menyambungkan ke database 'ujian.db'
    cursor = conn.cursor()

    # Membuat tabel peserta jika belum ada
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS peserta (
        id INTEGER PRIMARY KEY,
        nama TEXT,
        kelas TEXT,
        umur INTEGER,
        tahun_lahir INTEGER,
        jenis_kelamin TEXT,
        password TEXT
    )
    ''')

    conn.commit()  # Menyimpan perubahan ke database
    conn.close()   # Menutup koneksi

# Fungsi untuk menyimpan data peserta ke database
def simpan_peserta(nama, kelas, umur, tahun_lahir, jenis_kelamin, password):
    conn = sqlite3.connect('ujian.db')  # Menghubungkan ke database
    cursor = conn.cursor()

    # Menyimpan data peserta ke tabel peserta
    cursor.execute('''
    INSERT INTO peserta (nama, kelas, umur, tahun_lahir, jenis_kelamin, password)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (nama, kelas, umur, tahun_lahir, jenis_kelamin, password))

    conn.commit()  # Menyimpan perubahan ke database
    conn.close()   # Menutup koneksi

    print(f"Peserta {nama} berhasil disimpan.")  # Menampilkan pesan saat peserta berhasil disimpan

# Fungsi untuk mengecek login peserta
def cek_login(username, password):
    conn = sqlite3.connect('ujian.db')
    cursor = conn.cursor()

    # Mencari peserta dengan username dan password yang diberikan
    cursor.execute('''
    SELECT * FROM peserta WHERE nama = ? AND password = ?
    ''', (username, password))

    user = cursor.fetchone()  # Mengambil data peserta pertama yang ditemukan
    conn.close()

    # Jika ditemukan, kembalikan True, jika tidak ada, False
    return user is not None
