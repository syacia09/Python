print("\t\tTIKET BUS\t\t")
print("-"*45)
print("Kode Kota :")
print("1. Prabumulih")
print("2. Muara Enim")
print("3. Lubuk Linggau")
num = int(input("Pilihan Kota (1,2,3) : "))
print("Kode Kelas :")
print("1. Ekonomi")
print("2. Bisnis")
print("3. Eksekutif")
status = False
while (status != True) :
    num2 = int(input("Pilihan Kelas (1,2,3) : "))
    if (num == 1) :
        if (num2 == 1) :
            biaya = 100000
            status = True
        elif (num2 == 2) :
            biaya = 400000
            status = True
        elif (num2 == 3) :
            biaya = 700000
            status = True
        else :
            print("Undefined")
    if (num == 2) :
        if (num2 == 1) :
            biaya = 200000
            status = True
        elif (num2 == 2) :
            biaya = 500000
            status = True
        elif (num2 == 3) :
            biaya = 800000
            status = True
        else :
            print("Undefined")
    if (num == 3) :
        if (num2 == 1) :
            biaya = 300000
            status = True
        elif (num2 == 2) :
            biaya = 600000
            status = True
        elif (num2 == 3) :
            biaya = 900000
            status = True
        else :
            print("Undefined")
q = int(input("Banyak Tiket : "))
promo = input("Kode Promo : ")
print("-"*45)
print(f"Harga Tiket \t : Rp. {biaya:>5}")
biaya = q * biaya
print(f"Sub Total \t : Rp. {biaya:>5}")
diskon = 0
if (promo == "igs") :
    diskon = int(0.1 * biaya)
    print(f"Diskon \t\t : Rp. {diskon:>5}")
print(f"Diskon \t\t : Rp. {diskon}")
total = biaya - diskon
print(f"Total Bayar \t : RP. {total:>5}")



