import random

# List of words to guess from
word_list = ['python', 'hangman', 'challenge', 'programming', 'development']

def get_random_word(word_list):
    """Choose a random word from the list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Display the word with underscores for letters that haven't been guessed."""
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def display_hangman(incorrect_guesses):
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
    
    while incorrect_guesses < max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        print("\nWord: " + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
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
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        display_hangman(incorrect_guesses)
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
