"""
Fragile Regions and Genome Rearrangement Analysis

This module provides functionality for analyzing chromosomal rearrangements
and fragile regions in genomes. It builds upon the genome graph operations
to provide higher-level analysis tools for studying genome evolution.

The module includes functions for:
- Converting between different genome representations
- Analyzing breakpoint graphs  
- Performing two-break rearrangements
- Studying genome fragility

Functions:
    analyze_fragile_regions: Main function to analyze fragile regions
    perform_rearrangement: Apply rearrangements to genomes
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
    

def analyze_fragile_regions(genome, breakpoint_data=None):
    """
    Analyze fragile regions in a genome based on rearrangement patterns.
    
    This function identifies regions of the genome that are prone to
    rearrangements by analyzing breakpoint patterns and frequency.
    
    Args:
        genome (list): List of chromosomes representing the genome
        breakpoint_data (dict, optional): Additional breakpoint information
        
    Returns:
        dict: Analysis results including fragile regions and statistics
        
    Example:
        >>> genome = [[1, 2, 3], [-4, 5]]
        >>> analyze_fragile_regions(genome)
        {'fragile_regions': [...], 'statistics': {...}}
    """
    if not genome:
        return {'fragile_regions': [], 'statistics': {}}
    
    # Convert genome to graph representation for analysis
    edges = colored_edges(genome)
    
    # Calculate basic statistics
    total_genes = sum(len(chromosome) for chromosome in genome)
    num_chromosomes = len(genome)
    num_edges = len(edges)
    
    # Identify potential fragile regions
    # (This is a simplified analysis - real fragile region detection
    #  would require comparative genomics data)
    fragile_regions = []
    
    for i, chromosome in enumerate(genome):
        chromosome_length = len(chromosome)
        # Consider chromosomes with odd number of genes as potentially fragile
        if chromosome_length % 2 == 1:
            fragile_regions.append({
                'chromosome': i,
                'length': chromosome_length,
                'genes': chromosome,
                'fragility_score': 1.0 / chromosome_length
            })
    
    statistics = {
        'total_genes': total_genes,
        'num_chromosomes': num_chromosomes,
        'num_edges': num_edges,
        'avg_chromosome_length': total_genes / num_chromosomes if num_chromosomes > 0 else 0,
        'fragile_regions_count': len(fragile_regions)
    }
    
    return {
        'fragile_regions': fragile_regions,
        'statistics': statistics,
        'edges': edges
    }


def perform_rearrangement(genome, rearrangement_type="two_break", **kwargs):
    """
    Perform a specified type of chromosomal rearrangement on a genome.
    
    This function applies various types of rearrangements to study
    genome evolution and fragility patterns.
    
    Args:
        genome (list): Input genome to rearrange
        rearrangement_type (str): Type of rearrangement ("two_break", "inversion", etc.)
        **kwargs: Additional parameters specific to the rearrangement type
        
    Returns:
        tuple: (rearranged_genome, rearrangement_info)
        
    Example:
        >>> genome = [[1, 2, 3, 4]]
        >>> perform_rearrangement(genome, "two_break", a=1, b=2, c=3, d=4)
        ([[...]], {...})
    """
    if rearrangement_type == "two_break":
        # Extract required parameters
        a = kwargs.get('a')
        b = kwargs.get('b') 
        c = kwargs.get('c')
        d = kwargs.get('d')
        
        if None in [a, b, c, d]:
            raise ValueError("Two-break rearrangement requires parameters a, b, c, d")
        
        # Perform two-break rearrangement
        rearranged_genome = two_break_on_genome(genome, a, b, c, d)
        
        rearrangement_info = {
            'type': 'two_break',
            'parameters': {'a': a, 'b': b, 'c': c, 'd': d},
            'original_edges': colored_edges(genome),
            'new_edges': colored_edges(rearranged_genome)
        }
        
        return rearranged_genome, rearrangement_info
    
    else:
        raise ValueError(f"Unsupported rearrangement type: {rearrangement_type}")


def compare_genomes(genome1, genome2):
    """
    Compare two genomes and identify differences in their structure.
    
    Args:
        genome1, genome2 (list): Genomes to compare
        
    Returns:
        dict: Comparison results including structural differences
    """
    edges1 = colored_edges(genome1)
    edges2 = colored_edges(genome2)
    
    # Find edges that differ between genomes
    edges1_set = set(edges1)
    edges2_set = set(edges2)
    
    unique_to_genome1 = edges1_set - edges2_set
    unique_to_genome2 = edges2_set - edges1_set
    common_edges = edges1_set & edges2_set
    
    return {
        'genome1_unique_edges': list(unique_to_genome1),
        'genome2_unique_edges': list(unique_to_genome2),
        'common_edges': list(common_edges),
        'difference_count': len(unique_to_genome1) + len(unique_to_genome2),
        'similarity_ratio': len(common_edges) / max(len(edges1_set), len(edges2_set))
    }


def validate_genome(genome):
    """
    Validate genome structure and check for inconsistencies.
    
    Args:
        genome (list): Genome to validate
        
    Returns:
        dict: Validation results
    """
    errors = []
    warnings = []
    
    if not genome:
        errors.append("Empty genome")
        return {'valid': False, 'errors': errors, 'warnings': warnings}
    
    # Check for empty chromosomes
    for i, chromosome in enumerate(genome):
        if not chromosome:
            warnings.append(f"Empty chromosome at position {i}")
    
    # Check for duplicate genes (should not occur in valid genomes)
    all_genes = []
    for chromosome in genome:
        for gene in chromosome:
            abs_gene = abs(gene)
            if abs_gene in [abs(g) for g in all_genes]:
                errors.append(f"Duplicate gene {abs_gene} found")
            all_genes.append(gene)
    
    # Check for zero genes (invalid)
    for chromosome in genome:
        for gene in chromosome:
            if gene == 0:
                errors.append("Gene with value 0 found (invalid)")
    
    is_valid = len(errors) == 0
    
    return {
        'valid': is_valid,
        'errors': errors,
        'warnings': warnings,
        'total_genes': len(all_genes),
        'unique_genes': len(set(abs(g) for g in all_genes))
    }


class GenomeAnalyzer:
    """
    A comprehensive class for genome analysis and rearrangement studies.
    
    This class provides methods for analyzing genome structure, performing
    rearrangements, and studying evolutionary patterns.
    
    Attributes:
        genome (list): The current genome being analyzed
        history (list): History of rearrangements applied
    """
    
    def __init__(self, genome):
        """
        Initialize the analyzer with a genome.
        
        Args:
            genome (list): Initial genome to analyze
        """
        validation = validate_genome(genome)
        if not validation['valid']:
            raise ValueError(f"Invalid genome: {validation['errors']}")
        
        self.genome = genome
        self.history = []
    
    def analyze_fragility(self):
        """Analyze fragile regions in the current genome."""
        return analyze_fragile_regions(self.genome)
    
    def apply_rearrangement(self, rearrangement_type, **kwargs):
        """
        Apply a rearrangement to the current genome.
        
        Args:
            rearrangement_type (str): Type of rearrangement
            **kwargs: Parameters for the rearrangement
            
        Returns:
            dict: Results of the rearrangement
        """
        old_genome = self.genome.copy()
        new_genome, info = perform_rearrangement(self.genome, rearrangement_type, **kwargs)
        
        self.genome = new_genome
        self.history.append({
            'operation': rearrangement_type,
            'parameters': kwargs,
            'old_genome': old_genome,
            'new_genome': new_genome,
            'info': info
        })
        
        return info
    
    def compare_to(self, other_genome):
        """Compare current genome to another genome."""
        return compare_genomes(self.genome, other_genome)
    
    def get_statistics(self):
        """Get comprehensive statistics about the current genome."""
        analysis = self.analyze_fragility()
        validation = validate_genome(self.genome)
        
        return {
            'fragility_analysis': analysis,
            'validation': validation,
            'rearrangement_count': len(self.history)
        }


# Example usage and demonstration
if __name__ == "__main__":
    print("Fragile Regions and Genome Rearrangement Analysis")
    print("=" * 50)
    
    # Example genome with multiple chromosomes
    example_genome = [
        [1, 2, 3, 4, 5],      # Chromosome 1
        [-6, 7, -8],          # Chromosome 2  
        [9, 10, 11, 12]       # Chromosome 3
    ]
    
    print(f"Original genome: {example_genome}")
    
    # Create analyzer and perform analysis
    analyzer = GenomeAnalyzer(example_genome)
    
    # Analyze fragile regions
    fragility_results = analyzer.analyze_fragility()
    print(f"\nFragility analysis:")
    print(f"Total genes: {fragility_results['statistics']['total_genes']}")
    print(f"Number of chromosomes: {fragility_results['statistics']['num_chromosomes']}")
    print(f"Fragile regions found: {fragility_results['statistics']['fragile_regions_count']}")
    
    # Perform a two-break rearrangement
    print(f"\nPerforming two-break rearrangement...")
    try:
        rearrangement_result = analyzer.apply_rearrangement(
            "two_break", 
            a=1, b=2, c=3, d=4
        )
        print(f"Rearranged genome: {analyzer.genome}")
    except Exception as e:
        print(f"Rearrangement failed: {e}")
    
    # Get final statistics
    final_stats = analyzer.get_statistics()
    print(f"\nFinal statistics:")
    print(f"Validation status: {final_stats['validation']['valid']}")
    print(f"Total rearrangements applied: {final_stats['rearrangement_count']}")
