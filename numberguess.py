import random

def guess_the_number():
    a = int(input("Enter the 1st number: "))
    b= int(input("Enter the 2nd number: "))

    number_guess = random.randint(a,b)
    attempts = 0

    print("---------------Welcome to guess the number game----------------")
    print(f"System has selected a number between {a} and {b}, guess the number between them.....")
    
    while True:

        guess = int(input("Enter the number you have guessed: "))
        attempts += 1

        if guess <  a or guess > b:
            print(f"Please enter the number between {a} and {b}")

        elif guess < number_guess:
            print("Too low.....Try again")

        elif guess > number_guess:
            print("Too high.....Try again")

        else:
            print(f"Congrats....You guessed the correct number in {attempts} attempts.")
            break
guess_the_number()