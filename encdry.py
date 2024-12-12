# Simple Encryption/Decryption Tool using Caesar Cipher

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

# Main function
def main():
    print("Welcome to the Simple Encryption/Decryption Tool!")
    
    # Get input from the user
    operation = input("Would you like to (E)ncrypt or (D)ecrypt? ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (integer): "))
    
    if operation == "e":
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted text: {encrypted_text}")
    elif operation == "d":
        decrypted_text = decrypt(text, shift)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid choice! Please choose 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
