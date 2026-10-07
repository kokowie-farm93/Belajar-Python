#Game Tebak angka dengan break
secret_number = 7

while True:
    guess = int(input("Guess number (1-10): "))
    if guess == secret_number:
        print ("Congrats! Right Answer!")
        break
    else:
        print("False, try again!")