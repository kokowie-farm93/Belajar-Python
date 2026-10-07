angka = 1
while angka <= 5:
    print(angka)
    angka += 1 # artinya angka + !, wajib +=

password = ""

while password != "12345":
    password = input("Entry password : ")
    if password != "12345":
        print("Uncorrect Password")
print("Correct Password")