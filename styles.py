import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class ProfessionalStyles:
    def __init__(self):
        self.colors = self._setup_colors()
        self.fonts = self._setup_fonts()
        self.setup_styles()
    
    def _setup_colors(self):
        """Define modern color palette"""
        return {
            # Primary Colors
            'primary': '#2c3e50',
            'primary_light': '#34495e',
            'primary_dark': '#1a252f',
            
            # Accent Colors
            'accent': '#3498db',
            'accent_light': '#5dade2',
            'accent_dark': '#2980b9',
            
            # Success Colors
            'success': '#27ae60',
            'success_light': '#58d68d',
            'success_dark': '#229954',
            
            # Warning Colors
            'warning': '#f39c12',
            'warning_light': '#f8c471',
            'warning_dark': '#e67e22',
            
            # Danger Colors
            'danger': '#e74c3c',
            'danger_light': '#ec7063',
            'danger_dark': '#c0392b',
            
            # Neutral Colors
            'light': '#ecf0f1',
            'light_gray': '#bdc3c7',
            'gray': '#95a5a6',
            'dark_gray': '#7f8c8d',
            'dark': '#2c3e50',
            
            # Background Colors
            'bg_primary': '#2c3e50',
            'bg_secondary': '#34495e',
            'bg_light': '#ecf0f1',
            'bg_white': '#ffffff',
            
            # Text Colors
            'text_primary': '#2c3e50',
            'text_secondary': '#7f8c8d',
            'text_light': '#ecf0f1',
            'text_white': '#ffffff'
        }
    
    def _setup_fonts(self):
        """Define font families and sizes"""
        return {
            'h1': ('Arial', 24, 'bold'),
            'h2': ('Arial', 20, 'bold'),
            'h3': ('Arial', 16, 'bold'),
            'h4': ('Arial', 14, 'bold'),
            'body_large': ('Arial', 12),
            'body': ('Arial', 10),
            'body_small': ('Arial', 9),
            'button_large': ('Arial', 12, 'bold'),
            'button': ('Arial', 10, 'bold'),
            'caption': ('Arial', 8)
        }
    
    def setup_styles(self):
        """Configure all tkinter and ttk styles"""
        self._setup_ttk_styles()
        self._setup_custom_widgets()
    
    def _setup_ttk_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure Treeview
        style.configure('Modern.Treeview',
            background=self.colors['bg_white'],
            foreground=self.colors['text_primary'],
            rowheight=28,
            fieldbackground=self.colors['bg_white'],
            borderwidth=1,
            relief='flat',
            font=self.fonts['body']
        )
        
        style.configure('Modern.Treeview.Heading',
            background=self.colors['primary'],
            foreground=self.colors['text_light'],
            relief='flat',
            borderwidth=0,
            font=self.fonts['body']
        )
        
        style.map('Modern.Treeview.Heading',
            background=[('active', self.colors['accent'])]
        )
        
        # Configure Buttons
        self._setup_button_styles(style)
        
        # Configure Entries
        self._setup_entry_styles(style)
        
        # Configure Combobox
        self._setup_combobox_styles(style)
        
        # Configure Scrollbars
        self._setup_scrollbar_styles(style)
        
        # Configure Progressbar
        self._setup_progressbar_styles(style)
    
    def _setup_button_styles(self, style):
        """Configure button styles"""
        # Primary Button
        style.configure('Primary.TButton',
            background=self.colors['accent'],
            foreground=self.colors['text_white'],
            borderwidth=0,
            focuscolor='none',
            font=self.fonts['button'],
            padding=(20, 10)
        )
        style.map('Primary.TButton',
            background=[('active', self.colors['accent_dark']),
                       ('pressed', self.colors['accent_dark'])]
        )
        
        # Secondary Button
        style.configure('Secondary.TButton',
            background=self.colors['light_gray'],
            foreground=self.colors['text_primary'],
            borderwidth=0,
            focuscolor='none',
            font=self.fonts['button'],
            padding=(20, 10)
        )
        
        # Success Button
        style.configure('Success.TButton',
            background=self.colors['success'],
            foreground=self.colors['text_white'],
            borderwidth=0,
            focuscolor='none',
            font=self.fonts['button'],
            padding=(20, 10)
        )
        
        # Danger Button
        style.configure('Danger.TButton',
            background=self.colors['danger'],
            foreground=self.colors['text_white'],
            borderwidth=0,
            focuscolor='none',
            font=self.fonts['button'],
            padding=(20, 10)
        )
        
        # Warning Button
        style.configure('Warning.TButton',
            background=self.colors['warning'],
            foreground=self.colors['text_white'],
            borderwidth=0,
            focuscolor='none',
            font=self.fonts['button'],
            padding=(20, 10)
        )
    
    def _setup_entry_styles(self, style):
        """Configure entry styles"""
        style.configure('Modern.TEntry',
            fieldbackground=self.colors['bg_white'],
            foreground=self.colors['text_primary'],
            borderwidth=1,
            relief='flat',
            padding=(10, 5),
            font=self.fonts['body']
        )
        
        style.map('Modern.TEntry',
            fieldbackground=[('focus', self.colors['bg_white']),
                           ('active', self.colors['bg_white'])],
            bordercolor=[('focus', self.colors['accent'])]
        )
    
    def _setup_combobox_styles(self, style):
        """Configure combobox styles"""
        style.configure('Modern.TCombobox',
            fieldbackground=self.colors['bg_white'],
            foreground=self.colors['text_primary'],
            background=self.colors['bg_white'],
            borderwidth=1,
            relief='flat',
            padding=(10, 5),
            font=self.fonts['body']
        )
        
        style.map('Modern.TCombobox',
            fieldbackground=[('focus', self.colors['bg_white']),
                           ('readonly', self.colors['bg_white'])],
            background=[('readonly', self.colors['bg_white'])]
        )
    
    def _setup_scrollbar_styles(self, style):
        """Configure scrollbar styles"""
        style.configure('Modern.Vertical.TScrollbar',
            background=self.colors['light_gray'],
            darkcolor=self.colors['light_gray'],
            lightcolor=self.colors['light_gray'],
            troughcolor=self.colors['light'],
            bordercolor=self.colors['light_gray'],
            arrowcolor=self.colors['dark_gray'],
            relief='flat',
            borderwidth=0
        )
        
        style.map('Modern.Vertical.TScrollbar',
            background=[('active', self.colors['gray'])]
        )
    
    def _setup_progressbar_styles(self, style):
        """Configure progressbar styles"""
        style.configure('Modern.Horizontal.TProgressbar',
            background=self.colors['accent'],
            troughcolor=self.colors['light'],
            borderwidth=0,
            lightcolor=self.colors['accent'],
            darkcolor=self.colors['accent']
        )
    
    def _setup_custom_widgets(self):
        """Setup custom widget styles"""
        # These will be used by our custom widgets
        pass

