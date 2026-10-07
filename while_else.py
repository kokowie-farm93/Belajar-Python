# Find Correct password with attempt limit
correct_password = "python123"
attempt = 0
max_attempt = 3

while attempt < max_attempt:
    password = input("Enter password: ")
    attempt += 1

    if password == correct_password:
        print("Login succesful!")
        break
    else:
        print("Incorrect Password. Attempt left:", max_attempt - attempt)

else:
    print("Too many failed attempts. Access denied")