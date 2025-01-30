import random
import hashlib
from datetime import datetime #added real time date so the user can see his history save
import tkinter as tk
from tkinter import messagebox, filedialog

def generate_password(length, include_letters, include_numbers, include_symbols):
    """Generate a password of the specified length from the character pool."""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    
    char_pool = ""
    if include_letters:
        char_pool += letters
    if include_numbers:
        char_pool += numbers
    if include_symbols:
        char_pool += symbols
    
    if not char_pool:
        raise ValueError("No character types selected! At least one type must be included.")
    
    return ''.join(random.choice(char_pool) for _ in range(length))

def hash_and_save_password(password, file_name):
    """Hash the password using SHA-256 and save it to a file with a timestamp."""
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, "a") as file:
        file.write(f"Timestamp: {timestamp}\nPassword: {password}\nHash: {hashed_password}\n---\n")
    messagebox.showinfo("Success", f"Password hashed and saved to {file_name}")

def generate_and_save():
    try:
        length = int(length_entry.get())
        include_letters = letters_var.get()
        include_numbers = numbers_var.get()
        include_symbols = symbols_var.get()
        file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if not file_name:
            return
        
        password = generate_password(length, include_letters, include_numbers, include_symbols)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        hash_and_save_password(password, file_name)
    except ValueError as e:
        messagebox.showerror("Error", str(e))        

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2, sticky="w")

tk.Button(root, text="Generate & Save", command=generate_and_save).grid(row=4, column=0, columnspan=2)

password_entry = tk.Entry(root, width=40)
password_entry.grid(row=5, column=0, columnspan=2)

root.mainloop()