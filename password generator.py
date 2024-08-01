import random
import string

def generate_password(length=10, use_letters=True, use_digits=True, use_symbols=True):
    """
    Generate a random password based on user preferences.

    Parameters:
    - length (int): The length of the password.
    - use_letters (bool): Whether to include letters in the password.
    - use_digits (bool): Whether to include digits in the password.
    - use_symbols (bool): Whether to include symbols in the password.

    Returns:
    - str: The generated password.
    """
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Initialize selection based on user preferences
    selection = ''
    if use_letters:
        selection += letters
    if use_digits:
        selection += digits
    if use_symbols:
        selection += symbols

    # Ensure selection is not empty
    if not selection:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(random.choice(selection) for _ in range(length))

    return password

def main():
    """
    Main function to execute the password generation and display.
    """
    try:
        # Configuration
        length = 12  # Specify the length of the password
        use_letters = True
        use_digits = True
        use_symbols = True

        # Generate and print the password
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print("Generated Password:", password)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
