"""
Modern dark theme styling for Crypto Toolkit Pro
Cybersecurity dashboard aesthetic with neon accents
"""

# Main application stylesheet
MAIN_STYLE = """
/* Global Styles */
* {
    font-family: 'Segoe UI', 'Consolas', 'Monaco', monospace;
}

QMainWindow {
    background-color: #0a0e27;
}

/* Main Window */
QWidget {
    background-color: #0a0e27;
    color: #e0e0e0;
}

/* Tab Widget Styling */
QTabWidget::pane {
    border: 1px solid #1a1f3a;
    border-radius: 10px;
    background-color: #0f1433;
    margin-top: -1px;
}

QTabBar::tab {
    background-color: #131838;
    color: #8892b0;
    padding: 12px 25px;
    margin-right: 5px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: bold;
    font-size: 13px;
}

QTabBar::tab:hover {
    background-color: #1e2448;
    color: #64ffda;
}

QTabBar::tab:selected {
    background-color: #0f1433;
    color: #64ffda;
    border-bottom: 2px solid #64ffda;
}

/* Group Boxes */
QGroupBox {
    font-weight: bold;
    border: 2px solid #1a1f3a;
    border-radius: 10px;
    margin-top: 15px;
    padding-top: 10px;
    background-color: #0f1433;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    color: #64ffda;
}

/* Buttons */
QPushButton {
    background-color: #1a1f3a;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 12px;
    color: #e0e0e0;
}

QPushButton:hover {
    background-color: #64ffda;
    color: #0a0e27;
    transition: 0.3s;
}

QPushButton:pressed {
    background-color: #4a9eff;
}

QPushButton#dangerButton {
    background-color: #ff4757;
}

QPushButton#dangerButton:hover {
    background-color: #ff6b81;
}

QPushButton#successButton {
    background-color: #00d68f;
    color: #0a0e27;
}

/* Text Inputs */
QTextEdit, QLineEdit {
    background-color: #0a0e27;
    border: 2px solid #1a1f3a;
    border-radius: 8px;
    padding: 10px;
    font-family: 'Consolas', monospace;
    font-size: 12px;
    color: #64ffda;
}

QTextEdit:focus, QLineEdit:focus {
    border-color: #64ffda;
}

/* Combo Boxes */
QComboBox {
    background-color: #1a1f3a;
    border: 2px solid #1a1f3a;
    border-radius: 8px;
    padding: 8px;
    min-width: 150px;
}

QComboBox:hover {
    border-color: #64ffda;
}

QComboBox::drop-down {
    border: none;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid #64ffda;
    margin-right: 5px;
}

/* Labels */
QLabel {
    color: #8892b0;
    font-size: 12px;
}

QLabel#titleLabel {
    font-size: 24px;
    font-weight: bold;
    color: #64ffda;
    padding: 10px;
}

QLabel#subtitleLabel {
    font-size: 14px;
    color: #4a9eff;
}

/* Status Bar */
QStatusBar {
    background-color: #0f1433;
    color: #8892b0;
    border-top: 1px solid #1a1f3a;
}

/* Scroll Bars */
QScrollBar:vertical {
    background-color: #0a0e27;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #1a1f3a;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #64ffda;
}

/* Message Boxes */
QMessageBox {
    background-color: #0f1433;
}

QMessageBox QLabel {
    color: #e0e0e0;
}
"""

def apply_styles(app):
    """Apply the stylesheet to the application"""
    app.setStyleSheet(MAIN_STYLE)