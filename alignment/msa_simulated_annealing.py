"""
Multiple Sequence Alignment using Simulated Annealing

This module implements a Multiple Sequence Alignment (MSA) algorithm using
simulated annealing optimization. The algorithm starts with an initial
alignment and iteratively improves it by applying random modifications
and accepting or rejecting them based on the simulated annealing criterion.

Classes:
    MSASimulatedAnnealing: Main class implementing the MSA algorithm

Functions:
    initial_state: Generate initial alignment from input sequences
    score_of_alignment: Calculate alignment score
    find_score: Calculate pairwise alignment score
"""

import random
import math
import re
from itertools import combinations


def initial_state(sequence_list):
    """
    Generate an initial alignment by padding shorter sequences with gaps.
    
    This function creates an initial multiple sequence alignment by finding
    the longest sequence and padding all other sequences with gaps ('-') 
    at random positions to make them all the same length.
    
    Args:
        sequence_list (list): List of DNA/protein sequences as strings
        
    Returns:
        list: List of aligned sequences, all of equal length
        
    Example:
        >>> initial_state(['ACGT', 'ACT', 'ACGTT'])
        ['ACGT-', 'AC-GT', 'ACGTT']
    """
    if not sequence_list:
        return []
    
    length_list = [len(seq) for seq in sequence_list]
    max_length = max(length_list)
    max_position = length_list.index(max_length)
    
    aligned_sequences = []
    for i in range(len(sequence_list)):
        new_sequence = sequence_list[i]
        while len(new_sequence) != max_length:
            # Insert gap at random position
            random_position = random.randrange(len(new_sequence) + 1)
            new_sequence = new_sequence[:random_position] + "-" + new_sequence[random_position:]
        aligned_sequences.append(new_sequence)
    
    return aligned_sequences


def find_score(sequence_pair):
    """
    Calculate the alignment score between two sequences.
    
    This function computes a simple alignment score by counting mismatches
    between two sequences of equal length. Each mismatch contributes 1 to
    the total score (lower scores indicate better alignments).
    
    Args:
        sequence_pair (tuple): A tuple containing two sequences of equal length
        
    Returns:
        int: The number of mismatches between the two sequences
        
    Example:
        >>> find_score(('ACGT', 'ACCT'))
        1
    """
    seq_one = sequence_pair[0]
    seq_two = sequence_pair[1]
    score = 0
    
    for i in range(len(seq_one)):
        if seq_one[i] != seq_two[i]:
            score += 1
    
    return score


def score_of_alignment(sequence_list):
    """
    Calculate the total alignment score for a multiple sequence alignment.
    
    This function computes the sum of pairwise alignment scores for all
    possible pairs of sequences in the alignment.
    
    Args:
        sequence_list (list): List of aligned sequences of equal length
        
    Returns:
        int: Total alignment score (sum of all pairwise scores)
        
    Example:
        >>> score_of_alignment(['ACGT', 'ACCT', 'AGGT'])
        3
    """
    pairs = list(combinations(sequence_list, 2))
    total_score = 0
    
    for pair in pairs:
        total_score += find_score(pair)
    
    return total_score


def delete_gaps(sequence):
    """
    Remove gaps from a sequence and relocate them to the end.
    
    This function finds consecutive gap regions in a sequence, removes a
    random portion of them, and appends the removed gaps to the end of
    the sequence.
    
    Args:
        sequence (str): A sequence that may contain gaps ('-')
        
    Returns:
        str: Modified sequence with some gaps relocated
    """
    # Find gap regions using regex
    gap_iterator = re.finditer(r'^-|[^-]-', sequence)
    
    try:
        start = next(gap_iterator).end() - 1
    except StopIteration:
        return sequence
    
    # Randomly decide whether to continue finding gaps
    while True:
        continue_search = random.choice([True, False])
        if continue_search:
            break
        else:
            try:
                start = next(gap_iterator).end() - 1
            except StopIteration:
                return sequence
    
    # Find the end of the gap region
    temp_pos = start
    while temp_pos != len(sequence) and sequence[temp_pos] == '-':
        temp_pos += 1
    end = temp_pos
    
    # Remove random number of gaps from this region
    gap_count = random.randint(1, len(range(start, end)))
    output_list = list(sequence)
    output_list[start:start + gap_count] = ''
    output_list.append('-' * gap_count)
    
    return ''.join(output_list)


