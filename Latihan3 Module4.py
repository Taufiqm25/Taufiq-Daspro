database = {
    "opick": "07352311118",
    "eza": "07352311117",
    "zakira": "07352311119"
}


mata_kuliah = {
    "daspro": "pak yasir",
    "arsikom": "pak chiko",
    "matematika distrik": "pak sarifuddin"
}


def login():
    username = input("Masukkan username:")
    password = input("Masukkan password:")

    if username in database and database[username] == password:
        print("Login berhasil!")
        return True
    else:
        print("Username atau password salah.")
        return False


def input_mata_kuliah():
    print("Pilih mata kuliah yang ingin diinput:")
    for i, mata_kuliah_nama in enumerate(mata_kuliah.keys(), 1):
        print(f"{i}. {mata_kuliah_nama}")

    pilihan = int(input("Masukkan pilihan: "))
    if pilihan in range(1, len(mata_kuliah) + 1):
        mata_kuliah_nama = list(mata_kuliah.keys())[pilihan - 1]
        dosen_pengampuh = mata_kuliah[mata_kuliah_nama]
        print(f"Anda memilih mata kuliah {mata_kuliah_nama} yang diajarkan oleh {dosen_pengampuh}.")
    else:
        print("Pilihan tidak valid.")


if login():
    input_mata_kuliah()
