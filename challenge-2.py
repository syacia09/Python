print(">> \tTOKO PENJUALAN-XYZ\t <<")
print("-"*35)
nama_brg = input("Nama Barang\t= ")
hrg_brg = int(input("Harga Barang\t= Rp. "))
jumlah_beli = int(input("Jumlah Beli\t= "))

sub_total = hrg_brg * jumlah_beli
print("Subtotal\t= Rp.{:>5}".format(sub_total))

diskon = int(sub_total * 0.2)
print(f"Diskon (20%)\t= Rp.{diskon:>5}")

total_akhir = sub_total - diskon
print(f"Harga total\t= Rp.{total_akhir:>5} ")

besar_bayar = int(input("Besar Bayar\t= Rp."))
print("-"*35)

Kembalian = besar_bayar - total_akhir
print(f"Kembalian\t= {Kembalian:>5}")
RincianKembalian1 = Kembalian // 50000
Kembalian2 = Kembalian % 50000
RincianKembalian2 = Kembalian2 % 50000 // 20000
RincianKembalian3 = Kembalian2 % 50000 % 20000 // 10000
RincianKembalian4 = Kembalian2 % 50000 % 20000 % 10000 // 5000
RincianKembalian5 = Kembalian2 % 50000 % 20000 % 10000 % 5000 // 2000
RincianKembalian6 = Kembalian2 % 50000 % 20000 % 10000 % 5000 % 2000 // 1000
print("Rincian Kembalian : ")
print(f"Rp.50000\t= {RincianKembalian1:>5} lembar")
print(f"Rp.20000\t= {RincianKembalian2:>5} lembar")
print(f"Rp.10000\t= {RincianKembalian3:>5} lembar")
print(f"Rp.5000\t= {RincianKembalian4:>5} lembar")
print(f"Rp.2000\t= {RincianKembalian5:>5} lembar")
print(f"Rp.1000\t= {RincianKembalian6:>5} lembar")