def cek_kelulusan_mahasiswa(nama, nilai_tugas, nilai_ujian):
    # 1. Menghitung rata-rata nilai
    rata_rata = (nilai_tugas + nilai_ujian) / 2
    
    # 2. Memeriksa status kelulusan (True jika >= 75, False jika < 75)
    status_lulus = rata_rata >= 75
    
    # 3. Menampilkan hasil
    print(f"Nama Mahasiswa : {nama}")
    print(f"Nilai Tugas    : {nilai_tugas}")
    print(f"Nilai Ujian    : {nilai_ujian}")
    print(f"Rata-rata      : {rata_rata}")
    print(f"Status Lulus   : {status_lulus}")
    print("-" * 30)

# === UJI PROGRAM DENGAN DUA KOMBINASI NILAI ===

# Pengujian 1: Kasus Mahasiswa Lulus (Rata-rata >= 75)
print("--- UJI COBA 1 ---")
cek_kelulusan_mahasiswa(nama="Mariano Peralta", nilai_tugas=80, nilai_ujian=76)

# Pengujian 2: Kasus Mahasiswa Tidak Lulus (Rata-rata < 75)
print("--- UJI COBA 2 ---")
cek_kelulusan_mahasiswa(nama="Gabriel Mutombo", nilai_tugas=70, nilai_ujian=68)
