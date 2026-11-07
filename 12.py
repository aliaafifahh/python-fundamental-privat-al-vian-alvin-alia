while True :
    try :
        angka = int(input('Masukkan Bilangan : '))
    except ValueError :
        print('Bilangan Wajib Menggunakan Angka')
    else :
        print(f'Bilangan yang Anda Masukkan Adalah {angka}')
        break