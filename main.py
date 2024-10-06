from affine import Affine
from vigenere import Vigenere
from autokey import Autokey

def main():
    '''
    Main function for running different ciphers
    Parameters: none
    Side effects:
    - Prompts user inputs for choosing cipher type, operation (encrypt/decrypt), text input, and key input
    - Displays the result of the encryption/decryption
    Returns: none
    '''
    
    # Choose cipher type
    cipher = input("Which type of cipher would you like to use? Enter 'Affine', 'Vigenere', or 'Autokey'' to proceed, or enter 'Help' to learn more about what each cipher does: ").lower()
    cipher_status = False
    while cipher_status == False:
        if cipher == 'affine' or cipher == 'vigenere' or cipher == 'autokey':
            cipher_status = True
            break
        elif cipher == 'help':
            info = input("Which cipher would you like to learn more about? Enter 'Affine', 'Vigenere', or 'Autokey': ").lower()
            if info == 'affine':
                t = Affine('Hello World!')
                print(f"{'-' * 50}\nDescription of the Affine Cipher:\n{t}")
                cipher = input(f"{'-' * 50}\nWould you like to try a cipher? Enter 'Affine', 'Vigenere', or 'Autokey' to proceed, or enter 'Help' to learn more about what other ciphers do: ").lower()
            elif info == 'vigenere':
                t = Vigenere('Hello World!', 'hey')
                print(f"{'-' * 50}\nDescription of the Vigenere Cipher:\n{t}")
                cipher = input(f"{'-' * 50}\nWould you like to try a cipher? Enter 'Affine', 'Vigenere', or 'Autokey' to proceed, or enter 'Help' to learn more about what other ciphers do: ").lower()
            elif info == 'autokey':
                t = Autokey('Hello World!', 'hey')
                print(f"{'-' * 50}\nDescription of the Autokey Cipher:\n{t}")
                cipher = input(f"{'-' * 50}\nWould you like to try a cipher? Enter 'Affine', 'Vigenere', or 'Autokey' to proceed, or enter 'Help' to learn more about what other ciphers do: ").lower()
            else:
                cipher = input("Please enter a valid input: ").lower()
        else:
            cipher = input("Please enter a valid input: ").lower()

    # Choose operation
    operation = input("Would you like to encrypt or decrypt? Enter 'Encrypt' or 'Decrypt', or press return and the default will be encrypt: ").lower() or 'encrypt'
    operation_status = False
    while operation_status == False:
        if operation == 'encrypt' or operation == 'decrypt':
            operation_status = True
            break
        else:
            operation = input("Please enter a valid operation, or press return to use the default operation encrypt: ").lower() or 'encrypt'
    
    # Enter the text to encrypt/decrypt
    text = ''
    if operation == 'encrypt':
        text = input("Please enter the text to encrypt: ")
    elif operation == 'decrypt':
        text = input("Please enter the text to decrypt: ")
    
    # Enter keys
    key = ''
    if cipher == "affine":
        print("The affine cipher requires two integer keys to encode via the function (ax + b) mod 26.")
        a = input("Enter an integer value for 'a' that's not 0 and not coprime to 26 (i.e. not a multiple of 2 or 13), or press return to use the default value 1: ") or 1
        b = input("Enter an integer value for 'b', or press return to use the default value 1: ") or 1
        c = Affine(text, a, b)
        key = f"a={a}, b={b}" # saved in this format for printing later
    elif cipher == "vigenere":
        key = input("Enter a string with letters only (no punctuation, spaces, or other characters) as the key: ")
        c = Vigenere(text, key)
    elif cipher == "autokey":
        key = input("Enter a string with letters only (no punctuation, spaces, or other characters) as the key: ")
        c = Autokey(text, key)

    # Perform encryption/decryption
    result = ''
    if operation == "encrypt":
        result = c.encrypt()
    elif operation == "decrypt":
        result = c.decrypt()

    # Print the result
    print(f"{'-' * 50}")
    display = f"{cipher.capitalize()} cipher"
    if operation == 'encrypt':
        display += f" -- Encryption\nKey: {key}\nPlaintext: {text}\nCiphertext: {result}"
    elif operation == 'decrypt':
        display += f" -- Decryption\nKey: {key}\nCiphertext: {text}\nPlaintext: {result}"
    print(display)
    print(f"{'-' * 50}")

    # Write the result to a file
    save = input("Want to save the result in a file? Enter 'Yes' to save it or press return for 'No': ").lower() or 'no'
    if save == 'yes':
        file_name = input("Enter a file name (don't include the extension): ")
        file_name += '.txt'  # Add the .txt extension to the file name
        try:
            with open(file_name, 'w') as file:
                file.write(display)
            print(f"Result saved to {file_name}!")
        except Exception as e:
            print(f"Oops! An error occurred while writing to the file: {e}.")

if __name__ == "__main__":
    main()

