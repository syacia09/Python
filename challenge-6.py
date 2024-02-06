num = int(input("Masukkan angka ganjil (lebih dari 20) : "))
while (num % 2 == 0 or num <= 20) :
    print("Bilangan Salah..")
    num = int(input("Masukkan angka ganjil (lebih dari 20) : "))
else :
    print("Benar..")