"""
Symmetric encryption algorithms (AES, DES, 3DES)
Simple implementation with proper padding and error handling
"""

from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class AESCipher:
    """AES-256 encryption/decryption"""
    
    def __init__(self):
        self.key_size = 32  # 256 bits = 32 bytes
    
    def generate_key(self):
        """Generate random AES key"""
        return get_random_bytes(self.key_size)
    
    def encrypt(self, plaintext, key):
        """Encrypt text using AES-CBC mode"""
        # Convert key to bytes if string
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        # Ensure key length is correct (32 bytes for AES-256)
        if len(key) != self.key_size:
            # Hash the key to get correct length
            import hashlib
            key = hashlib.sha256(key).digest()
        
        # Generate random IV (Initialization Vector)
        iv = get_random_bytes(AES.block_size)
        
        # Create cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # Pad plaintext to block size and encrypt
        padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
        ciphertext = cipher.encrypt(padded_plaintext)
        
        # Combine IV and ciphertext, then encode as base64
        encrypted_data = iv + ciphertext
        return base64.b64encode(encrypted_data).decode('utf-8')
    
    def decrypt(self, ciphertext_b64, key):
        """Decrypt AES-CBC encrypted text"""
        # Convert key to bytes if string
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        # Ensure key length is correct
        if len(key) != self.key_size:
            import hashlib
            key = hashlib.sha256(key).digest()
        
        # Decode base64
        encrypted_data = base64.b64decode(ciphertext_b64)
        
        # Extract IV and actual ciphertext
        iv = encrypted_data[:AES.block_size]
        ciphertext = encrypted_data[AES.block_size:]
        
        # Create cipher and decrypt
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        
        # Unpad and return
        plaintext = unpad(padded_plaintext, AES.block_size)
        return plaintext.decode('utf-8')

class DESCipher:
    """DES encryption/decryption"""
    
    def __init__(self):
        self.key_size = 8  # 64 bits = 8 bytes
    
    def generate_key(self):
        """Generate random DES key"""
        return get_random_bytes(self.key_size)
    
    def encrypt(self, plaintext, key):
        """Encrypt text using DES-CBC mode"""
        # Convert key to bytes if string
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        # Ensure key length is correct
        if len(key) != self.key_size:
            import hashlib
            key = hashlib.md5(key).digest()[:self.key_size]
        
        # Generate random IV
        iv = get_random_bytes(DES.block_size)
        
        # Create cipher object
        cipher = DES.new(key, DES.MODE_CBC, iv)
        
        # Pad and encrypt
        padded_plaintext = pad(plaintext.encode('utf-8'), DES.block_size)
        ciphertext = cipher.encrypt(padded_plaintext)
        
        # Combine and encode
        encrypted_data = iv + ciphertext
        return base64.b64encode(encrypted_data).decode('utf-8')
    
    def decrypt(self, ciphertext_b64, key):
        """Decrypt DES-CBC encrypted text"""
        # Convert key to bytes if string
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        # Ensure key length is correct
        if len(key) != self.key_size:
            import hashlib
            key = hashlib.md5(key).digest()[:self.key_size]
        
        # Decode base64
        encrypted_data = base64.b64decode(ciphertext_b64)
        
        # Extract IV and ciphertext
        iv = encrypted_data[:DES.block_size]
        ciphertext = encrypted_data[DES.block_size:]
        
        # Decrypt
        cipher = DES.new(key, DES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        
        # Unpad and return
        plaintext = unpad(padded_plaintext, DES.block_size)
        return plaintext.decode('utf-8')

class TripleDESCipher:
    """Triple DES (3DES) encryption/decryption"""
    
    def __init__(self):
        self.key_size = 24  # 192 bits = 24 bytes
    
    def generate_key(self):
        """Generate random 3DES key"""
        return get_random_bytes(self.key_size)
    
    def encrypt(self, plaintext, key):
        """Encrypt text using 3DES-CBC mode"""
        # Convert key to bytes if string
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        # Ensure key length is correct
        if len(key) != self.key_size:
            import hashlib
            key = hashlib.sha256(key).digest()[:self.key_size]
        
        # Generate random IV
        iv = get_random_bytes(DES3.block_size)
        
        # Create cipher object
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        
        # Pad and encrypt
        padded_plaintext = pad(plaintext.encode('utf-8'), DES3.block_size)
        ciphertext = cipher.encrypt(padded_plaintext)
        
        # Combine and encode
        encrypted_data = iv + ciphertext
        return base64.b64encode(encrypted_data).decode('utf-8')
    
    def decrypt(self, ciphertext_b64, key):
        """Decrypt 3DES-CBC encrypted text"""
        # Convert key to bytes if string
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        # Ensure key length is correct
        if len(key) != self.key_size:
            import hashlib
            key = hashlib.sha256(key).digest()[:self.key_size]
        
        # Decode base64
        encrypted_data = base64.b64decode(ciphertext_b64)
        
        # Extract IV and ciphertext
        iv = encrypted_data[:DES3.block_size]
        ciphertext = encrypted_data[DES3.block_size:]
        
        # Decrypt
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        
        # Unpad and return
        plaintext = unpad(padded_plaintext, DES3.block_size)
        return plaintext.decode('utf-8')