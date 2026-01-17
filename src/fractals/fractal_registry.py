"""Fractal registry - central catalog of all available fractals"""

from typing import Dict, Any


class FractalRegistry:
    """Registry of all available fractals"""
    
    # 2D Fractals
    FRACTALS_2D = {
        "Mandelbrot": {
            "class": "Mandelbrot",
            "dimension": "2D",
            "description": "Classic Mandelbrot set - the most famous fractal",
            "complexity": 3,
            "module": "src.fractals.fractal_2d.mandelbrot"
        },
        "Julia Set": {
            "class": "JuliaSet",
            "dimension": "2D",
            "description": "Beautiful Julia set with customizable parameters",
            "complexity": 3,
            "module": "src.fractals.fractal_2d.julia"
        },
        "Burning Ship": {
            "class": "BurningShip",
            "dimension": "2D",
            "description": "The burning ship fractal - dramatic coastline appearance",
            "complexity": 4,
            "module": "src.fractals.fractal_2d.burning_ship"
        },
        "Newton": {
            "class": "NewtonFractal",
            "dimension": "2D",
            "description": "Newton's method fractal - colorful basin boundaries",
            "complexity": 3,
            "module": "src.fractals.fractal_2d.newton"
        },
        "Phoenix": {
            "class": "PhoenixFractal",
            "dimension": "2D",
            "description": "Phoenix fractal - rising from complex dynamics",
            "complexity": 4,
            "module": "src.fractals.fractal_2d.phoenix"
        },
        "Tricorn": {
            "class": "Tricorn",
            "dimension": "2D",
            "description": "Mandelbar or Tricorn - conjugate Mandelbrot",
            "complexity": 3,
            "module": "src.fractals.fractal_2d.tricorn"
        },
        "Barnsley Fern": {
            "class": "BarnsleyFern",
            "dimension": "2D",
            "description": "Nature-inspired fern pattern using IFS",
            "complexity": 2,
            "module": "src.fractals.fractal_2d.barnsley_fern"
        },
        "Sierpinski": {
            "class": "SierpinskiTriangle",
            "dimension": "2D",
            "description": "Classic Sierpinski triangle - infinite self-similarity",
            "complexity": 2,
            "module": "src.fractals.fractal_2d.sierpinski"
        },
        "Dragon Curve": {
            "class": "DragonCurve",
            "dimension": "2D",
            "description": "Heighway dragon curve - paper folding fractal",
            "complexity": 2,
            "module": "src.fractals.fractal_2d.dragon"
        },
        "Koch Snowflake": {
            "class": "KochSnowflake",
            "dimension": "2D",
            "description": "Koch snowflake - geometric beauty",
            "complexity": 2,
            "module": "src.fractals.fractal_2d.koch"
        },
        "Apollonian": {
            "class": "ApollonianGasket",
            "dimension": "2D",
            "description": "Apollonian gasket - circle packing fractal",
            "complexity": 3,
            "module": "src.fractals.fractal_2d.apollonian"
        },
        "Lyapunov": {
            "class": "LyapunovFractal",
            "dimension": "2D",
            "description": "Lyapunov fractal - chaos theory visualization",
            "complexity": 4,
            "module": "src.fractals.fractal_2d.lyapunov"
        },
        "Bifurcation": {
            "class": "BifurcationDiagram",
            "dimension": "2D",
            "description": "Logistic map bifurcation diagram",
            "complexity": 3,
            "module": "src.fractals.fractal_2d.bifurcation"
        },
        "Hilbert Curve": {
            "class": "HilbertCurve",
            "dimension": "2D",
            "description": "Space-filling Hilbert curve",
            "complexity": 2,
            "module": "src.fractals.fractal_2d.hilbert"
        },
        "Gosper Curve": {
            "class": "GosperCurve",
            "dimension": "2D",
            "description": "Gosper or flowsnake curve",
            "complexity": 3,
            "module": "src.fractals.fractal_2d.gosper"
        }
    }
    
    # 3D Fractals
    FRACTALS_3D = {
        "Mandelbulb": {
            "class": "Mandelbulb",
            "dimension": "3D",
            "description": "3D Mandelbrot - stunning bulbous fractal",
            "complexity": 5,
            "module": "src.fractals.fractal_3d.mandelbulb"
        },
        "Menger Sponge": {
            "class": "MengerSponge",
            "dimension": "3D",
            "description": "3D Sierpinski - infinite holes",
            "complexity": 4,
            "module": "src.fractals.fractal_3d.menger"
        },
        "Sierpinski 3D": {
            "class": "SierpinskiPyramid",
            "dimension": "3D",
            "description": "Tetrahedral Sierpinski pyramid",
            "complexity": 3,
            "module": "src.fractals.fractal_3d.sierpinski_3d"
        },
        "Julia 3D": {
            "class": "Julia3D",
            "dimension": "3D",
            "description": "3D Julia set - mesmerizing complexity",
            "complexity": 4,
            "module": "src.fractals.fractal_3d.julia_3d"
        },
        "Quaternion": {
            "class": "QuaternionJulia",
            "dimension": "3D",
            "description": "4D quaternion Julia in 3D space",
            "complexity": 5,
            "module": "src.fractals.fractal_3d.quaternion"
        },
        "Mandelbox": {
            "class": "Mandelbox",
            "dimension": "3D",
            "description": "Box-like fractal with amazing detail",
            "complexity": 5,
            "module": "src.fractals.fractal_3d.mandelbox"
        },
        "Klein Bottle": {
            "class": "KleinBottle",
            "dimension": "3D",
            "description": "Non-orientable surface fractal",
            "complexity": 4,
            "module": "src.fractals.fractal_3d.klein"
        },
        "Lorenz": {
            "class": "LorenzAttractor",
            "dimension": "3D",
            "description": "Chaotic Lorenz attractor butterfly",
            "complexity": 3,
            "module": "src.fractals.fractal_3d.lorenz"
        },
        "Cube Fractal": {
            "class": "CubeFractal",
            "dimension": "3D",
            "description": "Recursive cube subdivision",
            "complexity": 3,
            "module": "src.fractals.fractal_3d.cube"
        },
        "Dodecahedron": {
            "class": "DodecahedronFractal",
            "dimension": "3D",
            "description": "12-sided polyhedron fractal",
            "complexity": 4,
            "module": "src.fractals.fractal_3d.dodecahedron"
        },
        "Icosahedron": {
            "class": "IcosahedronFractal",
            "dimension": "3D",
            "description": "20-sided polyhedron fractal",
            "complexity": 4,
            "module": "src.fractals.fractal_3d.icosahedron"
        },
        "Tree 3D": {
            "class": "Tree3D",
            "dimension": "3D",
            "description": "3D fractal tree structure",
            "complexity": 3,
            "module": "src.fractals.fractal_3d.tree"
        },
        "Apollonian 3D": {
            "class": "ApollonianSphere",
            "dimension": "3D",
            "description": "3D sphere packing fractal",
            "complexity": 4,
            "module": "src.fractals.fractal_3d.apollonian_3d"
        },
        "Tetrahedron": {
            "class": "TetrahedralFractal",
            "dimension": "3D",
            "description": "Tetrahedral fractal subdivision",
            "complexity": 3,
            "module": "src.fractals.fractal_3d.tetrahedron"
        },
        "Octahedron": {
            "class": "OctahedralFractal",
            "dimension": "3D",
            "description": "8-sided octahedral fractal",
            "complexity": 3,
            "module": "src.fractals.fractal_3d.octahedron"
        }
    }
    
    @classmethod
    def get_all_fractals(cls) -> Dict[str, Any]:
        """Get all registered fractals"""
        all_fractals = {}
        all_fractals.update(cls.FRACTALS_2D)
        all_fractals.update(cls.FRACTALS_3D)
        return all_fractals
    
    @classmethod
    def get_2d_fractals(cls) -> Dict[str, Any]:
        """Get only 2D fractals"""
        return cls.FRACTALS_2D.copy()
    
    @classmethod
    def get_3d_fractals(cls) -> Dict[str, Any]:
        """Get only 3D fractals"""
        return cls.FRACTALS_3D.copy()
    
    @classmethod
    def get_fractal(cls, name: str) -> Dict[str, Any]:
        """Get specific fractal by name"""
        all_fractals = cls.get_all_fractals()
        return all_fractals.get(name)
