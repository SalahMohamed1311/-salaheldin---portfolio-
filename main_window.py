"""
Main application window with tabbed interface
Organizes all crypto tools in a professional layout
"""

from PyQt6.QtWidgets import (QMainWindow, QTabWidget, QWidget, QVBoxLayout,
                             QHBoxLayout, QGroupBox, QLabel, QPushButton,
                             QMessageBox, QFileDialog, QStatusBar, QApplication)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QFont

from ui.styles import apply_styles
from ui.widgets import (StyledTextArea, ModernButton, CopyButton,
                        InfoLabel, AlgorithmSelector, KeyInput)
from algorithms.symmetric_ciphers import AESCipher, DESCipher, TripleDESCipher
from algorithms.rsa_cipher import RSACipher
from algorithms.encoding import EncodingTools
from algorithms.hashing import HashTools


class MainWindow(QMainWindow):
    """Main application window"""

    def __init__(self):
        super().__init__()
        # Set window title - this appears in the title bar
        self.setWindowTitle(" Crypto machine")
        
        # Set window icon (optional - using default for now)
        # You can add an icon file later
        
        # Smaller compact size for MacBook Air M4
        self.setMinimumSize(800, 600)
        self.resize(900, 650)
        self.center_window()

        # Initialize cipher objects
        self.aes_cipher = AESCipher()
        self.des_cipher = DESCipher()
        self.triple_des_cipher = TripleDESCipher()
        self.rsa_cipher = RSACipher()
        self.encoding_tools = EncodingTools()
        self.hash_tools = HashTools()

        # Setup UI
        self.setup_ui()

        # Apply styling
        apply_styles(self)

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Secure Crypto Toolkit Active")

    def center_window(self):
        """Center window on screen"""
        screen = self.screen().availableGeometry()
        center = screen.center()
        self.move(center.x() - self.width() // 2, center.y() - self.height() // 2)

    def setup_ui(self):
        """Setup all UI components"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(8)
        main_layout.setContentsMargins(10, 8, 10, 8)

        header = self.create_header()
        main_layout.addWidget(header)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_symmetric_tab(), "🔒 Symmetric")
        self.tabs.addTab(self.create_rsa_tab(), "🔑 RSA")
        self.tabs.addTab(self.create_encoding_tab(), "📝 Encoding")
        self.tabs.addTab(self.create_hashing_tab(), "🔐 Hashing")

        main_layout.addWidget(self.tabs, stretch=1)

    def create_header(self):
        """Create application header - with visible title"""
        header = QWidget()
        header.setFixedHeight(70)
        header.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0a0e27, stop:1 #131838);
                border-bottom: 2px solid #64ffda;
                border-radius: 5px;
            }
        """)
        
        layout = QHBoxLayout(header)
        layout.setContentsMargins(15, 5, 15, 5)

        # Title section with icon and text
        title_widget = QWidget()
        title_layout = QVBoxLayout(title_widget)
        title_layout.setSpacing(2)
        
        # Main title with emoji and text
        main_title = QLabel("CRYPTO MACHINE")
        main_title.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: #64ffda;
            font-family: 'Segoe UI', 'Consolas', monospace;
            letter-spacing: 1px;
        """)
        
        # Subtitle
        sub_title = QLabel("Advanced Encryption | Cryptographic Hashing | Encoding Suite")
        sub_title.setStyleSheet("""
            font-size: 11px;
            color: #8892b0;
            font-family: 'Segoe UI', monospace;
        """)
        
        title_layout.addWidget(main_title)
        title_layout.addWidget(sub_title)
        
        # Version badge
        version_badge = QLabel("v2.0.0")
        version_badge.setStyleSheet("""
            background-color: #64ffda;
            color: #0a0e27;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: bold;
        """)
        version_badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(title_widget)
        layout.addStretch()
        layout.addWidget(version_badge)
        
        return header

    def create_symmetric_tab(self):
        """Create symmetric encryption tab - compact version"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(5)
        layout.setContentsMargins(5, 5, 5, 5)

        # Algorithm selection - compact
        algo_group = QGroupBox("Algorithm")
        algo_layout = QHBoxLayout()
        self.sym_algo = AlgorithmSelector(["AES-256", "DES", "3DES"])
        algo_layout.addWidget(QLabel("Select:"))
        algo_layout.addWidget(self.sym_algo)
        algo_layout.addStretch()
        algo_group.setLayout(algo_layout)

        # Input - compact height
        input_group = QGroupBox("Input")
        input_layout = QVBoxLayout()
        self.sym_input = StyledTextArea("Enter text to encrypt/decrypt...")
        self.sym_input.setMaximumHeight(100)
        input_layout.addWidget(self.sym_input)
        input_group.setLayout(input_layout)

        # Key with random button
        key_group = QGroupBox("Secret Key")
        key_layout = QHBoxLayout()
        self.sym_key = KeyInput("Enter encryption key...")
        self.random_key_btn = ModernButton("🎲 Random", is_success=True)
        self.random_key_btn.setMaximumWidth(100)
        self.random_key_btn.clicked.connect(self.generate_random_key)
        key_layout.addWidget(self.sym_key)
        key_layout.addWidget(self.random_key_btn)
        key_group.setLayout(key_layout)

        # Action buttons - compact
        action_layout = QHBoxLayout()
        self.encrypt_btn = ModernButton("🔒 Encrypt", is_success=True)
        self.decrypt_btn = ModernButton("🔓 Decrypt")
        self.clear_btn = ModernButton("🗑️ Clear", is_danger=True)
        self.encrypt_btn.clicked.connect(self.symmetric_encrypt)
        self.decrypt_btn.clicked.connect(self.symmetric_decrypt)
        self.clear_btn.clicked.connect(self.clear_symmetric)
        action_layout.addWidget(self.encrypt_btn)
        action_layout.addWidget(self.decrypt_btn)
        action_layout.addWidget(self.clear_btn)
        action_layout.addStretch()

        # Output - compact
        output_group = QGroupBox("Output")
        output_layout = QVBoxLayout()
        self.sym_output = StyledTextArea("Result will appear here...")
        self.sym_output.setMaximumHeight(100)
        output_actions = QHBoxLayout()
        self.copy_output_btn = ModernButton("📋 Copy")
        self.save_output_btn = ModernButton("💾 Save")
        self.copy_output_btn.clicked.connect(lambda: self.copy_to_clipboard(self.sym_output))
        self.save_output_btn.clicked.connect(lambda: self.save_to_file(self.sym_output))
        output_actions.addWidget(self.copy_output_btn)
        output_actions.addWidget(self.save_output_btn)
        output_actions.addStretch()
        output_layout.addWidget(self.sym_output)
        output_layout.addLayout(output_actions)
        output_group.setLayout(output_layout)

        layout.addWidget(algo_group)
        layout.addWidget(input_group)
        layout.addWidget(key_group)
        layout.addLayout(action_layout)
        layout.addWidget(output_group)

        return tab

    def create_rsa_tab(self):
        """Create RSA encryption tab - compact version"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(5)
        layout.setContentsMargins(5, 5, 5, 5)

        # Key generation
        key_gen_group = QGroupBox("RSA Key Generation")
        key_gen_layout = QHBoxLayout()
        self.generate_rsa_btn = ModernButton("🔑 Generate Keys", is_success=True)
        self.generate_rsa_btn.clicked.connect(self.generate_rsa_keys)
        key_gen_layout.addWidget(self.generate_rsa_btn)
        key_gen_layout.addStretch()
        key_gen_group.setLayout(key_gen_layout)

        # Public Key - compact
        pub_key_group = QGroupBox("Public Key")
        pub_key_layout = QVBoxLayout()
        self.public_key_display = StyledTextArea("Click 'Generate Keys' to create...")
        self.public_key_display.setMaximumHeight(80)
        pub_actions = QHBoxLayout()
        self.copy_pub_btn = ModernButton("📋 Copy")
        self.save_pub_btn = ModernButton("💾 Save")
        self.copy_pub_btn.clicked.connect(lambda: self.copy_to_clipboard(self.public_key_display))
        self.save_pub_btn.clicked.connect(lambda: self.save_text_to_file("public_key.pem", self.public_key_display.get_text()))
        pub_actions.addWidget(self.copy_pub_btn)
        pub_actions.addWidget(self.save_pub_btn)
        pub_actions.addStretch()
        pub_key_layout.addWidget(self.public_key_display)
        pub_key_layout.addLayout(pub_actions)
        pub_key_group.setLayout(pub_key_layout)

        # Private Key - compact
        priv_key_group = QGroupBox("Private Key (KEEP SECRET!)")
        priv_key_layout = QVBoxLayout()
        self.private_key_display = StyledTextArea("Click 'Generate Keys' to create...")
        self.private_key_display.setMaximumHeight(80)
        priv_actions = QHBoxLayout()
        self.copy_priv_btn = ModernButton("📋 Copy")
        self.save_priv_btn = ModernButton("💾 Save")
        self.copy_priv_btn.clicked.connect(lambda: self.copy_to_clipboard(self.private_key_display))
        self.save_priv_btn.clicked.connect(lambda: self.save_text_to_file("private_key.pem", self.private_key_display.get_text()))
        priv_actions.addWidget(self.copy_priv_btn)
        priv_actions.addWidget(self.save_priv_btn)
        priv_actions.addStretch()
        priv_key_layout.addWidget(self.private_key_display)
        priv_key_layout.addLayout(priv_actions)
        priv_key_group.setLayout(priv_key_layout)

        # Encryption section - side by side layout for compactness
        crypto_layout = QHBoxLayout()
        
        # Encrypt
        enc_group = QGroupBox("Encrypt")
        enc_layout = QVBoxLayout()
        self.rsa_input = StyledTextArea("Enter text...")
        self.rsa_input.setMaximumHeight(80)
        self.rsa_encrypt_btn = ModernButton("🔒 Encrypt", is_success=True)
        self.rsa_encrypt_btn.clicked.connect(self.rsa_encrypt)
        enc_layout.addWidget(self.rsa_input)
        enc_layout.addWidget(self.rsa_encrypt_btn)
        enc_group.setLayout(enc_layout)
        
        # Decrypt
        dec_group = QGroupBox("Decrypt")
        dec_layout = QVBoxLayout()
        self.rsa_decrypt_input = StyledTextArea("Enter encrypted text...")
        self.rsa_decrypt_input.setMaximumHeight(80)
        self.rsa_decrypt_btn = ModernButton("🔓 Decrypt")
        self.rsa_decrypt_btn.clicked.connect(self.rsa_decrypt)
        dec_layout.addWidget(self.rsa_decrypt_input)
        dec_layout.addWidget(self.rsa_decrypt_btn)
        dec_group.setLayout(dec_layout)
        
        crypto_layout.addWidget(enc_group)
        crypto_layout.addWidget(dec_group)

        # Output
        output_group = QGroupBox("Output")
        output_layout = QVBoxLayout()
        self.rsa_output = StyledTextArea("Result will appear here...")
        self.rsa_output.setMaximumHeight(80)
        output_actions = QHBoxLayout()
        self.copy_rsa_output_btn = ModernButton("📋 Copy")
        self.save_rsa_output_btn = ModernButton("💾 Save")
        self.copy_rsa_output_btn.clicked.connect(lambda: self.copy_to_clipboard(self.rsa_output))
        self.save_rsa_output_btn.clicked.connect(lambda: self.save_to_file(self.rsa_output))
        output_actions.addWidget(self.copy_rsa_output_btn)
        output_actions.addWidget(self.save_rsa_output_btn)
        output_actions.addStretch()
        output_layout.addWidget(self.rsa_output)
        output_layout.addLayout(output_actions)
        output_group.setLayout(output_layout)

        layout.addWidget(key_gen_group)
        layout.addWidget(pub_key_group)
        layout.addWidget(priv_key_group)
        layout.addLayout(crypto_layout)
        layout.addWidget(output_group)

        return tab

    def create_encoding_tab(self):
        """Create encoding/decoding tab - compact version"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(5)
        layout.setContentsMargins(5, 5, 5, 5)

        # Algorithm selection
        algo_group = QGroupBox("Algorithm")
        algo_layout = QHBoxLayout()
        self.encoding_algo = AlgorithmSelector(["Base64", "Hex", "URL"])
        algo_layout.addWidget(QLabel("Select:"))
        algo_layout.addWidget(self.encoding_algo)
        algo_layout.addStretch()
        algo_group.setLayout(algo_layout)

        # Input - compact
        input_group = QGroupBox("Input Text")
        input_layout = QVBoxLayout()
        self.encode_input = StyledTextArea("Enter text to encode/decode...")
        self.encode_input.setMaximumHeight(100)
        input_layout.addWidget(self.encode_input)
        input_group.setLayout(input_layout)

        # Action buttons
        action_layout = QHBoxLayout()
        self.encode_btn = ModernButton("📤 Encode", is_success=True)
        self.decode_btn = ModernButton("📥 Decode")
        self.clear_encode_btn = ModernButton("🗑️ Clear", is_danger=True)
        self.encode_btn.clicked.connect(self.encode_text)
        self.decode_btn.clicked.connect(self.decode_text)
        self.clear_encode_btn.clicked.connect(self.clear_encoding)
        action_layout.addWidget(self.encode_btn)
        action_layout.addWidget(self.decode_btn)
        action_layout.addWidget(self.clear_encode_btn)
        action_layout.addStretch()

        # Output - compact
        output_group = QGroupBox("Output")
        output_layout = QVBoxLayout()
        self.encode_output = StyledTextArea("Result will appear here...")
        self.encode_output.setMaximumHeight(100)
        output_actions = QHBoxLayout()
        self.copy_encode_btn = ModernButton("📋 Copy")
        self.save_encode_btn = ModernButton("💾 Save")
        self.copy_encode_btn.clicked.connect(lambda: self.copy_to_clipboard(self.encode_output))
        self.save_encode_btn.clicked.connect(lambda: self.save_to_file(self.encode_output))
        output_actions.addWidget(self.copy_encode_btn)
        output_actions.addWidget(self.save_encode_btn)
        output_actions.addStretch()
        output_layout.addWidget(self.encode_output)
        output_layout.addLayout(output_actions)
        output_group.setLayout(output_layout)

        layout.addWidget(algo_group)
        layout.addWidget(input_group)
        layout.addLayout(action_layout)
        layout.addWidget(output_group)

        return tab

    def create_hashing_tab(self):
        """Create hashing tab - compact version"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(5)
        layout.setContentsMargins(5, 5, 5, 5)

        # Info label - smaller
        info_label = QLabel("ℹ️ Hashing is one-way and cannot be decrypted.")
        info_label.setStyleSheet("color: #ffa500; padding: 5px; background-color: #1a1f3a; border-radius: 5px; font-size: 11px;")
        info_label.setWordWrap(True)
        layout.addWidget(info_label)

        # Algorithm selection
        algo_group = QGroupBox("Hash Algorithm")
        algo_layout = QHBoxLayout()
        self.hash_algo = AlgorithmSelector(["SHA-256", "MD5"])
        algo_layout.addWidget(QLabel("Select:"))
        algo_layout.addWidget(self.hash_algo)
        algo_layout.addStretch()
        algo_group.setLayout(algo_layout)

        # Input - compact
        input_group = QGroupBox("Input Text")
        input_layout = QVBoxLayout()
        self.hash_input = StyledTextArea("Enter text to hash...")
        self.hash_input.setMaximumHeight(100)
        input_layout.addWidget(self.hash_input)
        input_group.setLayout(input_layout)

        # Generate button
        self.generate_hash_btn = ModernButton("🔐 Generate Hash", is_success=True)
        self.generate_hash_btn.clicked.connect(self.generate_hash)

        # Output - compact
        output_group = QGroupBox("Hash Output")
        output_layout = QVBoxLayout()
        self.hash_output = StyledTextArea("Hash will appear here...")
        self.hash_output.setReadOnly(True)
        self.hash_output.setMaximumHeight(80)
        output_actions = QHBoxLayout()
        self.copy_hash_btn = ModernButton("📋 Copy")
        self.save_hash_btn = ModernButton("💾 Save")
        self.clear_hash_btn = ModernButton("🗑️ Clear", is_danger=True)
        self.copy_hash_btn.clicked.connect(lambda: self.copy_to_clipboard(self.hash_output))
        self.save_hash_btn.clicked.connect(lambda: self.save_to_file(self.hash_output))
        self.clear_hash_btn.clicked.connect(self.clear_hashing)
        output_actions.addWidget(self.copy_hash_btn)
        output_actions.addWidget(self.save_hash_btn)
        output_actions.addWidget(self.clear_hash_btn)
        output_actions.addStretch()
        output_layout.addWidget(self.hash_output)
        output_layout.addLayout(output_actions)
        output_group.setLayout(output_layout)

        layout.addWidget(algo_group)
        layout.addWidget(input_group)
        layout.addWidget(self.generate_hash_btn)
        layout.addWidget(output_group)

        return tab

    # ========== SYMMETRIC ENCRYPTION METHODS ==========

    def generate_random_key(self):
        algo = self.sym_algo.currentText()
        if algo == "AES-256":
            key = self.aes_cipher.generate_key()
        elif algo == "DES":
            key = self.des_cipher.generate_key()
        else:
            key = self.triple_des_cipher.generate_key()
        if isinstance(key, bytes):
            key = key.hex()
        self.sym_key.setText(key)
        self.status_bar.showMessage(f"✓ Generated random {algo} key", 3000)

    def symmetric_encrypt(self):
        text = self.sym_input.get_text()
        key = self.sym_key.text()
        algo = self.sym_algo.currentText()
        if not text or not key:
            QMessageBox.warning(self, "Error", "Please enter both text and key!")
            return
        try:
            if algo == "AES-256":
                result = self.aes_cipher.encrypt(text, key)
            elif algo == "DES":
                result = self.des_cipher.encrypt(text, key)
            else:
                result = self.triple_des_cipher.encrypt(text, key)
            self.sym_output.set_text(result)
            self.status_bar.showMessage(f"✓ Encrypted successfully with {algo}", 3000)
        except Exception as e:
            QMessageBox.critical(self, "Encryption Error", f"Failed to encrypt:\n{str(e)}")

    def symmetric_decrypt(self):
        text = self.sym_input.get_text()
        key = self.sym_key.text()
        algo = self.sym_algo.currentText()
        if not text or not key:
            QMessageBox.warning(self, "Error", "Please enter both text and key!")
            return
        try:
            if algo == "AES-256":
                result = self.aes_cipher.decrypt(text, key)
            elif algo == "DES":
                result = self.des_cipher.decrypt(text, key)
            else:
                result = self.triple_des_cipher.decrypt(text, key)
            self.sym_output.set_text(result)
            self.status_bar.showMessage(f"✓ Decrypted successfully with {algo}", 3000)
        except Exception as e:
            QMessageBox.critical(self, "Decryption Error", f"Failed to decrypt:\n{str(e)}")

    def clear_symmetric(self):
        self.sym_input.clear_text()
        self.sym_key.clear()
        self.sym_output.clear_text()
        self.status_bar.showMessage("Cleared all fields", 2000)

    # ========== RSA METHODS ==========

    def generate_rsa_keys(self):
        try:
            public_key, private_key = self.rsa_cipher.generate_keys()
            self.public_key_display.set_text(public_key)
            self.private_key_display.set_text(private_key)
            self.status_bar.showMessage("✓ RSA keys generated successfully!", 3000)
            QMessageBox.information(self, "Success", "RSA keys generated successfully!\n\nRemember to keep your private key secure!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate RSA keys:\n{str(e)}")

    def rsa_encrypt(self):
        text = self.rsa_input.get_text()
        public_key_pem = self.public_key_display.get_text()
        if not text or not public_key_pem:
            QMessageBox.warning(self, "Error", "Please enter text and generate/load public key!")
            return
        try:
            encrypted = self.rsa_cipher.encrypt(text, public_key_pem)
            self.rsa_output.set_text(encrypted)
            self.status_bar.showMessage("✓ RSA encrypted successfully!", 3000)
        except Exception as e:
            QMessageBox.critical(self, "Encryption Error", f"Failed to encrypt:\n{str(e)}")

    def rsa_decrypt(self):
        encrypted_text = self.rsa_decrypt_input.get_text()
        private_key_pem = self.private_key_display.get_text()
        if not encrypted_text or not private_key_pem:
            QMessageBox.warning(self, "Error", "Please enter encrypted text and generate/load private key!")
            return
        try:
            decrypted = self.rsa_cipher.decrypt(encrypted_text, private_key_pem)
            self.rsa_output.set_text(decrypted)
            self.status_bar.showMessage("✓ RSA decrypted successfully!", 3000)
        except Exception as e:
            QMessageBox.critical(self, "Decryption Error", f"Failed to decrypt:\n{str(e)}")

    # ========== ENCODING METHODS ==========

    def encode_text(self):
        text = self.encode_input.get_text()
        algo = self.encoding_algo.currentText()
        if not text:
            QMessageBox.warning(self, "Error", "Please enter text to encode!")
            return
        try:
            if algo == "Base64":
                result = self.encoding_tools.base64_encode(text)
            elif algo == "Hex":
                result = self.encoding_tools.hex_encode(text)
            else:
                result = self.encoding_tools.url_encode(text)
            self.encode_output.set_text(result)
            self.status_bar.showMessage(f"✓ Encoded with {algo}", 3000)
        except Exception as e:
            QMessageBox.critical(self, "Encoding Error", f"Failed to encode:\n{str(e)}")

    def decode_text(self):
        text = self.encode_input.get_text()
        algo = self.encoding_algo.currentText()
        if not text:
            QMessageBox.warning(self, "Error", "Please enter text to decode!")
            return
        try:
            if algo == "Base64":
                result = self.encoding_tools.base64_decode(text)
            elif algo == "Hex":
                result = self.encoding_tools.hex_decode(text)
            else:
                result = self.encoding_tools.url_decode(text)
            self.encode_output.set_text(result)
            self.status_bar.showMessage(f"✓ Decoded with {algo}", 3000)
        except Exception as e:
            QMessageBox.critical(self, "Decoding Error", f"Failed to decode:\n{str(e)}")

    def clear_encoding(self):
        self.encode_input.clear_text()
        self.encode_output.clear_text()
        self.status_bar.showMessage("Cleared all encoding fields", 2000)

    # ========== HASHING METHODS ==========

    def generate_hash(self):
        text = self.hash_input.get_text()
        algo = self.hash_algo.currentText()
        if not text:
            QMessageBox.warning(self, "Error", "Please enter text to hash!")
            return
        if algo == "SHA-256":
            result = self.hash_tools.sha256_hash(text)
        else:
            result = self.hash_tools.md5_hash(text)
        self.hash_output.set_text(result)
        self.status_bar.showMessage(f"✓ Generated {algo} hash", 3000)

    def clear_hashing(self):
        self.hash_input.clear_text()
        self.hash_output.clear_text()
        self.status_bar.showMessage("Cleared all hashing fields", 2000)

    # ========== UTILITY METHODS ==========

    def copy_to_clipboard(self, text_widget):
        """Copy text widget content to clipboard"""
        text = text_widget.get_text()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            self.status_bar.showMessage("✓ Copied to clipboard!", 2000)
            QMessageBox.information(self, "Success", "Text copied to clipboard!")
        else:
            QMessageBox.warning(self, "Error", "Nothing to copy!")

    def save_to_file(self, text_widget):
        text = text_widget.get_text()
        if not text:
            QMessageBox.warning(self, "Error", "Nothing to save!")
            return
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                self.status_bar.showMessage(f"✓ Saved to {file_path}", 3000)
                QMessageBox.information(self, "Success", f"File saved successfully!\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file:\n{str(e)}")

    def save_text_to_file(self, filename, text):
        if not text:
            QMessageBox.warning(self, "Error", "Nothing to save!")
            return
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", filename, "PEM Files (*.pem);;Text Files (*.txt)")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                self.status_bar.showMessage(f"✓ Saved to {file_path}", 3000)
                QMessageBox.information(self, "Success", f"File saved successfully!\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file:\n{str(e)}")