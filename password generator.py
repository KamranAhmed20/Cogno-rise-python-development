import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    """
    Generate a random password based on specified criteria.

    Parameters:
    - length (int): Length of the generated password.
    - use_letters (bool): Whether to include letters.
    - use_digits (bool): Whether to include digits.
    - use_symbols (bool): Whether to include symbols.

    Returns:
    - str: The generated password.
    """
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine selected character types
    characters = ''
    if use_letters:
        characters += letters
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols

    # Ensure at least one character type is included
    if not characters:
        raise ValueError("You must select at least one type of character.")

    # Generate password
    return ''.join(random.choice(characters) for _ in range(length))

def get_user_input():
    """
    Prompt user for the desired length and character types for the password.

    Returns:
    - tuple: (length, use_letters, use_digits, use_symbols)
    """
    # Get the length of the password from the user
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("The length must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Ask the user for character type preferences
    use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

    return length, use_letters, use_digits, use_symbols

def main():
    """
    Main function to execute the password generation based on user input.
    """
    print("Welcome to the Password Generator!")
    
    # Get user preferences
    length, use_letters, use_digits, use_symbols = get_user_input()

    try:
        # Generate and display the password
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"Your generated password is: {password}")
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()
