"""
Genome Rearrangement Analysis Package

This package contains tools for analyzing chromosomal rearrangements,
fragile regions, and genome evolution patterns.

Modules:
    fragile_regions: Analysis of fragile regions and genome rearrangements
"""

from .fragile_regions import (
    GenomeAnalyzer,
    analyze_fragile_regions,
    perform_rearrangement,
    compare_genomes,
    validate_genome
)

__version__ = "1.0.0"
__author__ = "Bioinformatics Team"

__all__ = [
    'GenomeAnalyzer',
    'analyze_fragile_regions',
    'perform_rearrangement',
    'compare_genomes',
    'validate_genome'
]
