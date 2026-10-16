username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":

    if password == "admin123":
        print("Access granted.")
    else:
        print("Incorrect password.")
else:
    print("Incorrect username.")