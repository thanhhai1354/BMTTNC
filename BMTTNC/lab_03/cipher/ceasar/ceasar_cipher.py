from cipher import ALPHABET  
class CeasarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        self.alphabet_len = len(ALPHABET)

    def encrypt_text(self, text: str, key: int) -> str:
        text = text.upper()  
        encrypted_text = []
        for letter in text:
            if letter not in self.alphabet:
                encrypted_text.append(letter)
                continue
            letter_index = self.alphabet.index(letter)
            shifted_index = (letter_index + key) % self.alphabet_len
            encrypted_letter = self.alphabet[shifted_index]
            encrypted_text.append(encrypted_letter)
        return "".join(encrypted_text)
    
    def decrypt_text(self, text: str, key: int) -> str:
        return self.encrypt_text(text, -key)