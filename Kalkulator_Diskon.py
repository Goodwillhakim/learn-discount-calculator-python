print("=" *41)
print("         Kalkulator Diskon")
print("=" *41)

def hitung_diskon (harga_awal:float, persen_diskon:float) -> float :
    harga_akhir = harga_awal * persen_diskon / 100
    jumlah_diskon = harga_awal - harga_akhir
    return harga_akhir
    
jumlah_barang = int(input("Masukan Jumlah Barang: ")) 

for i in range(jumlah_barang):
    print(f"\nBarang ke-{i+1}")
    
harga_awal = float(input("Masukan Harga Awal: "))
persen_diskon = float(input("Masukan Jumlah Diskon: "))

hasil = hitung_diskon (harga_awal, persen_diskon)

print(hasil)