# nilai = float(input(f"Masukkan Nilai :"))

# if nilai >= 75:
#     print ("Lulus")
# else:
#     print("Remidi")

# barang = input(f"Masukkan Nama Barang\t\t: ")
# harga = float(input(f"Masukkan Harga Barang\t\t: "))
# jumlah = int(input(f"Masukkan Jumlah Barang\t\t: "))

# total_belnja = jumlah*harga


# if total_belnja <= 150:
#     diskon = 0.1
# else:
#     diskon = 0

# pot_hrg = total_belnja*diskon
# totalan = pot_hrg-diskon

# print(f"{"":=^35}")
# print(f"{barang}\t\t:",f"Rp{total_belnja:>,.2f}")
# print(f"Diskon \t\t: {diskon}")
# print(f"{"":-^35}")
# print(f"Total\t\t: {totalan}")

usia = int(input(f"Masukkan Usia\t:"))

if usia >= 60:
    print("Lansia")
elif 18 <= usia < 60:
    print("Dewasa")
elif 13 <= usia < 18:
    print("Remaja")
elif 5 <= usia < 13:
    print("Anak-anak")
elif  0 < usia < 5:
    print("Balita")
else:
    print("Tidak Valid")