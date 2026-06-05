import random

def hangman():
    words = ["python", "django", "flask", "pandas", "numpy"]
    word = random.choice(words)
    guessed = set()
    wrong = 0
    max_wrong = 6

    print("Welcome to Hangman!")

    while wrong < max_wrong:
        # Display current state
        display = [letter if letter in guessed else "_" for letter in word]
        print("\nWord:", " ".join(display))
        print(f"Wrong guesses: {wrong}/{max_wrong}")
        print(f"Guessed letters: {', '.join(sorted(guessed)) if guessed else 'None'}")

        # Check win
        if "_" not in display:
            print("🎉 You won! The word was:", word)
            return

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("Already guessed that!")
            continue

        guessed.add(guess)

        if guess not in word:
            wrong += 1
            print(f"Wrong! '{guess}' is not in the word.")
        else:
            print(f"Good guess! '{guess}' is in the word.")

    print(f"\n💀 Game over! The word was: {word}")

hangman()
