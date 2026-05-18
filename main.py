#!/usr/bin/env python3
"""
Crypto Toolkit Pro - Main Entry Point
A professional cybersecurity toolkit for encryption, hashing, and encoding
"""

import sys
import os

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from ui.main_window import MainWindow

def main():
    """Main application entry point"""
    # Enable high DPI scaling for better appearance
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    # Create the application
    app = QApplication(sys.argv)
    app.setApplicationName("Crypto Toolkit Pro")
    app.setOrganizationName("CryptoSuite")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()