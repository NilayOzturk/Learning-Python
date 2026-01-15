import random
print("---Number Guessing Game---")
print("I'm guessng a number between 1 to 100.")

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Your guess: "))
    if guess < secret_number:
        print("Go HIGHER!")
    elif guess > secret_number:
        print("Go  LOWER!")
    else:
        print("🎉 CONGRATULATIONS! You found it!")
        break