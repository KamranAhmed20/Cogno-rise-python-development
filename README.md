# Hangman Game

Welcome to the **Hangman Game**! This is a simple Python implementation of the classic word-guessing game where players try to guess a hidden word one letter at a time. The game includes a visual representation of the hangman, which updates with each incorrect guess.

## Features

- **Random Word Selection**: The game randomly selects a word from a predefined list for the player to guess.
- **Visual Hangman**: A visual representation of the hangman is displayed, which progresses as the player makes incorrect guesses.
- **Input Validation**: Ensures that the player's input is a single alphabetic character.
- **Win/Lose Conditions**: The player wins by guessing the word correctly within the allowed number of incorrect guesses. If they run out of guesses, they lose and the correct word is revealed.

## How to Play

1. The game will prompt you to guess a letter in the hidden word.
2. If your guess is correct, the letter will be revealed in its correct position(s).
3. If your guess is incorrect, a part of the hangman will be drawn.
4. You have a maximum of 6 incorrect guesses before the game is over.
5. The game ends when you either guess the word correctly or use up all your guesses.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.


## Example Output

Welcome to Hangman!

| |
|
|
|
|
Word: _ _ _ _ _ _
Guess a letter: e
Good guess! 'e' is in the word.

| |
|
|
|
|
Word: _ _ e _ _ _

...

Congratulations! You guessed the word: 'example'



## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the classic hangman game.
- Thanks to the Python community for their support and resources.

