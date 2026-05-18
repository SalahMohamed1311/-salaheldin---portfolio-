"""
Hashing algorithms (SHA-256 and MD5)
Note: Hashing is one-way and cannot be reversed
"""

import hashlib

class HashTools:
    """Collection of hash functions"""
    
    def sha256_hash(self, text):
        """
        Generate SHA-256 hash
        SHA-256 produces a 64-character hexadecimal string
        """
        text_bytes = text.encode('utf-8')
        hash_object = hashlib.sha256(text_bytes)
        return hash_object.hexdigest()
    
    def md5_hash(self, text):
        """
        Generate MD5 hash
        MD5 produces a 32-character hexadecimal string
        Note: MD5 is considered cryptographically broken for security purposes
        """
        text_bytes = text.encode('utf-8')
        hash_object = hashlib.md5(text_bytes)
        return hash_object.hexdigest()