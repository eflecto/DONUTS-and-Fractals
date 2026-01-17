"""2D Fractal Renderer"""

import numpy as np
from PyQt6.QtGui import QImage, QColor
from PyQt6.QtCore import QSize
from numba import jit


class Renderer2D:
    """Renderer for 2D fractals"""
    
    def __init__(self, size: QSize, config):
        self.width = size.width()
        self.height = size.height()
        self.config = config
        
        # View parameters
        self.center_x = 0.0
        self.center_y = 0.0
        self.zoom = 1.0
        self.default_zoom = 1.0
        
    def render(self, fractal_info, max_iterations=256):
        """Render a 2D fractal"""
        # Get fractal name from info
        if isinstance(fractal_info, dict) and 'description' in fractal_info:
            # It's a fractal_info dict
            fractal_name = "Unknown"
        else:
            fractal_name = "Mandelbrot"  # default
            
        # Create image array
        image_array = self.render_mandelbrot(max_iterations)
        
        # Convert to QImage
        return self.array_to_qimage(image_array)
    
    def render_mandelbrot(self, max_iter):
        """Render Mandelbrot set"""
        # Calculate bounds
        aspect = self.width / self.height
        height_range = 4.0 / self.zoom
        width_range = height_range * aspect
        
        x_min = self.center_x - width_range / 2
        x_max = self.center_x + width_range / 2
        y_min = self.center_y - height_range / 2
        y_max = self.center_y + height_range / 2
        
        # Generate coordinate arrays
        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)
        
        # Calculate fractal
        result = self.mandelbrot_set(x, y, max_iter)
        
        # Apply colormap
        return self.apply_colormap(result, max_iter)
    
    @staticmethod
    @jit(nopython=True)
    def mandelbrot_set(x, y, max_iter):
        """Calculate Mandelbrot set using Numba for speed"""
        result = np.zeros((len(y), len(x)))
        
        for i in range(len(y)):
            for j in range(len(x)):
                c = complex(x[j], y[i])
                z = 0
                
                for n in range(max_iter):
                    if abs(z) > 2:
                        result[i, j] = n
                        break
                    z = z*z + c
                else:
                    result[i, j] = max_iter
                    
        return result
    
    def apply_colormap(self, data, max_iter):
        """Apply color mapping to fractal data"""
        # Normalize data
        normalized = data / max_iter
        
        # Create RGB image
        height, width = data.shape
        image = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Donut-themed color scheme
        for i in range(height):
            for j in range(width):
                t = normalized[i, j]
                
                if t >= 1.0:  # In set
                    image[i, j] = [0, 0, 0]
                else:
                    # Pink to orange gradient
                    r = int(255 * (0.8 + 0.2 * np.sin(t * 10)))
                    g = int(182 * (0.7 + 0.3 * np.cos(t * 8)))
                    b = int(193 * (0.5 + 0.5 * np.sin(t * 6)))
                    image[i, j] = [r, g, b]
                    
        return image
    
    def array_to_qimage(self, array):
        """Convert numpy array to QImage"""
        height, width, channels = array.shape
        bytes_per_line = channels * width
        
        # Ensure array is contiguous
        array = np.ascontiguousarray(array)
        
        image = QImage(array.data, width, height, bytes_per_line, 
                      QImage.Format.Format_RGB888)
        
        # Copy the image data
        return image.copy()
    
    def pan(self, dx, dy):
        """Pan the view"""
        scale = 4.0 / self.zoom / self.width
        self.center_x -= dx * scale
        self.center_y -= dy * scale
        
    def zoom(self, factor):
        """Zoom in/out"""
        self.zoom *= factor
        
    def reset_view(self):
        """Reset to default view"""
        self.center_x = 0.0
        self.center_y = 0.0
        self.zoom = self.default_zoom
