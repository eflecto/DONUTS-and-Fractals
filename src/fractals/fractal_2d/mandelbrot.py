"""Mandelbrot Set Implementation"""

import numpy as np
from numba import jit


class Mandelbrot:
    """Classic Mandelbrot fractal"""
    
    def __init__(self):
        self.name = "Mandelbrot Set"
        self.dimension = "2D"
        self.default_center = (0.0, 0.0)
        self.default_zoom = 1.0
        
    @staticmethod
    @jit(nopython=True)
    def calculate(x_coords, y_coords, max_iter):
        """
        Calculate Mandelbrot set
        
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
                    z = z * z + c
                else:
                    result[i, j] = max_iter
                    
        return result
    
    @staticmethod
    def get_interesting_points():
        """Return list of interesting coordinates to explore"""
        return [
            {"name": "Seahorse Valley", "x": -0.75, "y": 0.1, "zoom": 100},
            {"name": "Elephant Valley", "x": 0.3, "y": 0.03, "zoom": 50},
            {"name": "Triple Spiral", "x": -0.761, "y": 0.0852, "zoom": 200},
            {"name": "Needle", "x": -0.7, "y": 0.3, "zoom": 150},
            {"name": "Dendrite", "x": -0.1592, "y": 1.0317, "zoom": 300},
            {"name": "San Marco", "x": -0.75, "y": 0.0, "zoom": 50},
        ]
