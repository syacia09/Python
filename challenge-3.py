from datetime import date as dt 

print(f"<< \t\t UMUR \t\t >>")
print("-"*35)
print("Masukkan tanggal, bulan, tahun (Lahir). ")
print("\n")
tanggal = int(input("Tanggal \t : "))
bulan = int(input("Bulan \t\t : "))
tahun = int(input("Tahun \t\t : "))

tgl_lahir = dt(tahun, bulan, tanggal)
today = dt.today()
print(f"Tanggal lahir \t : {tgl_lahir.day}-{tgl_lahir.month}-{tgl_lahir.year}")
print(f"Tanggal hari ini : {today.day}-{today.month}-{today.year}")

selisih_tgl = today - tgl_lahir
print(f"Selisih tanggal : {selisih_tgl.days} hari")

usia_tahun = selisih_tgl.days // 365
usia_bulan = (selisih_tgl.days % 365 ) // 30

print(f"Usia \t\t : {usia_tahun} tahun {usia_bulan} bulan")