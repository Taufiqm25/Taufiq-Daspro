def gajiperminggu(gajibulan):
    return round(gajibulan / 4.33)

def gajiperhari(gajiperminggu, jumlahhari):
    return round (gajiperminggu /jumlahhari)

def gajiperjam(gajiperhari, jamkerja):
    return round (gajiperhari / jamkerja)

gajibulan = float(input("masukkan gaji per bulan anda:"))
jamkerja = int(input("masukkan jumlah jam kerja per hari:"))
jumlahhari = int(input("masukkan jumlah hari kerja perminggu:"))

gaji_per_minggu = gajiperminggu(gajibulan)
gaji_per_hari = gajiperhari(gaji_per_minggu, jumlahhari)
gaji_per_jam = gajiperjam(gaji_per_hari, jamkerja)

print("==Taufiq M. Djabir==")
print("==07352311118==")
print(f"gaji per minggu: {gaji_per_minggu}"' '"rupiah")
print(f"gaji per hari :{gaji_per_hari}"' '"rupiah")
print(f"gaji per jam: {gaji_per_jam}"' '"rupiah")