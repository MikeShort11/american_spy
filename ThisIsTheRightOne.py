# Simple Caesar Cipher Encryption without if statements

def encrypt(message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    for letter in message:
        start_index = alphabet.index(letter)
        new_index = start_index + shift
        new_letter = alphabet[new_index % 26]
        result = result + new_letter

    return result
#comments dont affect the code

def decrypt(message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    for letter in message:
        start_index = alphabet.index(letter)
        new_index = start_index - shift
        new_letter = alphabet[new_index % 26]
        result = result + new_letter

    return result 

# Main program
def main():
    print("Welcome to Caesar Cipher Encryption!")
    user_selection = input("Press 1 to encrypt, press 2 to decrypt")
    if user_selection == "2":
        message = input("Enter a message to encrypt (lowercase letters only, no spaces): ")
        shift = int(input("Enter a shift number: "))
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
    if user_selection == "2":
        message = input("Enter a message to decrypt (lowercase letters only, no spaces): ")
        shift = int(input("Enter a shift number: "))
        decrypted = decrypt(message, shift)
        print("decrypted message:", decrypted)      

if __name__ == "__main__":
    main()
