from datetime import datetime, timedelta
from prettytable import PrettyTable


admin_data = {"admin cantik": "admin lalala"}
pengguna_data = {"adella": "putri", "lala": "bila"}

data_menstruasi = {}

def login():
    print("\n**********************************")
    print(">>>>> Login dulu yaaa gurlss <<<<<")
    print("----------------------------------")
    username = input("Masukkan Username kamuu: ")
    password = input("Password nya juga yaa: ")
    if username in admin_data and admin_data[username] == password:
        return "admin"
    elif username in pengguna_data and pengguna_data[username] == password:
        return username
    else:
        return None

def tambah_data(username):
    print("\n*************************************************")
    print(">>>>> Silahkan menambah data menstruasi muu <<<<<")
    print("-------------------------------------------------")
    tanggal = input("Masukkan tanggal menstruasi mu (Tanggal-Bulan-Tahun): ")
    durasi = int(input("Masukkan durasi menstruasi mu(dalam hari): "))
    if username not in data_menstruasi:
        data_menstruasi[username] = []
    data_menstruasi[username].append({"tanggal": tanggal, "durasi": durasi})
    print("Okeyy!! Data berhasil ditambahkan!")

def tampilkan_data(username):
    print(f"\n----- Data Menstruasi {username} -----")
    if username not in data_menstruasi or not data_menstruasi[username]:
        print("Upss!! Kamu belum memiliki data menstruasi.")
    else:
        table = PrettyTable()
        table.field_names = ["No.", "Tanggal", "Durasi (hari)"]
        for i, data in enumerate(data_menstruasi[username], 1):
            table.add_row([i, data['tanggal'], data['durasi']])
        print(table)

def hitung_perkiraan(username):
    if username not in data_menstruasi or not data_menstruasi[username]:
        print("Upss!! Kamu belum memiliki data menstruasi untuk menghitung perkiraan selanjutnya.")
        return
    
    tanggal_terakhir = datetime.strptime(data_menstruasi[username][-1]['tanggal'], "%d-%m-%Y")
    perkiraan = tanggal_terakhir + timedelta(days=28)
    print(f"\nPerkiraan haid mu berikutnya: {perkiraan.strftime('%d-%m-%Y')}")

def tips_mengatasi_gejala():
    print("\n~~~ Berikut Tips and Trick untuk mengatasi gejala Menstruasi muu ~~~")
    tips = [
        "- Minum banyak-banyak air putih gurls",
        "- Istirahat yang cukup! jangan banyak begadang ya gurl",
        "- Lakukan olahraga ringan juga",
        "- Hindari makanan berlemak dan berkafein",
        "- kalau mulai timbul gejala kram bisa mulai gunakan kompres hangat pada perut yaa"
    ]
    table = PrettyTable()
    table.field_names = ["Tips Mengatasi Gejala Menstruasi"]
    for tip in tips:
        table.add_row([tip])
    print(table)

def kelola_admin():
    while True:
        print("\n------> Kelola Admin <------")
        print("1. Tambah Admin")
        print("2. Hapus Admin")
        print("3. Tampilkan Admin")
        print("4. Kembali ke Menu Admin")
        
        pilihan = input("Silahkan pilih menu (1-4): ")
        
        if pilihan == "1":
            username = input("Silahkan masukkan username admin baruu: ")
            password = input("Silahkan masukkan password admin baruu: ")
            admin_data[username] = password
            print("Okkey!! Admin baru berhasil ditambahkan.")
        elif pilihan == "2":
            username = input("Silahkan masukkan username admin yang akan dihapus: ")
            if username in admin_data and username != "admin":
                del admin_data[username]
                print("Okkey!! Admin berhasil dihapus.")
            else:
                print("Upss!! Admin tidak ditemukan atau tidak dapat dihapus.")
        elif pilihan == "3":
            print("\nDaftar Admin:")
            table = PrettyTable()
            table.field_names = ["Username"]
            for admin in admin_data:
                table.add_row([admin])
            print(table)
        elif pilihan == "4":
            break
        else:
            print("Ups!! Pilihan tidak valid. Silakan di coba lagi ya.")

