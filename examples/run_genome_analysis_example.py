#!/usr/bin/env python3
"""
Example: Genome Rearrangement and Fragile Region Analysis

This script demonstrates how to use the genome rearrangement analysis tools
to study chromosomal rearrangements, fragile regions, and genome evolution.

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

from genome_rearrangement import GenomeAnalyzer, analyze_fragile_regions, compare_genomes
from utils import chromosome_to_cycle, colored_edges


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


def demonstrate_fragile_region_analysis():
    """Demonstrate fragile region analysis."""
    print("\n\nFragile Region Analysis")
    print("=" * 40)
    
    # Create a sample genome
    genome = [
        [1, 2, 3, 4, 5],      # Chromosome 1 (even length)
        [-6, 7, -8],          # Chromosome 2 (odd length - potentially fragile)
        [9, 10, 11, 12, 13],  # Chromosome 3 (odd length - potentially fragile)
        [14, 15, 16, 17]      # Chromosome 4 (even length)
    ]
    
    print(f"Analyzing genome: {genome}")
    
    # Perform fragile region analysis
    analysis_results = analyze_fragile_regions(genome)
    
    print(f"\nAnalysis Results:")
    print(f"  Total genes: {analysis_results['statistics']['total_genes']}")
    print(f"  Number of chromosomes: {analysis_results['statistics']['num_chromosomes']}")
    print(f"  Average chromosome length: {analysis_results['statistics']['avg_chromosome_length']:.2f}")
    print(f"  Number of edges: {analysis_results['statistics']['num_edges']}")
    print(f"  Fragile regions found: {analysis_results['statistics']['fragile_regions_count']}")
    
    if analysis_results['fragile_regions']:
        print(f"\nFragile regions details:")
        for i, region in enumerate(analysis_results['fragile_regions']):
            print(f"    Region {i+1}: Chromosome {region['chromosome']}")
            print(f"      Length: {region['length']}")
            print(f"      Genes: {region['genes']}")
            print(f"      Fragility score: {region['fragility_score']:.3f}")
    
    return genome, analysis_results


def demonstrate_genome_analyzer():
    """Demonstrate the GenomeAnalyzer class."""
    print("\n\nGenome Analyzer Demonstration")
    print("=" * 40)
    
    # Create initial genome
    initial_genome = [
        [1, 2, 3, 4],
        [-5, 6, -7],
        [8, 9]
    ]
    
    print(f"Initial genome: {initial_genome}")
    
    try:
        # Create analyzer
        analyzer = GenomeAnalyzer(initial_genome)
        
        # Get initial statistics
        stats = analyzer.get_statistics()
        print(f"\nInitial validation: {stats['validation']['valid']}")
        print(f"Total genes: {stats['validation']['total_genes']}")
        print(f"Unique genes: {stats['validation']['unique_genes']}")
        
        if stats['validation']['warnings']:
            print(f"Warnings: {stats['validation']['warnings']}")
        
        # Perform fragility analysis
        fragility = analyzer.analyze_fragility()
        print(f"Fragile regions count: {fragility['statistics']['fragile_regions_count']}")
        
        # Attempt a two-break rearrangement
        print(f"\nAttempting two-break rearrangement...")
        try:
            rearrangement_info = analyzer.apply_rearrangement(
                "two_break",
                a=1, b=2, c=3, d=4
            )
            print(f"Rearrangement successful!")
            print(f"New genome: {analyzer.genome}")
            print(f"Rearrangement type: {rearrangement_info['type']}")
            
        except Exception as e:
            print(f"Rearrangement failed: {e}")
            print("This is expected if the specified edges don't exist in the genome graph.")
        
        # Get final statistics
        final_stats = analyzer.get_statistics()
        print(f"\nFinal rearrangement count: {final_stats['rearrangement_count']}")
        
        return analyzer
        
    except ValueError as e:
        print(f"Error creating analyzer: {e}")
        return None


def demonstrate_genome_comparison():
    """Demonstrate genome comparison functionality."""
    print("\n\nGenome Comparison Demonstration")
    print("=" * 40)
    
    # Create two related genomes
    genome1 = [
        [1, 2, 3, 4],
        [5, 6, 7]
    ]
    
    genome2 = [
        [1, 2, 4, 3],  # Rearranged version
        [5, 6, 7]      # Same
    ]
    
    print(f"Genome 1: {genome1}")
    print(f"Genome 2: {genome2}")
    
    # Compare genomes
    comparison = compare_genomes(genome1, genome2)
    
    print(f"\nComparison Results:")
    print(f"  Common edges: {len(comparison['common_edges'])}")
    print(f"  Unique to genome 1: {len(comparison['genome1_unique_edges'])}")
    print(f"  Unique to genome 2: {len(comparison['genome2_unique_edges'])}")
    print(f"  Total differences: {comparison['difference_count']}")
    print(f"  Similarity ratio: {comparison['similarity_ratio']:.3f}")
    
    if comparison['genome1_unique_edges']:
        print(f"  Edges unique to genome 1: {comparison['genome1_unique_edges']}")
    
    if comparison['genome2_unique_edges']:
        print(f"  Edges unique to genome 2: {comparison['genome2_unique_edges']}")
    
    return comparison


def demonstrate_validation():
    """Demonstrate genome validation."""
    print("\n\nGenome Validation Demonstration")
    print("=" * 40)
    
    # Test valid genome
    valid_genome = [[1, 2, 3], [-4, 5]]
    print(f"Testing valid genome: {valid_genome}")
    
    try:
        analyzer = GenomeAnalyzer(valid_genome)
        print("✓ Valid genome accepted")
    except ValueError as e:
        print(f"✗ Unexpected error: {e}")
    
    # Test invalid genome (duplicate genes)
    print(f"\nTesting invalid genome with duplicates: [[1, 2], [2, 3]]")
    try:
        invalid_genome = [[1, 2], [2, 3]]  # Gene 2 appears twice
        analyzer = GenomeAnalyzer(invalid_genome)
        print("✗ Invalid genome was incorrectly accepted")
    except ValueError as e:
        print(f"✓ Invalid genome correctly rejected: {e}")
    
    # Test genome with zero (invalid)
    print(f"\nTesting invalid genome with zero: [[1, 0, 3]]")
    try:
        zero_genome = [[1, 0, 3]]  # Gene 0 is invalid
        analyzer = GenomeAnalyzer(zero_genome)
        print("✗ Zero-gene genome was incorrectly accepted")
    except ValueError as e:
        print(f"✓ Zero-gene genome correctly rejected")


def main():
    """Main function to run all demonstrations."""
    print("Genome Rearrangement and Fragile Region Analysis Examples")
    print("=" * 60)
    print("This script demonstrates various genome analysis tools and algorithms.\n")
    
    try:
        # Run all demonstrations
        genome = demonstrate_basic_genome_operations()
        genome, analysis = demonstrate_fragile_region_analysis()
        analyzer = demonstrate_genome_analyzer()
        comparison = demonstrate_genome_comparison()
        demonstrate_validation()
        
        print("\n" + "=" * 60)
        print("All demonstrations completed successfully!")
        print("\nKey takeaways:")
        print("• Genome graphs provide a powerful representation for studying rearrangements")
        print("• Fragile regions can be identified through structural analysis")
        print("• The GenomeAnalyzer class provides comprehensive analysis tools")
        print("• Genome comparison helps identify evolutionary relationships")
        print("• Input validation ensures data integrity")
        
        print("\nYou can modify the genomes in this script to analyze your own data.")
        
    except Exception as e:
        print(f"Error running demonstrations: {e}")
        print("Please check that all required modules are properly installed.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
