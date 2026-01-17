"""Donut-themed button widget"""

from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import Qt, QSize, QRect, pyqtSignal, QPropertyAnimation
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush, QFont, QRadialGradient, QPainterPath


class DonutButton(QPushButton):
    """Custom donut-shaped button for fractal selection"""
    
    clicked = pyqtSignal()
    
    def __init__(self, name, fractal_info, color1="#FFB6C1", color2="#FF69B4"):
        super().__init__()
        self.fractal_name = name
        self.fractal_info = fractal_info
        self.color1 = QColor(color1)
        self.color2 = QColor(color2)
        self.hover = False
        self.scale = 1.0
        
        self.setFixedSize(200, 200)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setToolTip(f"{name}\n{fractal_info.get('description', '')}")
        
    def enterEvent(self, event):
        """Handle mouse enter"""
        self.hover = True
        self.scale = 1.1
        self.update()
        super().enterEvent(event)
        
    def leaveEvent(self, event):
        """Handle mouse leave"""
        self.hover = False
        self.scale = 1.0
        self.update()
        super().leaveEvent(event)
        
    def paintEvent(self, event):
        """Custom paint event to draw donut"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Calculate scaled dimensions
        rect = self.rect()
        center_x = rect.width() / 2
        center_y = rect.height() / 2
        outer_radius = min(center_x, center_y) * 0.8 * self.scale
        inner_radius = outer_radius * 0.4
        
        # Draw shadow
        if self.hover:
            shadow_gradient = QRadialGradient(center_x, center_y + 5, outer_radius)
            shadow_gradient.setColorAt(0, QColor(0, 0, 0, 50))
            shadow_gradient.setColorAt(1, QColor(0, 0, 0, 0))
            painter.setBrush(QBrush(shadow_gradient))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(int(center_x - outer_radius), 
                              int(center_y - outer_radius + 5),
                              int(outer_radius * 2), 
                              int(outer_radius * 2))
        
        # Draw outer donut circle with gradient
        gradient = QRadialGradient(center_x - outer_radius * 0.3, 
                                  center_y - outer_radius * 0.3, 
                                  outer_radius * 1.5)
        gradient.setColorAt(0, self.color1 if not self.hover else self.color1.lighter(120))
        gradient.setColorAt(1, self.color2 if not self.hover else self.color2.lighter(120))
        
        painter.setBrush(QBrush(gradient))
        painter.setPen(QPen(self.color2.darker(120), 3))
        
        # Create donut path
        outer_path = QPainterPath()
        outer_path.addEllipse(int(center_x - outer_radius), 
                            int(center_y - outer_radius),
                            int(outer_radius * 2), 
                            int(outer_radius * 2))
        
        inner_path = QPainterPath()
        inner_path.addEllipse(int(center_x - inner_radius), 
                            int(center_y - inner_radius),
                            int(inner_radius * 2), 
                            int(inner_radius * 2))
        
        donut_path = outer_path.subtracted(inner_path)
        painter.drawPath(donut_path)
        
        # Draw frosting highlights
        painter.setPen(Qt.PenStyle.NoPen)
        highlight_color = QColor(255, 255, 255, 100)
        painter.setBrush(QBrush(highlight_color))
        
        # Add sprinkles effect
        import random
        random.seed(hash(self.fractal_name))
        for _ in range(15):
            angle = random.uniform(0, 360)
            distance = random.uniform(inner_radius + 10, outer_radius - 10)
            x = center_x + distance * random.uniform(-1, 1)
            y = center_y + distance * random.uniform(-1, 1)
            
            sprinkle_color = QColor(
                random.randint(200, 255),
                random.randint(100, 200),
                random.randint(150, 255)
            )
            painter.setBrush(QBrush(sprinkle_color))
            painter.drawEllipse(int(x - 2), int(y - 2), 4, 8)
        
        # Draw text
        painter.setPen(QColor(255, 255, 255))
        font = QFont("Arial", 11, QFont.Weight.Bold)
        painter.setFont(font)
        
        # Draw fractal name in center
        text_rect = QRect(int(center_x - inner_radius + 5), 
                         int(center_y - 20),
                         int(inner_radius * 2 - 10), 
                         40)
        
        painter.drawText(text_rect, 
                        Qt.AlignmentFlag.AlignCenter | Qt.TextFlag.TextWordWrap, 
                        self.fractal_name)
        
        # Draw dimension badge
        dimension = self.fractal_info.get('dimension', '2D')
        badge_color = QColor("#FF1493" if dimension == "3D" else "#4169E1")
        painter.setBrush(QBrush(badge_color))
        painter.setPen(QPen(Qt.GlobalColor.white, 2))
        
        badge_x = int(center_x + outer_radius - 25)
        badge_y = int(center_y - outer_radius + 10)
        painter.drawEllipse(badge_x, badge_y, 30, 30)
        
        painter.setPen(Qt.GlobalColor.white)
        font.setPointSize(9)
        painter.setFont(font)
        painter.drawText(QRect(badge_x, badge_y, 30, 30), 
                        Qt.AlignmentFlag.AlignCenter, 
                        dimension)
