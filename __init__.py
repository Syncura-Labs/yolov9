"""
YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information
"""

__version__ = '1.0.0'

# Fix import paths for internal modules
import sys
from pathlib import Path

# Add current package directory to path so "from export import" works
_package_dir = Path(__file__).parent
if str(_package_dir) not in sys.path:
    sys.path.insert(0, str(_package_dir))