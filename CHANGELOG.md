# Changelog

All notable changes to DONUTS-and-Fractals will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-17

### Added - Initial Release 🎉

#### Core Features
- 🍩 Unique donut-themed user interface
- 🎨 15 different 2D fractals with interactive visualization
- 🌀 15 different 3D fractals with ray marching rendering
- 🖱️ Mouse-based navigation and control
- ⚡ NumPy and Numba optimized rendering
- 🎨 Multiple color schemes (Donut, Rainbow, Fire, Ocean, Galaxy)
- 💾 Screenshot export functionality
- ⚙️ Configurable settings via JSON

#### 2D Fractals
- Mandelbrot Set - Classic fractal with infinite detail
- Julia Set - Customizable parameter fractals
- Burning Ship - Ship-like fractal structures
- Newton Fractal - Root-finding visualization
- Phoenix Fractal - Complex dynamics
- Tricorn - Conjugate Mandelbrot
- Barnsley Fern - Nature-inspired IFS
- Sierpinski Triangle - Classic recursive triangle
- Dragon Curve - Paper-folding fractal
- Koch Snowflake - Geometric beauty
- Apollonian Gasket - Circle packing
- Lyapunov Fractal - Chaos theory
- Bifurcation Diagram - Logistic map
- Hilbert Curve - Space-filling curve
- Gosper Curve - Flowsnake pattern

#### 3D Fractals
- Mandelbulb - 3D Mandelbrot extension
- Menger Sponge - 3D Sierpinski
- Sierpinski Pyramid - Tetrahedral fractal
- Julia 3D - Three-dimensional Julia set
- Quaternion Julia - 4D in 3D space
- Mandelbox - Box-folding fractal
- Klein Bottle - Non-orientable surface
- Lorenz Attractor - Chaotic system
- Cube Fractal - Recursive cubes
- Dodecahedron Fractal - 12-sided polyhedron
- Icosahedron Fractal - 20-sided polyhedron
- Tree 3D - Branching structure
- Apollonian Sphere - 3D sphere packing
- Tetrahedral Fractal - Pyramid subdivision
- Octahedral Fractal - 8-sided polyhedron

#### User Interface
- Main menu with donut-shaped fractal selectors
- Interactive fractal viewer with controls
- Real-time iteration adjustment slider
- Reset view functionality
- Save image dialog
- Keyboard shortcuts support

#### Documentation
- Comprehensive README with features and installation
- Detailed installation guide (INSTALL.md)
- User guide with tutorials (USER_GUIDE.md)
- FAQ with common questions
- Contributing guidelines (CONTRIBUTING.md)
- MIT License

#### Technical
- PyQt6-based GUI framework
- NumPy for mathematical operations
- Numba JIT compilation for performance
- PyOpenGL for 3D rendering
- Ray marching for 3D fractals
- Configurable rendering parameters
- Multi-threaded support (optional)

### Performance Optimizations
- JIT compilation with Numba for critical loops
- Efficient NumPy array operations
- Optimized ray marching algorithm
- Configurable quality levels

### Configuration
- JSON-based configuration system
- Customizable color schemes
- Adjustable rendering quality
- Window size and display settings
- Export settings

## [Unreleased]

### Planned Features
- [ ] Animation and keyframe system
- [ ] Video recording and export
- [ ] VR support for 3D fractals
- [ ] Fractal-based music generation
- [ ] Cloud preset sharing
- [ ] Batch rendering
- [ ] Custom fractal scripting
- [ ] Mobile app version
- [ ] Web-based version
- [ ] Plugin system

### Planned Improvements
- [ ] GPU acceleration for 3D rendering
- [ ] Improved UI/UX with more animations
- [ ] Advanced color mapping options
- [ ] Fractal morphing and transitions
- [ ] Real-time parameter tweaking
- [ ] Preset management system
- [ ] Tutorial mode for beginners
- [ ] Advanced camera controls
- [ ] Depth of field effects
- [ ] Post-processing filters

### Known Issues
- Some 3D fractals render slowly on integrated GPUs
- Very high iteration counts may cause UI freezing
- Ray marching precision limits at extreme zoom levels

## Version History

### Version Numbering
- **Major.Minor.Patch** (e.g., 1.2.3)
- **Major**: Breaking changes or major new features
- **Minor**: New features, backward compatible
- **Patch**: Bug fixes and minor improvements

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute to this project.

## Support

For bug reports and feature requests, please create an issue on GitHub:
https://github.com/eflecto/DONUTS-and-Fractals/issues

---

**Made with ❤️ and 🍩**
