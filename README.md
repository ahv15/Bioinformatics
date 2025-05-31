# Bioinformatics Algorithms and Tools

A comprehensive collection of bioinformatics algorithms and tools implemented from scratch in Python. This repository provides modular, well-documented implementations of key bioinformatics methods including sequence alignment, genome rearrangement analysis, and chromosomal structure manipulation.

## Project Overview

This repository implements fundamental bioinformatics algorithms with a focus on:
- **Multiple Sequence Alignment (MSA)** using simulated annealing optimization
- **Genome Rearrangement Analysis** including fragile region detection
- **Chromosomal Graph Operations** for studying genome structure and evolution

## Directory Structure

```
├── alignment/                    # Sequence alignment algorithms
│   ├── __init__.py              # Package initialization
│   └── msa_simulated_annealing.py   # Multiple sequence alignment using SA
├── genome_rearrangement/        # Genome rearrangement analysis tools
│   ├── __init__.py              # Package initialization  
│   └── fragile_regions.py       # Fragile region analysis and genome comparison
├── utils/                       # Shared utility functions
│   ├── __init__.py              # Package initialization
│   └── genome_graph.py          # Core genome graph operations
├── examples/                    # Example scripts and demonstrations
│   ├── run_msa_example.py       # MSA algorithm demonstrations
│   └── run_genome_analysis_example.py  # Genome analysis demonstrations
└── README.md                    # This file
```

## Dependencies & Requirements

**No external dependencies beyond standard Python installation.**

- **Python ≥ 3.7**
- **Standard Library Modules**: `random`, `math`, `re`, `itertools`, `sys`, `os`

This project is designed to run with only Python's standard library, making it easy to install and use in any Python environment.

## Usage Instructions

### Setting Up the Environment

1. **Clone or download** this repository to your local machine
2. **Add to Python Path** (choose one method):
   
   **Method A: Environment Variable**
   ```bash
   export PYTHONPATH="${PYTHONPATH}:/path/to/Bioinformatics"
   ```
   
   **Method B: Direct Import in Scripts**
   ```python
   import sys
   sys.path.append('/path/to/Bioinformatics')
   ```

### Running Example Scripts

**Multiple Sequence Alignment Example:**
```bash
cd /path/to/Bioinformatics
python examples/run_msa_example.py
```

**Genome Analysis Example:**
```bash
cd /path/to/Bioinformatics  
python examples/run_genome_analysis_example.py
```

### Using as a Library

```python
# Import specific modules
from alignment import MSASimulatedAnnealing
from genome_rearrangement import GenomeAnalyzer
from utils import chromosome_to_cycle, colored_edges

# Use in your code
sequences = ["ACGTACGT", "ACGTCGT", "ACGTACGTT"]
msa = MSASimulatedAnnealing(sequences)
alignment, score, history = msa.align()
```

## Implemented Modules/Pipelines

### Sequence Alignment (`alignment/`)
- **`msa_simulated_annealing.py`**: Multiple sequence alignment using simulated annealing optimization
  - Implements gap insertion/deletion and swapping operations
  - Temperature-based optimization with configurable parameters
  - Supports both DNA and protein sequences
  - Provides comprehensive scoring and optimization tracking

### Genome Rearrangement (`genome_rearrangement/`)
- **`fragile_regions.py`**: Comprehensive genome rearrangement analysis toolkit
  - Fragile region identification and analysis
  - Two-break rearrangement operations
  - Genome comparison and validation
  - Statistical analysis of genome structure
  - `GenomeAnalyzer` class for interactive analysis

### Utilities (`utils/`)
- **`genome_graph.py`**: Core genome graph manipulation functions
  - Chromosome to cycle conversion (`chromosome_to_cycle`)
  - Cycle to chromosome conversion (`cycle_to_chromosome`) 
  - Colored edge generation (`colored_edges`)
  - Graph to genome conversion (`graph_to_genome`)
  - Two-break operations (`two_break_genome_graph`, `two_break_on_genome`)

## Example Commands

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

### Genome Rearrangement Analysis
```python
from genome_rearrangement import GenomeAnalyzer

# Define genome structure
genome = [
    [1, 2, 3, 4],     # Chromosome 1
    [-5, 6, -7],      # Chromosome 2 (negative indicates reverse orientation)
    [8, 9]            # Chromosome 3
]

# Analyze genome
analyzer = GenomeAnalyzer(genome)
fragility_analysis = analyzer.analyze_fragility()

# Perform rearrangement
rearrangement_info = analyzer.apply_rearrangement(
    "two_break", 
    a=1, b=2, c=3, d=4
)

print(f"New genome: {analyzer.genome}")
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

## Algorithm Details

### Multiple Sequence Alignment (Simulated Annealing)
- **Initial State**: Random gap insertion to equalize sequence lengths
- **Operations**: Gap insertion, deletion, and position swapping  
- **Scoring**: Pairwise mismatch counting across all sequence pairs
- **Optimization**: Simulated annealing with exponential cooling schedule
- **Convergence**: Temperature-based termination criterion

### Genome Rearrangement Analysis
- **Representation**: Signed permutations with breakpoint graphs
- **Operations**: Two-break rearrangements, inversions
- **Analysis**: Fragile region detection, structural comparison
- **Validation**: Input validation and consistency checking

### Graph Operations
- **Chromosome-Cycle Conversion**: Bidirectional transformation between representations
- **Colored Edges**: Adjacency representation for genome structure  
- **Two-Break Operations**: Fundamental rearrangement mechanism
- **Graph-Genome Conversion**: Reconstruction from graph representation
