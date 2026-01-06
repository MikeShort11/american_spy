# Simple Caesar Cipher Encryption without if statements

def encrypt(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    for char in text:
        index = alphabet.index(char)           # find the position of the character
        shifted_index = (index + shift) % 26  # shift it
        result += alphabet[shifted_index]     # get the new character

    return result

# Main program
print("Welcome to Caesar Cipher Encryption!")
message = input("Enter a message to encrypt (lowercase letters only, no spaces): ")
shift = int(input("Enter a shift number: "))

encrypted = encrypt(message, shift)
print("Encrypted message:", encrypted)
