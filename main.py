#!/usr/bin/env python3
"""
DONUTS-and-Fractals - Interactive Fractal Visualization Tool
Main entry point for the application
"""

import sys
import json
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from src.ui.main_window import MainWindow
from src.utils.config_loader import ConfigLoader


def setup_application():
    """Setup and configure the Qt application"""
    app = QApplication(sys.argv)
    app.setApplicationName("DONUTS-and-Fractals")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("eflecto")
    
    # Enable high DPI scaling
    app.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
    
    return app


def main():
    """Main application entry point"""
    print("🍩 Starting DONUTS-and-Fractals...")
    
    # Load configuration
    config = ConfigLoader.load_config()
    
    # Create and setup application
    app = setup_application()
    
    # Create main window
    window = MainWindow(config)
    window.show()
    
    print("✨ Application started successfully!")
    print("💡 Select a donut to explore fractals!")
    
    # Run application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
