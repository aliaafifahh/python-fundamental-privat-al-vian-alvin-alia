buku = [
    ['Artificial Intelligence for Dumies', 5],
    ['The Power of Kepepet', 8],
    ['Hujan Kemarin', 6],
    ['Data Structure and Algorithm 2nd Edition', 10],
    ['Hundred Pages of Machine Learning', 2]
]
def tabel_buku (buku) :
    print(f"{"":=>62}")
    print(f"|{"No.":^7}|{"Nama Buku":^42}|{"Stok":^9}|")
    print(f"{"":=>62}")
    for i in range (len(buku)):
        print(f"|{i+1:^7}|{buku[i][0]:<42}|{buku[i][1]:^9}|")
    print(f"{"":=>62}")

tabel_buku(buku)
tabel_buku(buku)
tabel_buku(buku)



# def ganjil_genap (angka = 1):
#     if angka %2 == 0:
#         return 'Genap'
#     return 'Ganjil'

# print(ganjil_genap(angka=3))
# print(ganjil_genap(angka=7))
# print(ganjil_genap(angka=100))
# print(ganjil_genap(angka=-5))
# print(ganjil_genap(angka=-42))

# for i in [3, 7, 100, -5, -42]:
#     print(ganjil_genap(i))

def perpangkatan (angka1,angka2):
    hasil = 1
    for _ in range(angka2):
        hasil *= angka1
    return hasil

# print(perpangkatan(2,2))
# print(perpangkatan(2,3))
# print(perpangkatan(5,2))
# print(perpangkatan(2,5))
# print(perpangkatan(3,4))

for i,j in [(2,2),(2,3),(5,2),(2,5),(3,4)]:
    print(perpangkatan(i,j))