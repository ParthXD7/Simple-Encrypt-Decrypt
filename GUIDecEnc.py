import tkinter as tk
from tkinter import messagebox

# Function for encryption
def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  # Check if the character is alphabetic
            shift_base = 65 if char.isupper() else 97  # For uppercase and lowercase letters
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

# Function for decryption
def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Check if the character is alphabetic
            shift_base = 65 if char.isupper() else 97  # For uppercase and lowercase letters
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    return decrypted_text

# Function to handle the encryption/decryption process
def process_text():
    operation = operation_var.get()
    text = text_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Shift value must be an integer.")
        return

    if operation == "e":
        result = encrypt(text, shift)
        result_label.config(text=f"Encrypted text: {result}")
    elif operation == "d":
        result = decrypt(text, shift)
        result_label.config(text=f"Decrypted text: {result}")
    else:
        messagebox.showerror("Invalid choice", "Please choose 'Encrypt' or 'Decrypt'.")
    
    # Enable the copy button
    copy_button.config(state=tk.NORMAL)

# Function to copy the result to the clipboard
def copy_to_clipboard():
    result_text = result_label.cget("text").replace("Encrypted text: ", "").replace("Decrypted text: ", "")
    root.clipboard_clear()
    root.clipboard_append(result_text)
    messagebox.showinfo("Copied", "Text copied to clipboard.")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Tool By ParthXD7")

# Operation selection
operation_var = tk.StringVar(value="e")
tk.Radiobutton(root, text="Encrypt", variable=operation_var, value="e").grid(row=0, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Decrypt", variable=operation_var, value="d").grid(row=0, column=1, padx=10, pady=10)

# Text input
tk.Label(root, text="Enter text:").grid(row=1, column=0, padx=10, pady=10)
text_entry = tk.Entry(root, width=50)
text_entry.grid(row=1, column=1, padx=10, pady=10)

# Shift input
tk.Label(root, text="Enter shift value:").grid(row=2, column=0, padx=10, pady=10)
shift_entry = tk.Entry(root)
shift_entry.grid(row=2, column=1, padx=10, pady=10)

# Process button
process_button = tk.Button(root, text="Process", command=process_text)
process_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.grid(row=5, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
