#Number Guessing Game with break
secret_number = 7

while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret_number:
        print ("Congratulations! You got it!")
        break
    else:
        print("Wrong, try again!")