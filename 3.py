# while True:
#     angka = int(input(f"Masukkan angka\t: "))
#     if angka % 2 == 0:
#         print(f"Genapp")
#     else:
#         print(f"Ganjil")

#     program_lg = input(f"Apakah Ingin Menggunakan Program Lagi?\nA.Ya\nB.Tidak\n")
#     if program_lg == "A":
#         continue
#     else:
#         break

# print(f'Program Selesai')


# hasil = 0
# while True:

#     angka = int(input(f"Masukkan Angka\t: "))
#     if angka != 0:
#         hasil += angka
#         continue
#     else:
#         break  
# print(f"Hasil\t= {hasil}")

panjang = int(input(f"Masukkan panjang\t: "))
for i in range (panjang):
    print('* ', end="")