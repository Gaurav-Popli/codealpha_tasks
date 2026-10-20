import random

def play_hangman():
    # 1) Predefined list of 5 words
    words = ['python', 'codealpha', 'program', 'developer', 'script']

    # Randomly selecting any one word
    secret_word = random.choice(words)

    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("===================")
    print("Welcome to Hangman Game")
    print("===================")
    print(f"Guess the hidden word! You have {max_incorrect} incorrect attempts.\n")

    # Game loop
    while incorrect_guesses < max_incorrect:
        # Displaying current progress (like 'p _ t h _ _')
        display_word = ''
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '

        print(f'Word: {display_word.strip()}')
        print(f'Incorrect guesses left: {max_incorrect - incorrect_guesses}')
        print(f'Guessed letters: {", ".join(guessed_letters) if guessed_letters else "None"}')

        # Check if the player has guessed all letters
        all_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_guessed = False
                break

        if all_guessed:
            print('\n Congratulations! You guessed the word correctly!')
            print(f'The secret word was: {secret_word}')
            return

        # Get user input
        guess = input('\nGuess a letter: ').lower().strip()

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print(' Invalid input. Please enter a single letter.\n')
            continue

        if guess in guessed_letters:
            print(' You already guessed that letter! Try another one.\n')
            continue

        # Add guess to history
        guessed_letters.append(guess)

        # Checking if guess is in secret_word
        if guess in secret_word:
            print(' Correct guess!\n')
        else:
            incorrect_guesses += 1
            print(' Wrong guess!\n')

    # If maximum incorrect attempts reached
    print("===============")
    print(' Game over!!!')
    print(f'You ran out of attempts. The word was: {secret_word}')
    print("===============")

if __name__ == '__main__':
    play_hangman()