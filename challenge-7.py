print("<<<\t\t\tIdentifikasi Bilangan\t\t\t>>>")
print("Indentifikasi nilai jika nilai 10-15 atau nilai 20-25 atau 25-40")
print("-"*70)
status = False
while (status != True) :
    num = int(input("Masukkan Bilangan : "))
    if ((num > 10 and num < 15) or (num > 20 and num < 25) or (num > 35 and num < 40)) :
        status = True
        print("Benar..")
    else :
        print("Salah")
    