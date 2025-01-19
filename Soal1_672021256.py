import os
import msvcrt

print("Menu Login")

# Username dan Password
user ="672021256"
pas ="672021256"

def program_kasir():
        os.system('cls')
        total = 0     
        print(14*"=")
        print("= Menu Kasir =")
        print(14*"=")
        # Input user
        makanan = input("Masukan Pesanan anda : ")
        harga = int(input("Masukan harga barang : "))
        jumlah = int(input("Berapa yang anda inginkan: "))
        total = harga * jumlah
        print("Total Pembelian anda sebanyak :" , total)
        bayaran = int(input("Masukan Pembayaran : "))

        # Hasil
        if bayaran < total:
            kurang = total - bayaran
            print("Maaf uang anda tidak cukup untuk", makanan , "uang anda kurang", kurang)
            input("")
        elif bayaran > total:
            lebih = bayaran - total
            print ("Pembayaran di terima, uang kembalian anda sebesar", lebih, "silahkan ambil", makanan , "anda")
        else:
            print("Pembaran diterima, Terimakasih")

def segitiga(n):

    panjang = [1]
    for i in range(n):
        # barisan pertama dengan segitiga kosong
        print(" " * (n-i), end="")
        for j in range(len(panjang)):
            print(panjang[j], end=" ")
        print()

        # Isi dari segitiga
        baris_baru = [1]

        for k in range(len(panjang)-1):
            baris_baru.append(panjang[k]+panjang[k+1])
        baris_baru.append(1)
        panjang = baris_baru    
    
a = 0
    
while a == 0:
    os.system('cls')
    username = input("Masukan Username anda :")
    password = input("Masukan Password anda :")
    if username != user or password != pas:
        print("Coba lagi, mungkin password atau username anda salah")
        print("\nTekan enter untuk melanjutkan program")
        input("")
        os.system('cls')
        a = 0
    else:
        print("Silahkan Masuk")
        input("")
        a = 1
        os.system('cls')

perulanngan = 0

while perulanngan == 0:
    os.system('cls')
    print("======== MAIN MENU APPLIKASI KASIR ============")
    print("=      Selamat datang di applikasi kasir      =")
    print("===============================================")
    print("1. Program Kasir")
    print("2. Segitiga")
    print("3. Exit")
    pilihan = input("pilih menu :")

    if pilihan == "1": 
        p = 0
        while p == 0:
            os.system('cls') 
            program_kasir()
            coba = input("Ingin coba lagi? (y/n)")   
            if coba == "y":
                p = 0                
            else:
                p = 1

    elif pilihan == "2":
        p = 0
        while p == 0:
            os.system('cls') 
            n = int(input("Masukan panjang segitiga yang diinginkan : "))
            segitiga(n)
            coba = input("Ingin coba lagi? (y/n)")   
            if coba == "y":
                p = 0                
            else:
                p = 1
        
    
    elif pilihan == "3":
        print("Terimakasih")
        perulanngan = 1
    
    else:
        print("Pilihan tidak ada")
        perulanngan = 0
             


    



