#!/usr/bin/env python3
"""
Bioinformatics Project - Package Initialization

This package provides a comprehensive collection of bioinformatics algorithms
and tools implemented from scratch in Python.

Author: Harshit
Version: 1.0.0
License: Educational/Research Use

Modules:
    alignment: Sequence alignment algorithms
    utils: Core utility functions and genome graph operations
    examples: Demonstration scripts for MSA algorithm
"""

__version__ = "1.0.0"
__author__ = "Harshit"
__description__ = "Bioinformatics Algorithms and Tools"

# Version history
__changelog__ = {
    "1.0.0": "Initial refactored release with modular structure"
}

# Package metadata
__all__ = [
    'alignment',
    'utils'
]

def get_version():
    """Return the current version string."""
    return __version__

def get_info():
    """Return package information."""
    return {
        'name': 'Bioinformatics',
        'version': __version__,
        'author': __author__,
        'description': __description__
    }

print(f"Bioinformatics Package v{__version__} - {__description__}")