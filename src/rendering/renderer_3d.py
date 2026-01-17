"""3D Fractal Renderer using ray marching"""

import numpy as np
from PyQt6.QtGui import QImage
from PyQt6.QtCore import QSize
from numba import jit


class Renderer3D:
    """Renderer for 3D fractals using ray marching"""
    
    def __init__(self, size: QSize, config):
        self.width = size.width()
        self.height = size.height()
        self.config = config
        
        # Camera parameters
        self.camera_pos = np.array([0.0, 0.0, -3.0])
        self.camera_target = np.array([0.0, 0.0, 0.0])
        self.camera_up = np.array([0.0, 1.0, 0.0])
        
        # Rotation
        self.rotation_x = 0.0
        self.rotation_y = 0.0
        
    def render(self, fractal_info, max_iterations=8):
        """Render a 3D fractal"""
        # Render Mandelbulb (example)
        image_array = self.render_mandelbulb(max_iterations)
        
        # Convert to QImage
        return self.array_to_qimage(image_array)
    
    def render_mandelbulb(self, power=8):
        """Render Mandelbulb fractal"""
        # Create image array
        image = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        # Camera setup
        fov = 45.0
        aspect = self.width / self.height
        
        for y in range(self.height):
            for x in range(self.width):
                # Calculate ray direction
                px = (2.0 * x / self.width - 1.0) * aspect * np.tan(np.radians(fov / 2))
                py = (1.0 - 2.0 * y / self.height) * np.tan(np.radians(fov / 2))
                
                # Apply rotation
                ray_dir = self.rotate_vector(
                    np.array([px, py, 1.0]), 
                    self.rotation_x, 
                    self.rotation_y
                )
                ray_dir = ray_dir / np.linalg.norm(ray_dir)
                
                # Ray march
                color = self.ray_march(self.camera_pos, ray_dir, power)
                
                # Donut-themed coloring
                image[y, x] = [
                    int(255 * color * 0.9),  # Pink tint
                    int(182 * color * 0.8),
                    int(193 * color * 0.7)
                ]
                
        return image
    
    @staticmethod
    def rotate_vector(v, angle_x, angle_y):
        """Rotate vector by angles"""
        # Rotation around Y axis
        cos_y = np.cos(angle_y)
        sin_y = np.sin(angle_y)
        v = np.array([
            v[0] * cos_y - v[2] * sin_y,
            v[1],
            v[0] * sin_y + v[2] * cos_y
        ])
        
        # Rotation around X axis
        cos_x = np.cos(angle_x)
        sin_x = np.sin(angle_x)
        v = np.array([
            v[0],
            v[1] * cos_x - v[2] * sin_x,
            v[1] * sin_x + v[2] * cos_x
        ])
        
        return v
    
    def ray_march(self, origin, direction, power):
        """Ray marching algorithm"""
        max_steps = 100
        max_dist = 10.0
        min_dist = 0.001
        
        total_dist = 0.0
        
        for step in range(max_steps):
            pos = origin + direction * total_dist
            
            # Distance estimation to Mandelbulb
            dist = self.mandelbulb_de(pos, power)
            
            if dist < min_dist:
                # Hit! Calculate shading
                normal = self.estimate_normal(pos, power)
                light_dir = np.array([1.0, 1.0, -1.0])
                light_dir = light_dir / np.linalg.norm(light_dir)
                
                # Simple diffuse lighting
                diffuse = max(0.0, np.dot(normal, light_dir))
                ambient = 0.2
                
                return ambient + diffuse * 0.8
            
            total_dist += dist
            
            if total_dist > max_dist:
                break
        
        # Miss - return background
        return 0.0
    
    @staticmethod
    def mandelbulb_de(pos, power=8, max_iter=10):
        """Distance estimator for Mandelbulb"""
        z = pos.copy()
        dr = 1.0
        r = 0.0
        
        for i in range(max_iter):
            r = np.linalg.norm(z)
            
            if r > 2.0:
                break
            
            # Convert to spherical coordinates
            theta = np.arctan2(np.sqrt(z[0]**2 + z[1]**2), z[2])
            phi = np.arctan2(z[1], z[0])
            
            dr = pow(r, power - 1) * power * dr + 1.0
            
            # Scale and rotate
            zr = pow(r, power)
            theta = theta * power
            phi = phi * power
            
            # Convert back to cartesian
            z = zr * np.array([
                np.sin(theta) * np.cos(phi),
                np.sin(phi) * np.sin(theta),
                np.cos(theta)
            ])
            z += pos
        
        return 0.5 * np.log(r) * r / dr
    
    def estimate_normal(self, pos, power):
        """Estimate surface normal using gradient"""
        eps = 0.001
        
        normal = np.array([
            self.mandelbulb_de(pos + np.array([eps, 0, 0]), power) - 
            self.mandelbulb_de(pos - np.array([eps, 0, 0]), power),
            
            self.mandelbulb_de(pos + np.array([0, eps, 0]), power) - 
            self.mandelbulb_de(pos - np.array([0, eps, 0]), power),
            
            self.mandelbulb_de(pos + np.array([0, 0, eps]), power) - 
            self.mandelbulb_de(pos - np.array([0, 0, eps]), power)
        ])
        
        return normal / np.linalg.norm(normal)
    
    def array_to_qimage(self, array):
        """Convert numpy array to QImage"""
        height, width, channels = array.shape
        bytes_per_line = channels * width
        
        array = np.ascontiguousarray(array)
        
        image = QImage(array.data, width, height, bytes_per_line,
                      QImage.Format.Format_RGB888)
        
        return image.copy()
    
    def pan(self, dx, dy):
        """Pan the camera"""
        right = np.cross(self.camera_target - self.camera_pos, self.camera_up)
        right = right / np.linalg.norm(right)
        
        self.camera_pos += right * dx * 0.01
        self.camera_pos += self.camera_up * dy * 0.01
        
    def zoom(self, factor):
        """Zoom camera"""
        direction = self.camera_target - self.camera_pos
        self.camera_pos += direction * (1 - factor) * 0.5
        
    def rotate(self, dx, dy):
        """Rotate camera"""
        self.rotation_y += dx * 0.01
        self.rotation_x += dy * 0.01
        
    def reset_view(self):
        """Reset camera to default"""
        self.camera_pos = np.array([0.0, 0.0, -3.0])
        self.rotation_x = 0.0
        self.rotation_y = 0.0
