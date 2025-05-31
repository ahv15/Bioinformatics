#!/usr/bin/env python3
"""
Example: Genome Graph Operations

This script demonstrates how to use the refactored genome graph operations
that were originally in FragileRegions.py. These functions provide the
building blocks for genome rearrangement analysis.

Usage:
    python examples/run_genome_analysis_example.py

Requirements:
    - Python 3.7+
    - Standard library modules only (no external dependencies)
"""

import sys
import os

# Add the parent directory to Python path to import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from genome_rearrangement import (
    chromosome_to_cycle, 
    cycle_to_chromosome,
    colored_edges,
    graph_to_genome,
    two_break_genome_graph,
    two_break_on_genome
)


def demonstrate_basic_genome_operations():
    """Demonstrate basic genome graph operations."""
    print("Basic Genome Graph Operations")
    print("=" * 40)
    
    # Example chromosome
    chromosome = [1, -2, 3, 4, -5]
    print(f"Original chromosome: {chromosome}")
    
    # Convert to cycle representation
    cycle = chromosome_to_cycle(chromosome)
    print(f"Cycle representation: {cycle}")
    
    # Convert back to chromosome
    back_to_chromosome = cycle_to_chromosome(cycle)
    print(f"Back to chromosome: {back_to_chromosome}")
    
    # Example genome with multiple chromosomes
    genome = [
        [1, 2, 3],
        [-4, 5, -6],
        [7, 8]
    ]
    print(f"\nExample genome: {genome}")
    
    # Get colored edges
    edges = colored_edges(genome)
    print(f"Colored edges: {edges}")
    
    return genome


def demonstrate_two_break_operations():
    """Demonstrate two-break operations on genome graphs."""
    print("\n\nTwo-Break Operations")
    print("=" * 40)
    
    # Simple example genome
    genome = [[1, 2, 3, 4]]
    print(f"Original genome: {genome}")
    
    # Get the graph representation
    graph_edges = colored_edges(genome)
    print(f"Original colored edges: {graph_edges}")
    
    # Demonstrate two-break on graph (if we have valid edges)
    if len(graph_edges) >= 2:
        # For demonstration, let's try a simple two-break
        # Note: In practice, you need to carefully choose a, b, c, d values
        # that correspond to actual edges in the graph
        
        print(f"\nDemonstrating two-break operations:")
        print(f"Function available: two_break_genome_graph(edges, a, b, c, d)")
        print(f"Function available: two_break_on_genome(genome, a, b, c, d)")
        
        # Show the structure without actually performing a break
        # (since we'd need to carefully validate the parameters)
        print(f"\nTo perform a two-break rearrangement:")
        print(f"1. Choose four nodes a, b, c, d that form two edges (a,b) and (c,d)")
        print(f"2. Replace them with edges (a,c) and (b,d)")
        print(f"3. Convert back to genome representation")
    
    return graph_edges


def demonstrate_cycle_conversions():
    """Demonstrate chromosome-cycle conversions."""
    print("\n\nChromosome-Cycle Conversions")
    print("=" * 40)
    
    # Test various chromosome configurations
    test_chromosomes = [
        [1, 2, 3],           # Simple forward
        [-1, 2, -3],         # Mixed orientations
        [4, -5, 6, -7],      # Longer with mixed orientations
        [-1, -2, -3]         # All reverse
    ]
    
    for i, chromosome in enumerate(test_chromosomes, 1):
        print(f"\nTest {i}: {chromosome}")
        
        # Convert to cycle
        cycle = chromosome_to_cycle(chromosome)
        print(f"  Cycle: {cycle}")
        
        # Convert back
        back_to_chromosome = cycle_to_chromosome(cycle)
        print(f"  Back to chromosome: {back_to_chromosome}")
        
        # Verify round-trip conversion
        if chromosome == back_to_chromosome:
            print(f"  ✓ Round-trip conversion successful")
        else:
            print(f"  ✗ Round-trip conversion failed!")


def demonstrate_graph_conversions():
    """Demonstrate graph-genome conversions."""
    print("\n\nGraph-Genome Conversions")
    print("=" * 40)
    
    # Example genomes
    test_genomes = [
        [[1, 2]],                    # Single chromosome, simple
        [[1, 2, 3], [4, 5]],        # Multiple chromosomes
        [[-1, 2], [3, -4, 5]]       # Mixed orientations
    ]
    
    for i, genome in enumerate(test_genomes, 1):
        print(f"\nTest {i}: {genome}")
        
        # Convert to colored edges
        edges = colored_edges(genome)
        print(f"  Colored edges: {edges}")
        
        # Convert back to genome
        try:
            back_to_genome = graph_to_genome(list(edges))  # Convert tuple to list
            print(f"  Back to genome: {back_to_genome}")
            
            # Note: The conversion might not preserve exact chromosome order
            # but should preserve the gene content and relationships
            
        except Exception as e:
            print(f"  Error in conversion: {e}")


def main():
    """Main function to run all demonstrations."""
    print("Genome Graph Operations Examples")
    print("=" * 50)
    print("This script demonstrates the refactored genome graph operations")
    print("that were originally in FragileRegions.py.\n")
    
    try:
        # Run all demonstrations
        genome = demonstrate_basic_genome_operations()
        edges = demonstrate_two_break_operations()
        demonstrate_cycle_conversions()
        demonstrate_graph_conversions()
        
        print("\n" + "=" * 50)
        print("All demonstrations completed successfully!")
        
        print("\nOriginal FragileRegions.py functions available:")
        print("• chromosome_to_cycle() - Convert chromosome to cycle representation")
        print("• cycle_to_chromosome() - Convert cycle back to chromosome")
        print("• colored_edges() - Generate colored edges from genome")
        print("• graph_to_genome() - Convert graph back to genome")
        print("• two_break_genome_graph() - Apply two-break to genome graph")
        print("• two_break_on_genome() - Apply two-break to genome")
        
        print("\nThese functions are now properly organized in:")
        print("• utils/genome_graph.py (implementation)")
        print("• genome_rearrangement/fragile_regions.py (re-exports)")
        
        print("\nYou can import them using:")
        print("from genome_rearrangement import chromosome_to_cycle, colored_edges, ...")
        print("or")
        print("from utils import chromosome_to_cycle, colored_edges, ...")
        
    except Exception as e:
        print(f"Error running demonstrations: {e}")
        print("Please check that all required modules are properly installed.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
