"""Julia Set Implementation"""

import numpy as np
from numba import jit


class JuliaSet:
    """Julia set fractal with customizable parameter"""
    
    def __init__(self, c_real=-0.4, c_imag=0.6):
        self.name = "Julia Set"
        self.dimension = "2D"
        self.c = complex(c_real, c_imag)
        self.default_center = (0.0, 0.0)
        self.default_zoom = 1.0
        
    @staticmethod
    @jit(nopython=True)
    def calculate(x_coords, y_coords, c_real, c_imag, max_iter):
        """
        Calculate Julia set
        
        Args:
            x_coords: Array of x coordinates
            y_coords: Array of y coordinates
            c_real: Real part of complex parameter
            c_imag: Imaginary part of complex parameter
            max_iter: Maximum iterations
            
        Returns:
            2D array of iteration counts
        """
        height = len(y_coords)
        width = len(x_coords)
        result = np.zeros((height, width), dtype=np.int32)
        c = complex(c_real, c_imag)
        
        for i in range(height):
            for j in range(width):
                z = complex(x_coords[j], y_coords[i])
                
                for n in range(max_iter):
                    if abs(z) > 2.0:
                        result[i, j] = n
                        break
                    z = z * z + c
                else:
                    result[i, j] = max_iter
                    
        return result
    
    def calculate_with_param(self, x_coords, y_coords, max_iter):
        """Calculate with current parameter"""
        return self.calculate(x_coords, y_coords, 
                             self.c.real, self.c.imag, max_iter)
    
    @staticmethod
    def get_interesting_parameters():
        """Return list of interesting c parameters"""
        return [
            {"name": "Dendrite", "c": complex(-0.4, 0.6)},
            {"name": "Dragon", "c": complex(-0.8, 0.156)},
            {"name": "Douady Rabbit", "c": complex(-0.123, 0.745)},
            {"name": "San Marco", "c": complex(-0.75, 0.0)},
            {"name": "Siegel Disk", "c": complex(-0.391, -0.587)},
            {"name": "Spiral", "c": complex(0.285, 0.01)},
            {"name": "Snowflake", "c": complex(-0.4, -0.59)},
        ]
