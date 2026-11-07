try :
    with open("File09.csv","r",encoding="utf-8") as file :
        pass
except FileNotFoundError :
    print ("File Tidak Ada")
finally :
    print ("Selesai")