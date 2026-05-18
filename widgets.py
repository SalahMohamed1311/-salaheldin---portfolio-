"""
Custom widgets for Crypto Toolkit Pro
Beautiful, reusable UI components
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QTextEdit, QComboBox, QLineEdit,
                             QGroupBox, QMessageBox)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QClipboard

class StyledTextArea(QTextEdit):
    """Custom styled text area with copy functionality"""
    
    def __init__(self, placeholder="Enter text here..."):
        super().__init__()
        self.setPlaceholderText(placeholder)
        self.setMaximumHeight(150)
        
    def get_text(self):
        """Get text content"""
        return self.toPlainText()
    
    def set_text(self, text):
        """Set text content"""
        self.setText(text)
    
    def clear_text(self):
        """Clear text content"""
        self.clear()

class ModernButton(QPushButton):
    """Modern styled button with hover animations"""
    
    def __init__(self, text, icon_text="", is_danger=False, is_success=False):
        super().__init__(text)
        
        if icon_text:
            self.setText(f"{icon_text} {text}")
        
        if is_danger:
            self.setObjectName("dangerButton")
        elif is_success:
            self.setObjectName("successButton")
        
        self.setMinimumHeight(35)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

class CopyButton(QPushButton):
    """Specialized button for copying to clipboard"""
    
    def __init__(self, parent_widget, source_text_area=None):
        super().__init__("📋 Copy")
        self.parent_widget = parent_widget
        self.source_text_area = source_text_area
        self.setMinimumHeight(30)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
    def copy_text(self, text):
        """Copy text to clipboard"""
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        
        # Show temporary success message
        self.setText("✓ Copied!")
        QTimer.singleShot(1500, lambda: self.setText("📋 Copy"))

class InfoLabel(QLabel):
    """Styled information label"""
    
    def __init__(self, text, is_title=False, is_subtitle=False):
        super().__init__(text)
        
        if is_title:
            self.setObjectName("titleLabel")
        elif is_subtitle:
            self.setObjectName("subtitleLabel")
        else:
            self.setStyleSheet("color: #8892b0; padding: 5px;")

class AlgorithmSelector(QComboBox):
    """Styled dropdown for algorithm selection"""
    
    def __init__(self, algorithms):
        super().__init__()
        self.addItems(algorithms)
        self.setMinimumHeight(35)

class KeyInput(QLineEdit):
    """Styled input for encryption keys"""
    
    def __init__(self, placeholder="Enter secret key..."):
        super().__init__()
        self.setPlaceholderText(placeholder)
        self.setEchoMode(QLineEdit.EchoMode.Password)
        self.setMinimumHeight(35)

# Circular import fix for QApplication
from PyQt6.QtWidgets import QApplication