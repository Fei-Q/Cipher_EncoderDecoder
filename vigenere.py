from cipher import Cipher

class Vigenere(Cipher):
    '''
    A class representing an Vigenere cipher
    Attributes:
    - text (str): the input text to be encrypted/decrypted, inherited from the superclass Cipher
    - key (str): a word to encode/decode text
    '''
    def __init__(self, text, key):
        '''
        Initializes a Vigenere cipher object
        Parameters: text (inherited from superclass Cipher), key (str)
        Side effects: initializes a Vigenere cipher obejct with the text to be encoded/decoded, and the key to encode/decode it with
        '''
        super().__init__(text)
        self.key = key

    def check_valid_key(self):
        '''
        Check if the key is valid: a string with letters only (no spaces, punctuation, or special characters)
        Parameters: none
        Side effects: none
        Returns: True (valid) or False (invalid)
        '''
        if len(self.key) > 0 and self.key.isalpha():
            return True
        return False

    def set_valid_key(self):
        '''
        Prompts user to enter a valid key
        Parameters: none
        Side effects: updates key to a new value
        Returns: none
        '''
        while self.check_valid_key() == False:
            new_key = input("Invalid key. Please enter a string with letters only: ")
            self.key = new_key

    def extend_key(self):
        '''
        Parameters: none
        Side effects: extends the key to match the length of the text
        - appends the key to the end of extended_key until its length == len(text)
        Returns: extended_key
        '''
        key = self.key.lower()
        text_length = len(self.get_text())
        extended_key = key * (text_length // len(key)) + key[:text_length % len(key)]
        return extended_key

    def encrypt(self):
        '''
        Encrypt a plaintext via Vigenere cipher
        Parameters: none
        Side effects:
        - sets a valid plaintext and key
        - extends the key to match the length of the plaintext
        Returns: encrypted ciphertext (str)
        '''
        self.set_valid_text()
        self.set_valid_key()
        full_key = self.extend_key()
        ciphertext = ''
        for i in range(len(self.get_text())):
            char = self.get_text()[i]
            key = full_key[i]
            if char in self.alphabet_upper:
                ciphertext += self.alphabet_upper[(self.alphabet_upper.index(char) + self.alphabet_lower.index(key)) % 26]
            elif char in self.alphabet_lower:
                ciphertext += self.alphabet_lower[(self.alphabet_lower.index(char) + self.alphabet_lower.index(key)) % 26]
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self):
        '''
        Decrypt a ciphertext via Vigenere cipher
        Parameters: none
        Side effects:
        - sets a valid ciphertext and key
        - extends the key to match the length of the ciphertext
        Returns: decrypted plaintext (str)
        '''
        self.set_valid_text()
        self.set_valid_key()
        full_key = self.extend_key()
        plaintext = ''
        for i in range(len(self.get_text())):
            char = self.get_text()[i]
            key = full_key[i]
            if char in self.alphabet_upper:
                plaintext += self.alphabet_upper[(self.alphabet_upper.index(char) - self.alphabet_lower.index(key)) % 26]
            elif char in self.alphabet_lower:
                plaintext += self.alphabet_lower[(self.alphabet_lower.index(char) - self.alphabet_lower.index(key)) % 26]
            else:
                plaintext += char
        return plaintext

    def __str__(self):
        '''
        Overload string method to print info
        Parameters: none
        Side effects: prints info about Vigenere cipher
        Returns: none
        '''
        description = "  The Vigenère cipher is a classical polyalphabetic substitution cipher that encrypts plaintext by shifting each letter of the message according to a keyword. Essentially, each letter is encoded with a different Caesar cipher (a special case of the Affine cipher with a = 1). The shift for each letter is determined by a keyword mapped onto the Vigenère square.\n"
        description += "  While the Vigenère cipher is also a symmetric cipher, it's more resistant to brute force attacks via frequency analysis compared to simple, monoalphabetic substitution ciphers. Still, it can be broken using techniques such as Kasiski examination, especially if the keyword is relatively short or if patterns exist within the plaintext.\n"
        description += "  For more detailed information, checkout these online resources! https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Algebraic_description"
        return description

if __name__ == "__main__":
    e = Vigenere("For you, a thousand times over.", "IRan") # from 'The Kite Runner' by Khaled Hosseini
    print(f'Test - encryption\nPlain text: {e.get_text()}\nCipher text: {e.encrypt()}')
    
    d = Vigenere("I gjvqmv mzkyci la uzy jmfflf cegqxreswhth gr uzy zwjxd.", "absurdism") # from 'The Stranger' by Albert Camus
    print(f'Test - decryption\nPlain text: {d.get_text()}\nCipher text: {d.decrypt()}')
