"""
Genome Graph Operations Module

This module contains functions for manipulating genome structures using graph-based
representations. These functions are commonly used in bioinformatics for analyzing
chromosomal rearrangements and genome evolution.

Functions:
    chromosome_to_cycle: Convert chromosome representation to cycle representation
    cycle_to_chromosome: Convert cycle representation back to chromosome
    colored_edges: Generate colored edges from genome representation
    graph_to_genome: Convert graph representation back to genome
    two_break_genome_graph: Apply two-break rearrangement to genome graph
    two_break_on_genome: Apply two-break rearrangement to genome
"""


def chromosome_to_cycle(chromosome):
    """
    Convert a chromosome representation to a cycle representation.
    
    This function transforms a signed permutation (chromosome) into a cycle
    of nodes following the standard breakpoint graph construction.
    
    Args:
        chromosome (list): A list of signed integers representing genes
                          Positive integers represent genes in forward orientation
                          Negative integers represent genes in reverse orientation
    
    Returns:
        list: A list of nodes representing the cycle
              Each gene is represented by two consecutive nodes
    
    Example:
        >>> chromosome_to_cycle([1, -2, 3])
        [1, 2, 4, 3, 5, 6]
    """
    nodes = []
    for i in range(len(chromosome)):
        gene = chromosome[i]
        if int(gene) > 0:
            # Forward orientation: (2*gene-1, 2*gene)
            nodes.append(2 * int(gene) - 1)
            nodes.append(2 * int(gene))
        else:
            # Reverse orientation: (-2*gene, -2*gene-1)
            nodes.append(-2 * int(gene))
            nodes.append(-2 * int(gene) - 1)
    return nodes


def cycle_to_chromosome(nodes):
    """
    Convert a cycle representation back to a chromosome representation.
    
    This function reverses the transformation performed by chromosome_to_cycle,
    converting a cycle of nodes back to a signed permutation.
    
    Args:
        nodes (list): A list of nodes representing a cycle
        
    Returns:
        list: A list of signed integers representing the chromosome
              Positive integers represent genes in forward orientation
              Negative integers represent genes in reverse orientation
    
    Example:
        >>> cycle_to_chromosome([1, 2, 4, 3, 5, 6])
        [1, -2, 3]
    """
    chromosome = []
    for i in range(0, int(len(nodes) / 2)):
        if nodes[2 * i] < nodes[2 * i + 1]:
            # Forward orientation
            chromosome.append(int(nodes[2 * i + 1] / 2))
        else:
            # Reverse orientation
            chromosome.append(int(-nodes[2 * i] / 2))
    return chromosome


def colored_edges(genome):
    """
    Generate colored edges from a genome representation.
    
    This function creates a set of colored edges that represent the adjacencies
    between genes in a genome, following the breakpoint graph model.
    
    Args:
        genome (list): A list of chromosomes, where each chromosome is a list
                      of signed integers representing genes
    
    Returns:
        tuple: A tuple of edge pairs representing colored edges
               Each edge is a tuple of two nodes
    
    Example:
        >>> colored_edges([[1, -2, 3], [4, 5]])
        ((2, 4), (3, 5), (6, 1), (7, 8), (10, 7))
    """
    edges = []
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome)
        for j in range(len(chromosome)):
            # Connect each gene's tail to the next gene's head
            pair = (nodes[2 * j + 1], nodes[(2 * j + 2) % len(nodes)])
            edges.append(tuple(pair))
    return tuple(edges)


def graph_to_genome(graph):
    """
    Convert a graph representation back to a genome representation.
    
    This function reconstructs the genome from its graph representation,
    essentially performing the inverse operation of colored_edges.
    
    Args:
        graph (list): A list of edge pairs representing the genome graph
        
    Returns:
        tuple: A tuple of chromosomes, where each chromosome is a tuple
               of signed integers representing genes
    
    Note:
        This function has a bug in the original code (returns "Nuple" instead of "tuple")
        which has been fixed in this refactored version.
    """
    genome = []
    if not graph:
        return tuple(genome)
    
    init = graph[0][0]
    if init % 2 == 0:
        end = init - 1
    else:
        end = init + 1
    
    chromosome = []
    i = 0
    
    while True:
        if init % 2 == 0:
            chromosome.append(int(init / 2))
        else:
            chromosome.append(int(-(init + 1) / 2))
        
        next_node = graph[i][1]
        if next_node == end:
            genome.append(tuple(chromosome))
            if i == len(graph) - 1:
                break
            i = i + 1
            if i == len(graph):
                break
            init = graph[i][0]
            if init % 2 == 0:
                end = init - 1
            else:
                end = init + 1
            chromosome = []
            continue
        
        i = i + 1
        if i < len(graph):
            init = graph[i][0]
        else:
            break
    
    return tuple(genome)


def two_break_genome_graph(genome_graph, a, b, c, d):
    """
    Apply a two-break rearrangement to a genome graph.
    
    This function performs a two-break operation on the genome graph by
    replacing edges (a,b) and (c,d) with edges (a,c) and (b,d).
    
    Args:
        genome_graph (list): A list of edge pairs representing the genome graph
        a, b, c, d (int): The four nodes involved in the two-break operation
        
    Returns:
        list: The modified genome graph after the two-break operation
    
    Example:
        >>> two_break_genome_graph([(1,2), (3,4)], 1, 2, 3, 4)
        [(1,3), (2,4)]
    """
    modified_graph = []
    for edge in genome_graph:
        if edge == (a, b):
            modified_graph.append((a, c))
        elif edge == (b, a):
            modified_graph.append((b, d))
        elif edge == (c, d):
            modified_graph.append((c, a))
        elif edge == (d, c):
            modified_graph.append((d, b))
        else:
            modified_graph.append(edge)
    return modified_graph


def two_break_on_genome(genome, a, b, c, d):
    """
    Apply a two-break rearrangement to a genome.
    
    This function performs a complete two-break operation on a genome by:
    1. Converting the genome to its graph representation
    2. Applying the two-break operation to the graph
    3. Converting the modified graph back to genome representation
    
    Args:
        genome (list): A list of chromosomes representing the genome
        a, b, c, d (int): The four nodes involved in the two-break operation
        
    Returns:
        tuple: The modified genome after the two-break operation
    
    Example:
        >>> two_break_on_genome([[1, 2, 3]], 1, 2, 3, 4)
        # Returns the rearranged genome
    """
    graph = colored_edges(genome)
    graph = two_break_genome_graph(graph, a, b, c, d)
    modified_genome = graph_to_genome(graph)
    return modified_genome
