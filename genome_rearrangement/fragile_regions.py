"""
Fragile Regions Module

This module provides access to genome graph operations that were originally
in FragileRegions.py. These functions serve as building blocks that could
be used for fragile regions analysis in the future.

All functions have been moved to utils/genome_graph.py for better organization
and are re-exported here for backward compatibility.

Original Functions (now in utils/genome_graph.py):
    chromosome_to_cycle: Convert chromosome representation to cycle representation
    cycle_to_chromosome: Convert cycle representation back to chromosome
    colored_edges: Generate colored edges from genome representation
    graph_to_genome: Convert graph representation back to genome
    two_break_genome_graph: Apply two-break rearrangement to genome graph
    two_break_on_genome: Apply two-break rearrangement to genome
"""

import sys
import os

# Add utils directory to path for importing genome_graph module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

try:
    from genome_graph import (
        chromosome_to_cycle,
        cycle_to_chromosome,
        colored_edges,
        graph_to_genome,
        two_break_genome_graph,
        two_break_on_genome
    )
except ImportError:
    print("Warning: Could not import genome_graph utilities.")
    print("Please ensure the utils/genome_graph.py module is available.")

# Re-export all original functions for backward compatibility
__all__ = [
    'chromosome_to_cycle',
    'cycle_to_chromosome',
    'colored_edges', 
    'graph_to_genome',
    'two_break_genome_graph',
    'two_break_on_genome'
]


# Example usage and demonstration of the original functionality
if __name__ == "__main__":
    print("Fragile Regions Module - Original Functionality")
    print("=" * 50)
    
    # Example genome with multiple chromosomes (same as original)
    example_genome = [
        [1, 2, 3, 4, 5],      # Chromosome 1
        [-6, 7, -8],          # Chromosome 2  
        [9, 10, 11, 12]       # Chromosome 3
    ]
    
    print(f"Original genome: {example_genome}")
    
    # Demonstrate the original functions
    print(f"\nDemonstrating original FragileRegions.py functionality:")
    
    # Test chromosome to cycle conversion
    test_chromosome = [1, -2, 3]
    cycle = chromosome_to_cycle(test_chromosome)
    print(f"Chromosome {test_chromosome} -> Cycle {cycle}")
    
    # Test cycle back to chromosome
    back_to_chromosome = cycle_to_chromosome(cycle)
    print(f"Cycle {cycle} -> Chromosome {back_to_chromosome}")
    
    # Test colored edges
    edges = colored_edges(example_genome)
    print(f"Colored edges: {edges}")
    
    # Test two-break operations (if valid parameters exist)
    print(f"\nTwo-break operations available:")
    print(f"- two_break_genome_graph(genome_graph, a, b, c, d)")
    print(f"- two_break_on_genome(genome, a, b, c, d)")
    
    print(f"\nAll original functions from FragileRegions.py are available")
    print(f"and have been refactored into a more organized structure.")
