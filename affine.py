from cipher import Cipher

class Affine(Cipher):
    '''
    A class representing an Affine cipher
    - famous Affine ciphers include the Caesar cipher (a = 1), Atbash cipher (a = -1), and ROT13 (Caesar cipher with b = 13)
    Attributes:
    - text (str): the input text to be encrypted/decrypted, inherited from the superclass Cipher
    - a (int): variable to encode/decode text
    - b (int): variable to encode/decode text
    '''
    def __init__(self, text, a=1, b=1):
        '''
        Initializes an Affine cipher object
        Parameters: text (inherited from superclass Cipher), a (default: 1), b (defalut: 1)
        Side effects: initializes an Affine cipher obejct with the text to be encoded/decoded, and the varialbes a and b to encode/decode it with
        '''
        super().__init__(text)
        self.a = a
        self.b = b

    def check_valid_a(self):
        '''
        Check if variable 'a' is valid:
        - a number -> can be transformed into an integer
        - cannot be 0
        - must be coprime to 26 (i.e. not a multiple of 2 or 13)
        Parameters: none
        Side effects: none
        Returns: True (valid) or False (invalid)
        '''
        try:
            self.a = int(self.a)
            if (self.a != 0) and (self.a % 2 != 0) and (self.a % 13 != 0):
                return True
            return False
        except ValueError:
            return False

    def set_valid_a(self):
        '''
        Prompts user to enter a valid value for 'a', or skip and use the default value 1
        Parameters: none
        Side effects: updates 'a' to a new value
        Returns: none
        '''
        while self.check_valid_a() == False:
            new_a = input("Invalid value for 'a'. Please enter a valid integer, or press return and a default value of 1 will be used: ") or 1
            self.a = new_a
    
    def check_valid_b(self):
        '''
        Check if variable 'b' is valid:
        - a number -> can be transformed into an integer
        Parameters: none
        Side effects: none
        Returns: True (valid) or False (invalid)
        '''
        try:
            self.b = int(self.b)
            return True
        except ValueError:
            return False
    
    def set_valid_b(self):
        '''
        Prompts user to enter a valid value for 'b', or skip and use the default value 1
        Parameters: none
        Side effects: updates 'b' to a new value
        Returns: none
        '''
        while self.check_valid_b() == False:
            new_b = input("Invalid value for 'b'. Please enter a valid integer, or press return and a default value of 1 will be used: ") or 1
            self.b = new_b

    def encrypt(self):
        '''
        Encrypt a plaintext via Affine cipher
        Parameters: none
        Side effects: sets the text, 'a', and 'b' attributes of the Affine cipher object
        Returns: encrypted ciphertext (str)
        '''
        ciphertext = ''
        self.set_valid_text()
        self.set_valid_a()
        self.set_valid_b()
        for char in self.get_text():
            if char in self.alphabet_upper:
                ciphertext += self.alphabet_upper[(self.a * self.alphabet_upper.index(char) + self.b) % 26]
            elif char in self.alphabet_lower:
                ciphertext += self.alphabet_lower[(self.a * self.alphabet_lower.index(char) + self.b) % 26]
            else:
                ciphertext += char
        return ciphertext
    
    def decrypt(self):
        '''
        Decrypt a ciphertext via Aphine cipher
        Parameters: none
        Side effects: sets the text, 'a', and 'b' attributes of the Affine cipher object
        Returns: decrypted plaintext (str)
        '''
        plaintext = ''
        self.set_valid_text()
        self.set_valid_a()
        self.set_valid_b()
        a_inverse = self.mod_inverse(self.a)
        for char in self.get_text():
            if char in self.alphabet_upper:
                plaintext += self.alphabet_upper[(a_inverse * (self.alphabet_upper.index(char) - self.b)) % 26]
            elif char in self.alphabet_lower:
                plaintext += self.alphabet_lower[(a_inverse * (self.alphabet_lower.index(char) - self.b)) % 26]
            else:
                plaintext += char
        return plaintext
    
    def __str__(self):
        '''
        Overload string method to print info
        Parameters: none
        Side effects: prints info about Affine cipher
        Returns: none
        '''
        description = "  The affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter. Each letter is enciphered with the function (ax + b) mod 26, where b is the magnitude of the shift.\n"
        description += "  The cipher is symmetric, meaning that it can be encrypted and decrypted using the same key. As such, it has the weaknesses of all substitution ciphers.\n"
        description += "  For more detailed information, checkout these online resources! https://en.wikipedia.org/wiki/Affine_cipher"
        return description

if __name__ == "__main__":
    e = Affine("There ain't no sin and there ain't no virtue. There's just stuff people do.",'3','7') # from 'The Count of Monte Cristo' by Alexandre Dumas
    print(f'\nTest - encryption\nPlain text: {e.get_text()}\nCipher text: {e.encrypt()}')
    
    d = Affine("Svv sfgasve szm muosv, xoj ekam sfgasve szm akzm muosv jbsf kjbmze.",5,18) # from 'Animal Farm' by George Orwell
    print(f'\nTest - decryption\nPlain text: {d.get_text()}\nCipher text: {d.decrypt()}')