def insert_gaps(sequence):
    """
    Insert gaps at random positions in a sequence.
    
    This function finds gap regions in a sequence, removes some gaps,
    and inserts them at a random position elsewhere in the sequence.
    
    Args:
        sequence (str): A sequence that may contain gaps ('-')
        
    Returns:
        str: Modified sequence with gaps relocated
    """
    # Find gap regions using regex
    gap_iterator = re.finditer(r'^-|[^-]-', sequence)
    
    try:
        start = next(gap_iterator).end() - 1
    except StopIteration:
        return sequence
    
    # Randomly decide whether to continue finding gaps
    while True:
        continue_search = random.choice([True, False])
        if continue_search:
            break
        else:
            try:
                start = next(gap_iterator).end() - 1
            except StopIteration:
                return sequence
    
    # Find the end of the gap region
    temp_pos = start
    while temp_pos != len(sequence) and sequence[temp_pos] == '-':
        temp_pos += 1
    end = temp_pos
    
    # Remove random number of gaps from this region
    gap_count = random.randint(1, len(range(start, end)))
    output_list = list(sequence)
    output_list[start:start + gap_count] = ''
    output_list.insert(random.randrange(len(output_list)), '-' * gap_count)
    
    return ''.join(output_list)


def swap_gaps(sequence):
    """
    Swap gaps with adjacent nucleotides/amino acids.
    
    This function finds gap positions and swaps them with neighboring
    non-gap characters in either direction (left or right).
    
    Args:
        sequence (str): A sequence that may contain gaps ('-')
        
    Returns:
        str: Modified sequence with gaps swapped
    """
    gap_positions = [i for i, char in enumerate(sequence) if char == "-"]
    
    if len(gap_positions) == 0:
        return sequence
    
    # Choose a random gap position
    gap_pos = random.choice(gap_positions)
    direction = random.choice(['left', 'right'])
    result = ""
    
    if direction == 'left':
        # Find the leftmost non-gap character
        start_pos = gap_pos
        while start_pos >= 0 and sequence[start_pos] == '-':
            start_pos -= 1
        start_pos += 1
        
        # Choose random number of characters to move
        char_count = 0 if (len(sequence[:start_pos]) == 0) else random.randrange(len(sequence[:start_pos])) + 1
        char_start_pos = start_pos - char_count
        
        # Perform the swap
        result = (sequence[:char_start_pos] + 
                 sequence[start_pos:gap_pos + 1] + 
                 sequence[char_start_pos:start_pos] + 
                 sequence[gap_pos + 1:])
    else:
        # Find the rightmost non-gap character
        end_pos = gap_pos
        while end_pos < len(sequence) and sequence[end_pos] == '-':
            end_pos += 1
        end_pos -= 1
        
        # Choose random number of characters to move
        char_count = 0 if (len(sequence[end_pos:]) == 0) else random.randrange(len(sequence[end_pos:])) + 1
        char_end_pos = end_pos + char_count
        
        # Perform the swap
        result = (sequence[:gap_pos] + 
                 sequence[end_pos + 1:char_end_pos + 1] + 
                 sequence[gap_pos:end_pos + 1] + 
                 sequence[char_end_pos + 1:])
    
    return result


def next_state(sequence_list):
    """
    Generate the next state by applying random modifications to sequences.
    
    This function applies one of three possible operations (swap, insert, delete)
    to each sequence in the alignment to generate a neighboring state.
    
    Args:
        sequence_list (list): Current alignment state
        
    Returns:
        list: Modified alignment state
    """
    result = []
    for sequence in sequence_list:
        # Choose random operation: 1=swap, 2=insert, 3=delete
        operation_map = {1: swap_gaps, 2: insert_gaps, 3: delete_gaps}
        chosen_operation = random.randint(1, 3)
        result.append(operation_map[chosen_operation](sequence))
    
    return result


