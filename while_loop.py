number = 1
while number <= 5:
    print(number)
    number += 1 # is mean +1, must use +=

password = ""

while password != "12345":   # keep looping while the password is not equal to "12345"
    password = input("Enter password : ")
    if password != "12345":
        print("Incorrect Password")
print("Login successful")