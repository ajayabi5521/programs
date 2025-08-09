import random

# Setup
number_to_guess = random.randint(1, 100)
guesses = []

print("🎯 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess in guesses:
            print("⚠️ You've already guessed that number!")
            continue

        guesses.append(guess)

        if guess == number_to_guess:
            print(f"✅ Correct! You guessed it in {len(guesses)} tries.")
            print("Your guesses:", guesses)
            break

        # Feedback
        if len(guesses) > 1:
            prev_diff = abs(guesses[-2] - number_to_guess)
            curr_diff = abs(guess - number_to_guess)
            if curr_diff < prev_diff:
                print("🔥 Warmer!")
            else:
                print("❄️ Colder!")

        if guess < number_to_guess:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

    except ValueError:
        print("Please enter a valid number.")
