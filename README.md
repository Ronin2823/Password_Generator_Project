# Password Generator

## Project Overview
This Python project is a **Password Generator** that creates random, secure passwords based on user-defined criteria such as length and character types (letters, numbers, symbols). It is designed as an introductory project for beginners to learn Python programming fundamentals like string manipulation, user input handling, and working with libraries.

---

## Features
1. User-defined password length.
2. Options to include:
   - Letters (uppercase and lowercase)
   - Numbers
   - Symbols
3. Generates a secure, randomized password based on user preferences.
4. Error handling for invalid inputs or missing criteria.

---

## How It Works
1. The user is prompted to input:
   - Desired password length.
   - Whether to include letters, numbers, and symbols.
2. The program constructs a pool of characters based on the user’s choices.
3. A random password of the specified length is generated and displayed to the user.

---

## Requirements
- Python 3.x

No additional libraries are required as the program uses Python’s built-in `random` module.

---

## How to Run the Program
1. Clone or download this repository.
2. Open a terminal and navigate to the folder containing the `password_generator.py` file.
3. Run the program with:
   ```bash
   python password_generator.py
   ```
4. Follow the prompts to generate your password.

---

## Example Usage
### Input:
```
Enter the desired password length: 12
Include letters? (yes/no): yes
Include numbers? (yes/no): yes
Include symbols? (yes/no): no
```

### Output:
```
Your generated password: a9f6kLr2n1xP
```

---

## File Structure
- `password_generator.py`: The main script containing the password generator logic.

---

## Code Organization
### Functions:
1. **`get_user_input()`**: Handles user input for password preferences.
2. **`build_char_pool()`**: Creates a pool of characters based on user choices.
3. **`generate_password()`**: Generates a random password of the specified length.
4. **`main()`**: Ties everything together and handles program execution.

---

## Future Enhancements
- Add a feature to generate multiple passwords at once.
- Include a password strength evaluation.
- Save generated passwords to a file.
- Add a graphical user interface (GUI).

---

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
