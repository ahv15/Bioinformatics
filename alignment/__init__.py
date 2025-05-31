"""
Sequence Alignment Package

This package contains algorithms and tools for sequence alignment,
including multiple sequence alignment and pairwise alignment methods.

Modules:
    msa_simulated_annealing: Multiple sequence alignment using simulated annealing
"""

from .msa_simulated_annealing import (
    MSASimulatedAnnealing,
    initial_state,
    score_of_alignment,
    find_score,
    simulated_annealing
)

__version__ = "1.0.0"
__author__ = "Bioinformatics Team"

__all__ = [
    'MSASimulatedAnnealing',
    'initial_state',
    'score_of_alignment', 
    'find_score',
    'simulated_annealing'
]
