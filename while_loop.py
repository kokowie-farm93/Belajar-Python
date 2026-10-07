number = 1
while number <= 5:
    print(number)
    number += 1 # is mean +1, must use +=

password = ""

while password != "12345":
    password = input("Entry password : ")
    if password != "12345":
        print("Incorrect Password")
print("Correct Password")