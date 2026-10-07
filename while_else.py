# Cari password yang benar dengan batas percobaan
password_benar = "python123"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password = input("Enter password: ")
    percobaan += 1

    if password == password_benar:
        print("Login Berhasil")
        break
    else:
        print("Password Salah. Sisa percobaan:", max_percobaan - percobaan)

else:
    print("Terlalu banyak percobaan gagal. Akses ditolak")