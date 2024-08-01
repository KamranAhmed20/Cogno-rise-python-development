import random

# Step 1: Word List
word_list = ['python', 'hangman', 'challenge', 'programming', 'development', 'interface', 'functionality', 'algorithm']

def get_random_word(word_list):
    """Step 2: Select a random word from the list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Step 3: Show underscores for unguessed letters."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def display_hangman(incorrect_guesses):
    """Step 6: Display the hangman figure for incorrect guesses."""
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(hangman_stages[incorrect_guesses])

def play_hangman():
    word = get_random_word(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")

    # Step 4: Initial Display
    while incorrect_guesses < max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        print("\nWord: " + display_word(word, guessed_letters))
        
        # Step 5: User Input
        guess = input("Guess a letter: ").lower()
        
        # Step 6: Check Letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        # Step 7: Win/Loss Check
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        display_hangman(incorrect_guesses)
        print(f"\nGame Over! The word was: {word}")

    # Step 8: Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_hangman()
    else:
        print("Thank you for playing!")

# Step 9: User Interface and Game Start
if __name__ == "__main__":
    play_hangman()
