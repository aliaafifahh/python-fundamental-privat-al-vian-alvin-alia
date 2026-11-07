def cek_angka(x) :
    if not(isinstance(x,(int,float))) :
        raise ValueError("Elemen Huruf Terdeteksi")
    
def summ(x) :
    map(cek_angka,x)
    hasil = 0
    for i in x :
        hasil += i
    return hasil

def meann(x) :
    return summ(x)/len(x)