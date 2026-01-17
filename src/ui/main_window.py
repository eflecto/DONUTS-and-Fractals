"""Main application window with donut-themed interface"""

from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QScrollArea, QGridLayout,
                             QStackedWidget, QFrame)
from PyQt6.QtCore import Qt, QSize, pyqtSignal, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush, QFont, QLinearGradient

from src.ui.donut_button import DonutButton
from src.ui.fractal_viewer import FractalViewer
from src.fractals.fractal_registry import FractalRegistry


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.current_fractal = None
        
        self.init_ui()
        self.setup_fractals()
        
    def init_ui(self):
        """Initialize user interface"""
        # Window setup
        window_config = self.config.get('window', {})
        self.setWindowTitle("🍩 DONUTS-and-Fractals")
        self.setGeometry(100, 100, 
                        window_config.get('width', 1280),
                        window_config.get('height', 720))
        
        # Set donut color scheme
        self.setStyleSheet(self.get_donut_stylesheet())
        
        # Create central widget with stacked layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create stacked widget for menu/viewer switching
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)
        
        # Create menu page
        self.menu_page = self.create_menu_page()
        self.stacked_widget.addWidget(self.menu_page)
        
        # Create viewer page
        self.viewer_page = QWidget()
        viewer_layout = QVBoxLayout(self.viewer_page)
        viewer_layout.setContentsMargins(0, 0, 0, 0)
        
        # Back button
        back_button = QPushButton("⬅ Back to Menu")
        back_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #FFB6C1, stop:1 #FFA07A);
                color: white;
                border: none;
                border-radius: 20px;
                padding: 10px 30px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #FF69B4, stop:1 #FF7F50);
            }
        """)
        back_button.clicked.connect(self.show_menu)
        viewer_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)
        
        # Fractal viewer
        self.fractal_viewer = FractalViewer(self.config)
        viewer_layout.addWidget(self.fractal_viewer, stretch=1)
        
        self.stacked_widget.addWidget(self.viewer_page)
        
        # Show menu by default
        self.stacked_widget.setCurrentWidget(self.menu_page)
        
    def create_menu_page(self):
        """Create the main menu page with donut buttons"""
        menu_widget = QWidget()
        layout = QVBoxLayout(menu_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("🍩 DONUTS-and-Fractals 🍩")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 48px;
                font-weight: bold;
                color: #FF69B4;
                padding: 20px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(255,182,193,50), stop:1 rgba(255,160,122,50));
                border-radius: 30px;
            }
        """)
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Select your favorite fractal donut!")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("font-size: 20px; color: #FF7F50; padding: 10px;")
        layout.addWidget(subtitle)
        
        # Scroll area for donuts
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        # Container for donut grid
        container = QWidget()
        self.donut_grid = QGridLayout(container)
        self.donut_grid.setSpacing(25)
        self.donut_grid.setContentsMargins(20, 20, 20, 20)
        
        scroll.setWidget(container)
        layout.addWidget(scroll, stretch=1)
        
        # Footer
        footer = QLabel("Made with ❤️ and 🍩 by eflecto")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setStyleSheet("font-size: 14px; color: #FFB6C1; padding: 10px;")
        layout.addWidget(footer)
        
        return menu_widget
    
    def setup_fractals(self):
        """Setup fractal donut buttons"""
        fractals = FractalRegistry.get_all_fractals()
        
        # Colors for donuts
        donut_colors = [
            ("#FFB6C1", "#FF69B4"),  # Pink
            ("#FFA07A", "#FF7F50"),  # Coral
            ("#FFD700", "#FFA500"),  # Gold
            ("#98FB98", "#00FA9A"),  # Mint
            ("#87CEEB", "#4682B4"),  # Sky
            ("#DDA0DD", "#BA55D3"),  # Plum
        ]
        
        row, col = 0, 0
        max_cols = 4
        
        for i, (name, fractal_info) in enumerate(fractals.items()):
            color1, color2 = donut_colors[i % len(donut_colors)]
            
            donut = DonutButton(name, fractal_info, color1, color2)
            donut.clicked.connect(lambda checked, f=fractal_info: self.show_fractal(f))
            
            self.donut_grid.addWidget(donut, row, col)
            
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
    
    def show_fractal(self, fractal_info):
        """Show selected fractal in viewer"""
        self.current_fractal = fractal_info
        self.fractal_viewer.load_fractal(fractal_info)
        self.stacked_widget.setCurrentWidget(self.viewer_page)
    
    def show_menu(self):
        """Return to main menu"""
        self.stacked_widget.setCurrentWidget(self.menu_page)
        self.fractal_viewer.stop_rendering()
    
    def get_donut_stylesheet(self):
        """Get application-wide donut-themed stylesheet"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #FFF5EE, stop:1 #FFE4E1);
            }
            QWidget {
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QScrollBar:vertical {
                background: #FFE4E1;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #FFB6C1;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical:hover {
                background: #FF69B4;
            }
        """
    
    def keyPressEvent(self, event):
        """Handle keyboard shortcuts"""
        if event.key() == Qt.Key.Key_Escape:
            if self.stacked_widget.currentWidget() == self.viewer_page:
                self.show_menu()
            else:
                self.close()
        elif event.key() == Qt.Key.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()
        super().keyPressEvent(event)
