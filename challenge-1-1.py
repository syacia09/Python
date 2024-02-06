nilai = int(input ("Masukkan nilai ( diatas 10 dan dibawah 13 ) : "))
hasil = nilai > 10 and nilai < 13
print ("Nilai yang dimasukkan : ", hasil)

nilai = int(input ("Masukkan nilai ( diantara 20-23 atau 34-38 atau 40-42 ) : "))
hasil = (nilai > 20 and nilai < 23) or (nilai > 34 and nilai < 38) or (nilai > 40 and nilai < 42)
print ("Nilai yang dimasukkan : ", hasil)
