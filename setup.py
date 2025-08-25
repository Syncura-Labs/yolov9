#!/usr/bin/env python3
"""
Setup script for YOLOv9 - Learning What You Want to Learn Using Programmable Gradient Information

Implementation of the YOLOv9 architecture for object detection, instance segmentation, 
and panoptic segmentation tasks.
"""

import os
import re
from pathlib import Path
from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements.txt and return list of dependencies."""
    req_file = Path(__file__).parent / 'requirements.txt'
    if not req_file.exists():
        return []
    
    requirements = []
    with open(req_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if line and not line.startswith('#'):
                requirements.append(line)
    
    return requirements


def read_long_description():
    """Read README.md for long description."""
    readme_file = Path(__file__).parent / 'README.md'
    if readme_file.exists():
        with open(readme_file, 'r', encoding='utf-8') as f:
            return f.read()
    return ""


# Package metadata
NAME = "yolov9"
VERSION = "1.0.0"
DESCRIPTION = "YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information"
LONG_DESCRIPTION = read_long_description()
AUTHOR = "Chien-Yao Wang, Hong-Yuan Mark Liao"
AUTHOR_EMAIL = ""
URL = "https://github.com/WongKinYiu/yolov9"
LICENSE = "GPL-3.0"

# Read requirements
INSTALL_REQUIRES = read_requirements()

# Optional dependencies
EXTRAS_REQUIRE = {
    'export': [
        'coremltools>=6.0',
        'onnx>=1.9.0',
        'onnx-simplifier>=0.4.1',
        'nvidia-pyindex',
        'nvidia-tensorrt',
        'scikit-learn<=1.1.2',
        'tensorflow>=2.4.1',
        'tensorflowjs>=3.9.0',
        'openvino-dev',
    ],
    'logging': [
        'clearml>=1.2.0',
        'comet-ml',
    ],
    'deploy': [
        'tritonclient[all]~=2.24.0',
    ],
    'extras': [
        'mss',
    ]
}

# Add 'all' option to install all optional dependencies
EXTRAS_REQUIRE['all'] = sum(EXTRAS_REQUIRE.values(), [])

# Console scripts for main functionalities
CONSOLE_SCRIPTS = [
    'yolov9-detect=detect:main',
    'yolov9-train=train:main', 
    'yolov9-val=val:main',
    'yolov9-export=export:main',
    'yolov9-benchmarks=benchmarks:main',
]

# Package data to include
PACKAGE_DATA = {
    'yolov9': [
        'data/*.yaml',
        'data/hyps/*.yaml',
        'data/images/*',
        'models/detect/*.yaml',
        'models/segment/*.yaml', 
        'models/panoptic/*.yaml',
        'models/hub/*.yaml',
    ]
}

# Include additional files
INCLUDE_PACKAGE_DATA = True
PACKAGE_DIR = {'yolov9': '.'}

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    
    # Package configuration - map current directories to yolov9 namespace
    packages=[
        'yolov9',
        'yolov9.models',
        'yolov9.utils', 
        'yolov9.utils.loggers',
        'yolov9.utils.loggers.clearml',
        'yolov9.utils.loggers.comet', 
        'yolov9.utils.loggers.wandb',
        'yolov9.utils.segment',
        'yolov9.utils.segment.tal',
        'yolov9.utils.panoptic',
        'yolov9.utils.panoptic.tal', 
        'yolov9.utils.tal',
        'yolov9.classify',
        'yolov9.segment',
        'yolov9.panoptic',
    ],
    package_dir={
        'yolov9': '.',
        'yolov9.models': 'models',
        'yolov9.utils': 'utils',
        'yolov9.utils.loggers': 'utils/loggers',
        'yolov9.utils.loggers.clearml': 'utils/loggers/clearml',
        'yolov9.utils.loggers.comet': 'utils/loggers/comet',
        'yolov9.utils.loggers.wandb': 'utils/loggers/wandb',
        'yolov9.utils.segment': 'utils/segment',
        'yolov9.utils.segment.tal': 'utils/segment/tal',
        'yolov9.utils.panoptic': 'utils/panoptic',
        'yolov9.utils.panoptic.tal': 'utils/panoptic/tal',
        'yolov9.utils.tal': 'utils/tal',
        'yolov9.classify': 'classify',
        'yolov9.segment': 'segment',
        'yolov9.panoptic': 'panoptic',
    },
    package_data=PACKAGE_DATA,
    include_package_data=INCLUDE_PACKAGE_DATA,
    
    # Dependencies
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires='>=3.7',
    
    # Entry points
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
    },
    
    # Classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8', 
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
    ],
    
    # Keywords
    keywords='yolo, object-detection, computer-vision, deep-learning, pytorch, neural-networks, segmentation',
    
    # Project URLs
    project_urls={
        'Documentation': 'https://github.com/WongKinYiu/yolov9',
        'Source': 'https://github.com/WongKinYiu/yolov9',
        'Tracker': 'https://github.com/WongKinYiu/yolov9/issues',
    },
    
    # Zip safe
    zip_safe=False,
)