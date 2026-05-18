"""
UI package for Crypto Toolkit Pro
Contains all user interface components and styling
"""

from ui.main_window import MainWindow
from ui.styles import MAIN_STYLE, apply_styles
from ui.widgets import (
    StyledTextArea,
    ModernButton,
    CopyButton,
    InfoLabel,
    AlgorithmSelector,
    KeyInput
)

__all__ = [
    'MainWindow',
    'MAIN_STYLE',
    'apply_styles',
    'StyledTextArea',
    'ModernButton',
    'CopyButton',
    'InfoLabel',
    'AlgorithmSelector',
    'KeyInput'
]