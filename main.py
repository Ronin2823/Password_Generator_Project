import random

def get_user_input():
    """Get user preferences for the password."""
    length = int(input("Enter the desired password length: "))
    include_letters = input("Include letters? (yes/no): ").strip().lower()
    include_numbers = input("Include numbers? (yes/no): ").strip().lower()
    include_symbols = input("Include symbols? (yes/no): ").strip().lower()
    return length, include_letters, include_numbers, include_symbols


def build_char_pool(include_letters,include_numbers,include_symbols):
    """Build the character pool based on user preferences"""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    numbers = "0123456789"

    char_pool = ""
    if include_letters == "yes":
        char_pool += letters
    if include_numbers == "yes":
        char_pool += numbers
    if include_symbols == "yes":
        char_pool += symbols
    if not char_pool:
        raise ValueError("No character types selected! At least one type must be included.")
    return char_pool


def generate_password(length,char_pool):
    """Generate a password of the specified length from the character pool."""
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password


def main():
    """Main program flow."""
    try: 
        #Step 1: get user input
        length, include_letters, include_numbers, include_symbols = get_user_input()

        #Step 2: Build the character pool
        char_pool = build_char_pool(include_letters, include_numbers, include_symbols)

        #Step 3: Generate the password 
        password = generate_password(length,char_pool)

        #Step 4: Display the password 
        print("Yout generated password:", password)
    except ValueError as e: 
        print(e)

#Run the program 
if __name__ == "__main__":
    main()