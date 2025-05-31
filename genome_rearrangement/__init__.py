"""
Genome Rearrangement Analysis Package

This package contains the refactored genome graph operations that were
originally in FragileRegions.py. These functions provide the building
blocks for genome rearrangement analysis.

Modules:
    fragile_regions: Re-exports of original FragileRegions.py functions
"""

from .fragile_regions import (
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
