"""
Encoding/Decoding utilities for Base64, Hex, and URL encoding
"""

import base64
import urllib.parse

class EncodingTools:
    """Collection of encoding/decoding functions"""
    
    def base64_encode(self, text):
        """Encode text to Base64"""
        text_bytes = text.encode('utf-8')
        encoded_bytes = base64.b64encode(text_bytes)
        return encoded_bytes.decode('utf-8')
    
    def base64_decode(self, encoded_text):
        """Decode Base64 to text"""
        encoded_bytes = encoded_text.encode('utf-8')
        decoded_bytes = base64.b64decode(encoded_bytes)
        return decoded_bytes.decode('utf-8')
    
    def hex_encode(self, text):
        """Encode text to hexadecimal"""
        text_bytes = text.encode('utf-8')
        return text_bytes.hex()
    
    def hex_decode(self, hex_text):
        """Decode hexadecimal to text"""
        bytes_obj = bytes.fromhex(hex_text)
        return bytes_obj.decode('utf-8')
    
    def url_encode(self, text):
        """URL encode text"""
        return urllib.parse.quote(text, safe='')
    
    def url_decode(self, encoded_text):
        """URL decode text"""
        return urllib.parse.unquote(encoded_text)