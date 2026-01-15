import random
print("🎲---Number Guessing Game---🎲")
print("I'm guessing a number between 1 to 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Your guess: "))
        attempts +=1
        if guess < secret_number:
            print("❌ Too low! Go HIGHER ⬆️!")
        elif guess > secret_number:
            print("❌ Too high! Go LOWER ⬇️")
        else:
            print(f"🎉 CONGRATULATIONS! You found it in {attempts} try!")

            if attempts == 1:
                print("🌟 Rank: INCREDIBLE! Are you a psychic?!")
            elif attempts <= 5:
                print("😎 Rank: Genius! Very smart strategy.")
            elif attempts <= 10:
                print("👍 Rank: Good job! Above average.")
            else:
                print("😅 Rank: You struggled a bit, but you made it!")
            
            break

    except ValueError:
        print("⚠️ Please enter a valid number only!")