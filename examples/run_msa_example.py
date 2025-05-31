#!/usr/bin/env python3
"""
Example: Multiple Sequence Alignment using Simulated Annealing

This script demonstrates how to use the MSA simulated annealing algorithm
to align multiple DNA or protein sequences. It shows basic usage and
provides example sequences to work with.

Usage:
    python examples/run_msa_example.py

Requirements:
    - Python 3.7+
    - Standard library modules only (no external dependencies)
"""

import sys
import os

# Add the parent directory to Python path to import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from alignment import MSASimulatedAnnealing


def run_dna_alignment_example():
    """Demonstrate MSA with DNA sequences."""
    print("DNA Sequence Alignment Example")
    print("=" * 40)
    
    # Example DNA sequences (inspired by the Garfield example from the notebook)
    dna_sequences = [
        "GARFIELDTHELASTFATCAT",
        "GARFIELDTHEFASTCAT", 
        "GARFIELDTHEVERYFASTCAT",
        "THEFATCAT",
        "GARFIELDTHEVASTCAT"
    ]
    
    print("Input sequences:")
    for i, seq in enumerate(dna_sequences, 1):
        print(f"  Sequence {i}: {seq}")
    
    # Create MSA instance and run alignment
    msa = MSASimulatedAnnealing(dna_sequences)
    print("\nRunning simulated annealing optimization...")
    
    final_alignment, final_score, score_history = msa.align()
    
    # Display results
    print(f"\nResults:")
    print(f"  Initial score: {msa.get_initial_score()}")
    print(f"  Final score: {final_score}")
    print(f"  Score improvement: {msa.get_initial_score() - final_score}")
    print(f"  Optimization iterations: {len(score_history)}")
    
    print("\nInitial alignment:")
    msa.print_alignment("initial")
    
    print("\nFinal optimized alignment:")
    msa.print_alignment("final")
    
    return final_alignment, final_score


def run_protein_alignment_example():
    """Demonstrate MSA with protein sequences."""
    print("\n\nProtein Sequence Alignment Example")
    print("=" * 40)
    
    # Example protein sequences
    protein_sequences = [
        "MVLSPADKTNVKAAW",
        "MVLSPADKTNVKA",
        "MVLSPADKTNVKAAWG",
        "VLSPADKTNVKAAW",
        "MVLSPADKTNVKAAWGK"
    ]
    
    print("Input sequences:")
    for i, seq in enumerate(protein_sequences, 1):
        print(f"  Sequence {i}: {seq}")
    
    # Create MSA instance and run alignment
    msa = MSASimulatedAnnealing(protein_sequences)
    print("\nRunning simulated annealing optimization...")
    
    final_alignment, final_score, score_history = msa.align()
    
    # Display results
    print(f"\nResults:")
    print(f"  Initial score: {msa.get_initial_score()}")
    print(f"  Final score: {final_score}")
    print(f"  Score improvement: {msa.get_initial_score() - final_score}")
    print(f"  Optimization iterations: {len(score_history)}")
    
    print("\nFinal optimized alignment:")
    msa.print_alignment("final")
    
    return final_alignment, final_score


def analyze_score_convergence(score_history):
    """Analyze how the score converged during optimization."""
    print("\n\nScore Convergence Analysis")
    print("=" * 40)
    
    if len(score_history) < 10:
        print("Not enough data points for convergence analysis")
        return
    
    # Show score at different intervals
    intervals = [0, len(score_history)//4, len(score_history)//2, 
                3*len(score_history)//4, len(score_history)-1]
    
    print("Score progression:")
    for i, interval in enumerate(intervals):
        percentage = (interval / (len(score_history)-1)) * 100
        print(f"  {percentage:5.1f}% complete: score = {score_history[interval]}")
    
    # Calculate improvement rate
    initial_score = score_history[0]
    final_score = score_history[-1]
    improvement = initial_score - final_score
    improvement_rate = (improvement / initial_score) * 100 if initial_score > 0 else 0
    
    print(f"\nOverall improvement: {improvement_rate:.2f}%")


def main():
    """Main function to run all examples."""
    print("Multiple Sequence Alignment Examples")
    print("=" * 50)
    print("This script demonstrates the MSA simulated annealing algorithm")
    print("with both DNA and protein sequence examples.\n")
    
    try:
        # Run DNA alignment example
        dna_alignment, dna_score = run_dna_alignment_example()
        
        # Run protein alignment example  
        protein_alignment, protein_score = run_protein_alignment_example()
        
        # Create a detailed example with score analysis
        print("\n\nDetailed Analysis Example")
        print("=" * 40)
        
        test_sequences = ["ACGTACGT", "ACGTCGT", "ACGTACGTT", "CGTACGT"]
        msa = MSASimulatedAnnealing(test_sequences)
        final_alignment, final_score, score_history = msa.align()
        
        analyze_score_convergence(score_history)
        
        print("\n" + "=" * 50)
        print("Examples completed successfully!")
        print("You can modify the sequences in this script to test with your own data.")
        
    except Exception as e:
        print(f"Error running examples: {e}")
        print("Please check that all required modules are properly installed.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())