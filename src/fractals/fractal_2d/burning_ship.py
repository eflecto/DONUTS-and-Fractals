"""Burning Ship Fractal Implementation"""

import numpy as np
from numba import jit


class BurningShip:
    """Burning Ship fractal - similar to Mandelbrot with absolute values"""
    
    def __init__(self):
        self.name = "Burning Ship"
        self.dimension = "2D"
        self.default_center = (-0.5, -0.5)
        self.default_zoom = 0.5
        
    @staticmethod
    @jit(nopython=True)
    def calculate(x_coords, y_coords, max_iter):
        """
        Calculate Burning Ship fractal
        
        The Burning Ship uses absolute values before squaring,
        creating unique ship-like structures.
        
        Args:
            x_coords: Array of x coordinates
            y_coords: Array of y coordinates
            max_iter: Maximum iterations
            
        Returns:
            2D array of iteration counts
        """
        height = len(y_coords)
        width = len(x_coords)
        result = np.zeros((height, width), dtype=np.int32)
        
        for i in range(height):
            for j in range(width):
                c = complex(x_coords[j], y_coords[i])
                z = 0+0j
                
                for n in range(max_iter):
                    if abs(z) > 2.0:
                        result[i, j] = n
                        break
                    # Key difference: take absolute values
                    z = complex(abs(z.real), abs(z.imag))
                    z = z * z + c
                else:
                    result[i, j] = max_iter
                    
        return result
    
    @staticmethod
    def get_interesting_points():
        """Return list of interesting coordinates to explore"""
        return [
            {"name": "Main Ship", "x": -0.5, "y": -0.5, "zoom": 1},
            {"name": "Mast Detail", "x": -1.75, "y": -0.03, "zoom": 100},
            {"name": "Bow", "x": -1.76, "y": -0.02, "zoom": 200},
            {"name": "Coastline", "x": -1.625, "y": -0.06, "zoom": 150},
        ]
