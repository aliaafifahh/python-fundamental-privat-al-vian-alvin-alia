
# data = [
#     ['01', 'Sarapan Nasi Kuning', 5000],
#     ['01', 'Beli Galon', 20000],
#     ['01', 'Mie Ayam Tinton', 15000],
#     ['02', 'Cilor', 2000],
#     ['03', 'Paket Data', 50000]
# ]

# with open("File09.csv","w", encoding="utf-8") as filebaru :
#     for i in range(len(data)) :
#         print(data[i][0], data[i][1], data[i][2], sep=',', file=filebaru)

data = []

with open("File09.csv", "r", encoding="utf-8") as filebaru :
    for baris in filebaru :
        baris = baris.strip()
        tanggal, keterangan, harga = baris.split(",")
        harga = int(harga)
        data.append([tanggal, keterangan, harga])

print(data)