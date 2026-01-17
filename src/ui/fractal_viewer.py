"""Fractal viewer widget"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap, QPainter

from src.rendering.renderer_2d import Renderer2D
from src.rendering.renderer_3d import Renderer3D


class FractalViewer(QWidget):
    """Widget for displaying and interacting with fractals"""
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.current_fractal = None
        self.renderer = None
        self.is_rendering = False
        
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Info bar
        info_layout = QHBoxLayout()
        self.info_label = QLabel("Select a fractal to begin")
        self.info_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #FF69B4;
                padding: 10px;
                background: rgba(255, 182, 193, 50);
                border-radius: 10px;
            }
        """)
        info_layout.addWidget(self.info_label)
        
        # Controls
        self.reset_btn = QPushButton("Reset View")
        self.reset_btn.setStyleSheet("""
            QPushButton {
                background: #FFB6C1;
                color: white;
                border: none;
                border-radius: 15px;
                padding: 8px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #FF69B4;
            }
        """)
        self.reset_btn.clicked.connect(self.reset_view)
        info_layout.addWidget(self.reset_btn)
        
        self.save_btn = QPushButton("💾 Save")
        self.save_btn.setStyleSheet(self.reset_btn.styleSheet())
        self.save_btn.clicked.connect(self.save_image)
        info_layout.addWidget(self.save_btn)
        
        layout.addLayout(info_layout)
        
        # Canvas for fractal display
        self.canvas = FractalCanvas(self)
        layout.addWidget(self.canvas, stretch=1)
        
        # Control panel
        controls_layout = QHBoxLayout()
        
        # Iterations slider
        controls_layout.addWidget(QLabel("Iterations:"))
        self.iterations_slider = QSlider(Qt.Orientation.Horizontal)
        self.iterations_slider.setMinimum(50)
        self.iterations_slider.setMaximum(1000)
        self.iterations_slider.setValue(256)
        self.iterations_slider.valueChanged.connect(self.on_iterations_changed)
        controls_layout.addWidget(self.iterations_slider)
        
        self.iterations_label = QLabel("256")
        controls_layout.addWidget(self.iterations_label)
        
        layout.addLayout(controls_layout)
        
    def load_fractal(self, fractal_info):
        """Load and display a fractal"""
        self.current_fractal = fractal_info
        dimension = fractal_info.get('dimension', '2D')
        name = list(fractal_info.keys())[0] if isinstance(fractal_info, dict) else "Unknown"
        
        # Update info
        self.info_label.setText(f"🍩 {name} ({dimension})")
        
        # Create appropriate renderer
        if dimension == '2D':
            self.renderer = Renderer2D(self.canvas.size(), self.config)
        else:
            self.renderer = Renderer3D(self.canvas.size(), self.config)
        
        # Start rendering
        self.is_rendering = True
        self.render_fractal()
        
    def render_fractal(self):
        """Render the current fractal"""
        if not self.renderer or not self.current_fractal:
            return
            
        image = self.renderer.render(self.current_fractal, 
                                     self.iterations_slider.value())
        if image:
            self.canvas.set_image(image)
            
    def on_iterations_changed(self, value):
        """Handle iterations slider change"""
        self.iterations_label.setText(str(value))
        if self.is_rendering:
            self.render_fractal()
            
    def reset_view(self):
        """Reset view to default"""
        if self.renderer:
            self.renderer.reset_view()
            self.render_fractal()
            
    def save_image(self):
        """Save current fractal as image"""
        if self.canvas.current_image:
            from PyQt6.QtWidgets import QFileDialog
            filename, _ = QFileDialog.getSaveFileName(
                self, "Save Fractal", "", "PNG (*.png);;JPEG (*.jpg)"
            )
            if filename:
                self.canvas.current_image.save(filename)
                self.info_label.setText(f"💾 Saved to {filename}")
                
    def stop_rendering(self):
        """Stop rendering"""
        self.is_rendering = False


class FractalCanvas(QLabel):
    """Canvas widget for displaying fractal images"""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_viewer = parent
        self.current_image = None
        self.drag_start = None
        
        self.setMinimumSize(400, 400)
        self.setStyleSheet("""
            QLabel {
                background: #2C2C2C;
                border: 3px solid #FFB6C1;
                border-radius: 10px;
            }
        """)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("🍩 Fractal will appear here")
        
    def set_image(self, image):
        """Set and display image"""
        self.current_image = image
        pixmap = QPixmap.fromImage(image)
        scaled = pixmap.scaled(self.size(), 
                              Qt.AspectRatioMode.KeepAspectRatio,
                              Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(scaled)
        
    def mousePressEvent(self, event):
        """Handle mouse press for dragging"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start = event.pos()
            
    def mouseMoveEvent(self, event):
        """Handle mouse drag"""
        if self.drag_start and self.parent_viewer.renderer:
            delta = event.pos() - self.drag_start
            self.parent_viewer.renderer.pan(delta.x(), delta.y())
            self.parent_viewer.render_fractal()
            self.drag_start = event.pos()
            
    def mouseReleaseEvent(self, event):
        """Handle mouse release"""
        self.drag_start = None
        
    def wheelEvent(self, event):
        """Handle mouse wheel for zooming"""
        if self.parent_viewer.renderer:
            delta = event.angleDelta().y()
            zoom_factor = 1.1 if delta > 0 else 0.9
            self.parent_viewer.renderer.zoom(zoom_factor)
            self.parent_viewer.render_fractal()