def simulated_annealing(current_alignment):
    """
    Perform simulated annealing optimization on the multiple sequence alignment.
    
    This function implements the simulated annealing algorithm to optimize
    a multiple sequence alignment. It starts with high temperature and
    gradually cools down, accepting worse solutions with decreasing probability.
    
    Args:
        current_alignment (list): Initial alignment state
        
    Returns:
        tuple: (final_alignment, final_score, score_history)
            - final_alignment: The best alignment found
            - final_score: Score of the final alignment
            - score_history: List of scores throughout the optimization
    """
    score_history = []
    score_history.append(score_of_alignment(current_alignment))
    
    current_temperature = 1.0
    temperature_limit = 0.0001
    
    while current_temperature > temperature_limit:
        neighbor_alignment = next_state(current_alignment)
        
        current_score = score_of_alignment(current_alignment)
        neighbor_score = score_of_alignment(neighbor_alignment)
        
        if neighbor_score < current_score:
            # Accept better solution
            current_alignment = neighbor_alignment
            score_history.append(neighbor_score)
        else:
            # Accept worse solution with probability based on temperature
            acceptance_probability = math.pow(
                math.e, 
                (current_score - neighbor_score) / current_temperature
            )
            if acceptance_probability > random.random():
                current_alignment = neighbor_alignment
                score_history.append(neighbor_score)
        
        # Cool down the temperature
        current_temperature = current_temperature * 0.99999
    
    return current_alignment, score_of_alignment(current_alignment), score_history


class MSASimulatedAnnealing:
    """
    Multiple Sequence Alignment using Simulated Annealing.
    
    This class provides a complete implementation of multiple sequence alignment
    using simulated annealing optimization. It can align DNA or protein sequences
    and provides methods to run the algorithm and analyze results.
    
    Attributes:
        sequences (list): Input sequences to be aligned
        initial_alignment (list): Initial alignment state
        final_alignment (list): Final optimized alignment
        final_score (int): Score of the final alignment
        score_history (list): History of scores during optimization
    """
    
    def __init__(self, sequences):
        """
        Initialize the MSA algorithm with input sequences.
        
        Args:
            sequences (list): List of sequences to be aligned
        """
        self.sequences = sequences
        self.initial_alignment = None
        self.final_alignment = None
        self.final_score = None
        self.score_history = None
    
    def align(self):
        """
        Perform the multiple sequence alignment.
        
        This method runs the complete MSA algorithm: generates initial alignment,
        applies simulated annealing optimization, and stores the results.
        
        Returns:
            tuple: (final_alignment, final_score, score_history)
        """
        # Generate initial alignment
        self.initial_alignment = initial_state(self.sequences)
        
        # Run simulated annealing
        self.final_alignment, self.final_score, self.score_history = (
            simulated_annealing(self.initial_alignment)
        )
        
        return self.final_alignment, self.final_score, self.score_history
    
    def get_initial_score(self):
        """
        Get the score of the initial alignment.
        
        Returns:
            int: Score of the initial alignment, or None if not yet computed
        """
        if self.initial_alignment:
            return score_of_alignment(self.initial_alignment)
        return None
    
    def print_alignment(self, alignment_type="final"):
        """
        Print the alignment in a readable format.
        
        Args:
            alignment_type (str): Type of alignment to print ("initial" or "final")
        """
        if alignment_type == "initial" and self.initial_alignment:
            print("Initial Alignment:")
            for i, seq in enumerate(self.initial_alignment):
                print(f"Sequence {i+1}: {seq}")
        elif alignment_type == "final" and self.final_alignment:
            print("Final Alignment:")
            for i, seq in enumerate(self.final_alignment):
                print(f"Sequence {i+1}: {seq}")
        else:
            print(f"No {alignment_type} alignment available.")


# Example usage and test case
if __name__ == "__main__":
    # Example sequences from the original notebook
    test_sequences = [
        "GARFIELDTHELASTFATCAT",
        "GARFIELDTHEFASTCAT", 
        "GARFIELDTHEVERYFASTCAT",
        "THEFATCAT",
        "GARFIELDTHEVASTCAT"
    ]
    
    print("Multiple Sequence Alignment using Simulated Annealing")
    print("=" * 55)
    
    # Create MSA instance and run alignment
    msa = MSASimulatedAnnealing(test_sequences)
    final_alignment, final_score, score_history = msa.align()
    
    # Print results
    print(f"\nInitial Score: {msa.get_initial_score()}")
    print(f"Final Score: {final_score}")
    print(f"Score Improvement: {msa.get_initial_score() - final_score}")
    
    print("\nInitial Alignment:")
    msa.print_alignment("initial")
    
    print("\nFinal Alignment:")
    msa.print_alignment("final")
    
    print(f"\nOptimization completed after {len(score_history)} iterations")
