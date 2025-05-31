"""
Bioinformatics Utilities Package

This package contains utility functions for various bioinformatics operations
including genome graph manipulations, sequence analysis, and data processing.

Modules:
    genome_graph: Functions for genome and chromosome graph operations
"""

from .genome_graph import (
    chromosome_to_cycle,
    cycle_to_chromosome,
    colored_edges,
    graph_to_genome,
    two_break_genome_graph,
    two_break_on_genome
)

__version__ = "1.0.0"
__author__ = "Bioinformatics Team"

__all__ = [
    'chromosome_to_cycle',
    'cycle_to_chromosome', 
    'colored_edges',
    'graph_to_genome',
    'two_break_genome_graph',
    'two_break_on_genome'
]
