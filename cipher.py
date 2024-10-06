class Cipher:
    '''
    A class representing a cipher (general base class for all ciphers)
    Attributes:
    - text (str): the input text to be encrypted/decrypted
    '''
    def __init__(self, text):
        '''
        Initializes a new Cipher object
        Parameters: text (user input for text to be encoded) [private]
        Side effects: initializes a new Cipher object with input text
        Returns: none
        '''
        self.set_text(text)
    
    '''Setters and getters for text'''
    def set_text(self, text):
        self.__text = text
    def get_text(self):
        return self.__text

    alphabet_lower = [chr(i) for i in range(97, 123)] # lowercase alphabet
    alphabet_upper = [chr(i) for i in range(65, 91)] # uppercase alphabet

    def check_valid_text(self):
        '''
        Check if text input is valid (i.e. not an empty string)
        Parameters: none
        Side effects: none
        Returns: True (len > 0) or False (empty string)
        '''
        return len(self.__text) > 0 # return True if len > 0

    def set_valid_text(self):
        '''
        Prompts user to enter a valid text input
        Parameters: none
        Side effects: updates text to a valid input
        Returns: none
        '''
        while self.check_valid_text() == False:
            new_text = input('Enter a valid string with text using the English alphabet: ')
            self.set_text(new_text)
    
    def mod_inverse(self, x):
        '''
        Calculates the modular inverse of a number
        - equation: (x * x^-1) mod 26 = 1
        - required for decryption of some ciphers (e.g. Affine cipher)
        Parameters: x
        Side effects: none
        Returns: y (modular inverse of x: y = x^-1)
        '''
        for y in range(26):
            if (x * y) % 26 == 1:
                return y
