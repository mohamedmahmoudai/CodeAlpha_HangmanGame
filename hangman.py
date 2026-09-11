import random

def play_hangman():
    # 1. Predefined list of 5 words as specified in the requirements
    words = ["python", "codealpha", "developer", "program", "script"]
    
    # Select a random word from the list
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("========================================")
    print("      Welcome to CodeAlpha Hangman!     ")
    print("========================================")
    print("Guess the word one letter at a time.")
    print(f"You have a maximum of {max_incorrect} incorrect guesses allowed.\n")

    # Main Game Loop
    while incorrect_guesses < max_incorrect:
        # Display current progress of the word
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"Word: {display_word.strip()}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        print(f"Letters guessed so far: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Check win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the correct word!")
            print(f"The word was indeed: '{word_to_guess}'")
            break

        # Get player input
        guess = input("\nEnter a letter: ").lower().strip()

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter from A to Z.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already guessed the letter '{guess}'. Try a different one!")
            continue

        # Process guess
        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"✅ Great job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.")

        print("-" * 40)

    # Check lose condition
    if incorrect_guesses == max_incorrect:
        print("\n❌ Game Over! You ran out of attempts.")
        print(f"The correct word was: '{word_to_guess}'")

if __name__ == "__main__":
    play_hangman()