def kelola_pengguna():
    while True:
        print("\n------> Kelola Pengguna <------")
        print("1. Menambah Pengguna")
        print("2. Menghapus Pengguna")
        print("3. Menampilkan Pengguna")
        print("4. Menampilkan Data Pengguna")
        print("5. Menghapus Data Pengguna")
        print("6. Kembali ke Menu Admin")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            username = input("Silahkan masukkan username pengguna baru: ")
            password = input("Silahkan masukkan password pengguna baru: ")
            pengguna_data[username] = password
            print("Okeyy!! Pengguna baru berhasil ditambahkan!.")
        elif pilihan == "2":
            username = input("Silahkan masukkan username pengguna yang ingin dihapus: ")
            if username in pengguna_data:
                del pengguna_data[username]
                if username in data_menstruasi:
                    del data_menstruasi[username]
                print("Okkey!! Pengguna berhasil dihapus.")
            else:
                print("Ups!! Pengguna tidak ditemukan.")
        elif pilihan == "3":
            print("\nBerikut daftar Pengguna yang ada:")
            table = PrettyTable()
            table.field_names = ["Username"]
            for user in pengguna_data:
                table.add_row([user])
            print(table)
        elif pilihan == "4":
            username = input("Silahkan masukkan username pengguna yang ingin ditampilkan datanyaa: ")
            if username in data_menstruasi:
                tampilkan_data(username)
            else:
                print("Upss!! Data pengguna tidak ditemukan.")
        elif pilihan == "5":
            username = input("Silahkan masukkan username pengguna yang datanya akan dihapus: ")
            if username in data_menstruasi:
                del data_menstruasi[username]
                print("Okkey!! Data pengguna berhasil dihapus.")
            else:
                print("Upss!! Data pengguna tidak ditemukan.")
        elif pilihan == "6":
            break
        else:
            print("Upss!! Pilihan tidak valid. Silakan di coba lagi ya.")

def menu_pengguna(username):
    while True:
        print(f"\n_____ Menu Pengguna: {username} _____")
        print("1. Tambah Data Menstruasi")
        print("2. Tampilkan Data Menstruasi")
        print("3. Hitung Perkiraan Haid Berikutnya")
        print("4. Tips Mengatasi Gejala Haid")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tambah_data(username)
        elif pilihan == "2":
            tampilkan_data(username)
        elif pilihan == "3":
            hitung_perkiraan(username)
        elif pilihan == "4":
            tips_mengatasi_gejala()
        elif pilihan == "5":
            print("Terima kasih yaa telah menggunakan program ini. Stay happy and healthy, Sampai jumpa!")
            break
        else:
            print("Ups!! Pilihan tidak valid. Silakan coba lagi.")

def menu_admin():
    while True:
        print("\n>>>>> Menu Admin <<<<<")
        print("1. Kelola Admin")
        print("2. Kelola Pengguna")
        print("3. Keluar")
        
        pilihan = input("Silahkan pilih menu (1-3): ")
        
        if pilihan == "1":
            kelola_admin()
        elif pilihan == "2":
            kelola_pengguna()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini. Stay happy and healthy, Sampai jumpa!")
            break
        else:
            print("Upss!!Pilihan tidak valid. Silakan coba lagi.")

def main():
    print("\n-----------------------------------------------------------------------")
    print(">>>>> Selamat datang di Sistem Pemantauan Siklus Haid, Hi Check!! <<<<<")
    print("-----------------------------------------------------------------------")
    while True:
        user_type = login()
        if user_type == "admin":
            print("Login mu berhasil sebagai Admin!!")
            menu_admin()
        elif user_type:
            print(f"Login mu berhasil sebagai Pengguna: Hi {user_type}!")
            menu_pengguna(user_type)
        else:
            print("Ups!! Login gagal. Silakan coba lagi.")
        
        lanjut = input("Apakah Anda ingin melanjutkan program? (y/n): ")
        if lanjut.lower() != 'y':
            print("Terima kasih telah menggunakan program ini. stay happy and healthy, Sampai jumpa!")
            break

if __name__ == "__main__":
    main()