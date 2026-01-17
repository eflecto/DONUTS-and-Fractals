"""Configuration loader utility"""

import json
from pathlib import Path
from typing import Dict, Any


class ConfigLoader:
    """Loads and manages application configuration"""
    
    DEFAULT_CONFIG_PATH = Path(__file__).parent.parent.parent / "config.json"
    
    @classmethod
    def load_config(cls, config_path: Path = None) -> Dict[str, Any]:
        """
        Load configuration from JSON file
        
        Args:
            config_path: Path to config file (optional)
            
        Returns:
            Configuration dictionary
        """
        if config_path is None:
            config_path = cls.DEFAULT_CONFIG_PATH
            
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print(f"✓ Configuration loaded from {config_path}")
            return config
        except FileNotFoundError:
            print(f"⚠ Config file not found, using defaults")
            return cls.get_default_config()
        except json.JSONDecodeError as e:
            print(f"⚠ Error parsing config: {e}, using defaults")
            return cls.get_default_config()
    
    @staticmethod
    def get_default_config() -> Dict[str, Any]:
        """Return default configuration"""
        return {
            "window": {"width": 1280, "height": 720},
            "rendering": {"max_iterations": 256},
            "colors": {"default_scheme": "donut"}
        }
    
    @classmethod
    def save_config(cls, config: Dict[str, Any], config_path: Path = None):
        """Save configuration to JSON file"""
        if config_path is None:
            config_path = cls.DEFAULT_CONFIG_PATH
            
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"✓ Configuration saved to {config_path}")
