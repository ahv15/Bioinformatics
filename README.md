# Bioinformatics Algorithms and Tools

A comprehensive collection of bioinformatics algorithms and tools implemented from scratch in Python. This repository provides modular, well-documented implementations of key bioinformatics methods including sequence alignment and genome graph operations.


## Project Overview

This repository implements fundamental bioinformatics algorithms with a focus on:
- **Multiple Sequence Alignment (MSA)** using simulated annealing optimization
- **Genome Graph Operations** for studying chromosomal structure and rearrangements  

All algorithms are implemented from scratch without external bioinformatics libraries, making this an excellent educational resource and a solid foundation for custom bioinformatics pipelines.

## Directory Structure

```
├── alignment/                    # Sequence alignment algorithms
│   ├── __init__.py              # Package initialization
│   └── msa_simulated_annealing.py   # Multiple sequence alignment using SA
├── utils/                       # Shared utility functions
│   ├── __init__.py              # Package initialization
│   └── genome_graph.py          # Genome graph operations (refactored from FragileRegions.py)
├── examples/                    # Example scripts and demonstrations
│   └── run_msa_example.py       # MSA algorithm demonstration
├── __init__.py                  # Root package initialization
└── README.md                    # This file
```

## Dependencies & Requirements

**No external dependencies beyond standard Python installation.**

- **Python ≥ 3.7**
- **Standard Library Modules**: `random`, `math`, `re`, `itertools`, `sys`, `os`

This project is designed to run with only Python's standard library, making it easy to install and use in any Python environment.

## 🔧 **Quick Start**

### Installation
```bash
git clone https://github.com/ahv15/Bioinformatics.git
cd Bioinformatics
```

### Running Examples
```bash
# Multiple Sequence Alignment demonstration
python examples/run_msa_example.py
```

### Using as a Library
```python
# Import specific modules
from alignment import MSASimulatedAnnealing
from utils import chromosome_to_cycle, colored_edges, two_break_on_genome

# Use in your code
sequences = ["ACGTACGT", "ACGTCGT", "ACGTACGTT"]
msa = MSASimulatedAnnealing(sequences)
alignment, score, history = msa.align()
```

## Implemented Modules

### 📊 **Sequence Alignment** (`alignment/`)
- **`msa_simulated_annealing.py`**: Multiple sequence alignment using simulated annealing optimization
  - Implements gap insertion/deletion and swapping operations
  - Temperature-based optimization with configurable parameters
  - Supports both DNA and protein sequences
  - Provides comprehensive scoring and optimization tracking
  - Complete `MSASimulatedAnnealing` class with full API

### 🧬 **Genome Graph Operations** (`utils/`)
- **`genome_graph.py`**: Core genome graph manipulation functions (refactored and improved)
  - Chromosome to cycle conversion (`chromosome_to_cycle`)
  - Cycle to chromosome conversion (`cycle_to_chromosome`) 
  - Colored edge generation (`colored_edges`)
  - Graph to genome conversion (`graph_to_genome`) - **Bug fixed**: Nuple → tuple
  - Two-break operations (`two_break_genome_graph`, `two_break_on_genome`)

### 🎯 **Examples & Demonstrations** (`examples/`)
- **`run_msa_example.py`**: Comprehensive demonstration script
  - DNA sequence alignment examples
  - Protein sequence alignment examples  
  - Score convergence analysis
  - Performance tracking and visualization

## Example Usage

### Multiple Sequence Alignment
```python
from alignment import MSASimulatedAnnealing

# Define your sequences
sequences = [
    "GARFIELDTHELASTFATCAT",
    "GARFIELDTHEFASTCAT", 
    "GARFIELDTHEVERYFASTCAT"
]

# Create MSA instance and align
msa = MSASimulatedAnnealing(sequences)
final_alignment, final_score, score_history = msa.align()

# View results
print(f"Final score: {final_score}")
msa.print_alignment("final")
```

### Basic Genome Graph Operations
```python
from utils import chromosome_to_cycle, colored_edges

# Convert chromosome to cycle representation
chromosome = [1, -2, 3, 4]
cycle = chromosome_to_cycle(chromosome)
print(f"Cycle: {cycle}")

# Generate colored edges for genome
genome = [[1, 2, 3], [-4, 5]]
edges = colored_edges(genome)
print(f"Colored edges: {edges}")
```

### Two-Break Rearrangements
```python
from utils import two_break_on_genome

# Define genome structure
genome = [
    [1, 2, 3, 4],     # Chromosome 1
    [-5, 6, -7]       # Chromosome 2 (negative indicates reverse orientation)
]

# Perform two-break rearrangement
rearranged_genome = two_break_on_genome(genome, a=1, b=2, c=3, d=4)
print(f"Rearranged genome: {rearranged_genome}")
```

## Algorithm Details

### Multiple Sequence Alignment (Simulated Annealing)
- **Initial State**: Random gap insertion to equalize sequence lengths
- **Operations**: Gap insertion, deletion, and position swapping  
- **Scoring**: Pairwise mismatch counting across all sequence pairs
- **Optimization**: Simulated annealing with exponential cooling schedule
- **Convergence**: Temperature-based termination criterion

### Genome Graph Operations
- **Chromosome-Cycle Conversion**: Bidirectional transformation between representations
- **Colored Edges**: Adjacency representation for genome structure  
- **Two-Break Operations**: Fundamental rearrangement mechanism
- **Graph-Genome Conversion**: Reconstruction from graph representation
---
