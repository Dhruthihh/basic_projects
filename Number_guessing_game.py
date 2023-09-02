import random

secret_number = random.randint(1,100)
attempts = 0
max_attempts = 5

print("WELCOME TO NUMBER GUESSING GAME!")
#print("Guess a number between 1-100.")

while attempts < max_attempts:
    try:
        guess = int(input("Guess the number between 1-100:"))
        attempts += 1
        if guess == secret_number:
            print("Hurray!You guessed the correct number")
        elif guess < secret_number:
            print("guess a higher number")
        else:
            print("Guess a lower number")
    except ValueError:
        print("Invalid input.Guess a number between 1-100")
        
        
    if attempts>=max_attempts:
        print("You ran out of atempts")
        break