class GlassFrame(tk.Frame):
    """Glass morphism effect frame - إصدار مبسط"""
    def __init__(self, master, **kwargs):
        # إزالة blur_amount واستخدام لون ثابت
        bg_color = kwargs.pop('bg', '#34495e')  # استخدام لون ثابت بدل الشفافية
        super().__init__(master, bg=bg_color, **kwargs)
        
        # إزالة البوردر إذا كان يسبب مشاكل
        # self.border = tk.Frame(self, bg='#ffffff40', height=1)
        # self.border.pack(fill='x', side='bottom')

class ModernCard(tk.Frame):
    """Modern card widget with shadow and hover effects"""
    def __init__(self, master, **kwargs):
        self.bg_color = kwargs.pop('bg', '#ffffff')
        self.hover_color = kwargs.pop('hover_color', '#f8f9fa')
        self.shadow_color = kwargs.pop('shadow_color', '#bdc3c7')
        self.elevation = kwargs.pop('elevation', 2)
        self.corner_radius = kwargs.pop('corner_radius', 8)
        
        super().__init__(master, bg=self.bg_color, **kwargs)
        
        # Create shadow effect
        self.shadow = tk.Frame(master, bg=self.shadow_color)
        self.configure(
            relief='flat',
            borderwidth=0,
            highlightthickness=0
        )
        
        self._setup_appearance()
    
    def _setup_appearance(self):
        """Setup card appearance"""
        # Bind hover events
        self.bind('<Enter>', self._on_hover)
        self.bind('<Leave>', self._on_leave)
        
        # Bind to all children
        self._bind_to_children(self)
    
    def _bind_to_children(self, widget):
        """Bind events to all child widgets"""
        for child in widget.winfo_children():
            child.bind('<Enter>', self._on_hover)
            child.bind('<Leave>', self._on_leave)
            self._bind_to_children(child)
    
    def _on_hover(self, event):
        """Handle hover effect"""
        self.config(bg=self.hover_color)
        # Lift card on hover
        self.shadow.lift()
    
    def _on_leave(self, event):
        """Handle leave effect"""
        self.config(bg=self.bg_color)
    
    def pack(self, **kwargs):
        self.shadow.pack(**kwargs, padx=self.elevation, pady=self.elevation)
        super().pack(in_=self.shadow, fill='both', expand=True)
    
    def grid(self, **kwargs):
        self.shadow.grid(**kwargs, padx=self.elevation, pady=self.elevation)
        super().grid(in_=self.shadow, sticky='nsew')
    
    def place(self, **kwargs):
        self.shadow.place(**kwargs)
        super().place(in_=self.shadow, x=0, y=0, relwidth=1, relheight=1)

class GlassFrame(tk.Frame):
    """Glass morphism effect frame"""
    def __init__(self, master, blur_amount=10, **kwargs):
        super().__init__(master, **kwargs)
        self.blur_amount = blur_amount
        self.config(
            bg='#ffffff20',  # Semi-transparent white
            relief='flat',
            borderwidth=0
        )
        
        # Add border
        self.border = tk.Frame(self, bg='#ffffff40', height=1)
        self.border.pack(fill='x', side='bottom')

# Global styles instance
styles = ProfessionalStyles()