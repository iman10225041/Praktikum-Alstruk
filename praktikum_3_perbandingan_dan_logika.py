nilai = 82
kehadiran = 90

print("--- Kondisi Awal ---")
syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print(f"Apakah nilai memenuhi syarat? {syarat_nilai}")
print(f"Apakah kehadiran memenuhi syarat? {syarat_kehadiran}")

lulus_and = syarat_nilai and syarat_kehadiran
print(f"Hasil Kelulusan (menggunakan AND): {lulus_and}")


print("\n--- Nilai menjadi 70 ---")

nilai = 70
syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print(f"Apakah nilai memenuhi syarat? {syarat_nilai}")
print(f"Apakah kehadiran memenuhi syarat? {syarat_kehadiran}")

lulus_and_baru = syarat_nilai and syarat_kehadiran
print(f"Hasil Kelulusan Baru (menggunakan AND): {lulus_and_baru}")


print("\n--- Menggunakan OR ---")

lulus_or = syarat_nilai or syarat_kehadiran
print(f"Hasil Kelulusan Baru (menggunakan OR): {lulus_or}")
