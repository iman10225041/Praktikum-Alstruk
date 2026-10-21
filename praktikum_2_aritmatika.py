harga = 12000
jumlah = 4

total_harga = harga * jumlah
sisa_pembagian = total_harga % 2000
harga_setelah_diskon = total_harga - 5000

print(f"Harga per buku                         : Rp{harga:,}")
print(f"Jumlah buku yang dibeli                : {jumlah} buah")
print(f"Total harga awal                       : Rp{total_harga:,}")
print(f"Sisa pembagian total harga dengan 2.000 : {sisa_pembagian}")
print(f"Harga setelah diskon Rp5.000           : Rp{harga_setelah_diskon:,}")