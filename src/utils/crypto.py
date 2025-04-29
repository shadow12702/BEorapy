from cryptography.fernet import Fernet

CHARACTER_SET = 'utf-8'

class Crypto:
        
    def __init__(self, secret_key:str):
        try:
            self.fernet = Fernet(secret_key.encode(CHARACTER_SET))
        except Exception as ex:
            raise ex
    
    def encrypt(self, plaintext):
        '''Encrypt the plaintext'''
        try:
            value = self.fernet.encrypt(plaintext.encode())
            return value.decode(CHARACTER_SET)
        except:
            return plaintext

    def decrypt(self, encrypted_text):
        '''Decrypt the encrypted text'''
        try:
            value = self.fernet.decrypt(encrypted_text.encode())
            return value.decode(CHARACTER_SET)
        except Exception as ex:
            print(ex)
            return  encrypted_text

    @staticmethod
    def generate_key():
        '''Generate key for cryptography'''
        return Fernet.generate_key().decode(CHARACTER_SET)
    