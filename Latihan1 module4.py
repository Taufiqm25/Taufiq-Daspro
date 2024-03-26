harga = int(input("Masukkan harga belanja: "))

if harga >= 250000:
    diskon = harga * 50 / 100
    print("Diskon yang Anda dapatkan:", diskon)
else:
    print("Belanjaan tidak mendapat diskon")
