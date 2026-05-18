"""
RSA asymmetric encryption implementation
Public key for encryption, private key for decryption
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

class RSACipher:
    """RSA encryption/decryption using 2048-bit keys"""
    
    def __init__(self):
        self.key_size = 2048
    
    def generate_keys(self):
        """
        Generate RSA public and private key pair
        Returns: (public_key_pem, private_key_pem)
        """
        # Generate RSA key pair
        key = RSA.generate(self.key_size)
        
        # Extract private key
        private_key = key.export_key('PEM')
        
        # Extract public key
        public_key = key.publickey().export_key('PEM')
        
        # Convert to string
        return public_key.decode('utf-8'), private_key.decode('utf-8')
    
    def encrypt(self, plaintext, public_key_pem):
        """
        Encrypt text using RSA public key
        - Public key is used for encryption (anyone can encrypt)
        - Only private key holder can decrypt
        """
        # Load public key
        public_key = RSA.import_key(public_key_pem)
        
        # Create cipher object
        cipher = PKCS1_OAEP.new(public_key)
        
        # Encrypt the message
        # RSA can only encrypt small amounts of data (key_size/8 - 42 bytes)
        # For longer messages, we'd need hybrid encryption
        ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
        
        # Return base64 encoded ciphertext
        return base64.b64encode(ciphertext).decode('utf-8')
    
    def decrypt(self, ciphertext_b64, private_key_pem):
        """
        Decrypt text using RSA private key
        - Private key is used for decryption (keep secret!)
        """
        # Load private key
        private_key = RSA.import_key(private_key_pem)
        
        # Create cipher object
        cipher = PKCS1_OAEP.new(private_key)
        
        # Decode base64 and decrypt
        ciphertext = base64.b64decode(ciphertext_b64)
        plaintext = cipher.decrypt(ciphertext)
        
        return plaintext.decode('utf-8')