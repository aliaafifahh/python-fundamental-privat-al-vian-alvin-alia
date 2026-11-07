def Pertambahan(a,b) :
    return a + b

def Pengurangan(a,b) :
    return a - b

def Perkalian(a,b) :
    return a * b

def Pembagian(a,b) :
    return a / b

def Euclidean_Distance(x) :
    if not(isinstance(x,(list,tuple))) :
        raise ValueError("Input Wajib Tuple atau List 2 Dimensi")
    if len(x) != 2 :
        raise ValueError("Jumlah elemen pada input wajib berjumlah 2 list atau tuple")
    if len(x[0]) != len(x[1]) :
        raise ValueError("Jumlah dimensi pada masing2 titik berbeda")
    hasil = 0
    for i in range(len(x[0])) :
        hasil += (x[0][i] - x[1][i])**2
    return hasil**0.5
        
    