# Bioinformatics Algorithms and Tools

A comprehensive collection of bioinformatics algorithms and tools implemented from scratch in Python. This repository provides modular, well-documented implementations of key bioinformatics methods including sequence alignment and genome graph operations.

## Project Overview

This repository implements fundamental bioinformatics algorithms with a focus on:
- **Multiple Sequence Alignment (MSA)** using simulated annealing optimization
- **Genome Graph Operations** for studying chromosomal structure and rearrangements
- **Modular Design** with reusable utilities and clear separation of concerns

All algorithms are implemented from scratch without external bioinformatics libraries, making this an excellent educational resource and a solid foundation for custom bioinformatics pipelines.

## Directory Structure

```
├── alignment/                    # Sequence alignment algorithms
│   ├── __init__.py              # Package initialization
│   └── msa_simulated_annealing.py   # Multiple sequence alignment using SA
├── genome_rearrangement/        # Genome graph operations (refactored from FragileRegions.py)
│   ├── __init__.py              # Package initialization  
│   └── fragile_regions.py       # Re-exports of original genome graph functions
├── utils/                       # Shared utility functions
│   ├── __init__.py              # Package initialization
│   └── genome_graph.py          # Core genome graph operations
├── examples/                    # Example scripts and demonstrations
│   └── run_msa_example.py       # MSA algorithm demonstration
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

### Using as a Library

```python
# Import specific modules
from alignment import MSASimulatedAnnealing
from genome_rearrangement import chromosome_to_cycle, colored_edges
from utils import graph_to_genome, two_break_on_genome

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

### Genome Graph Operations (`genome_rearrangement/` and `utils/`)
- **`utils/genome_graph.py`**: Core genome graph manipulation functions
  - Chromosome to cycle conversion (`chromosome_to_cycle`)
  - Cycle to chromosome conversion (`cycle_to_chromosome`) 
  - Colored edge generation (`colored_edges`)
  - Graph to genome conversion (`graph_to_genome`)
  - Two-break operations (`two_break_genome_graph`, `two_break_on_genome`)

- **`genome_rearrangement/fragile_regions.py`**: Re-exports of genome graph functions
  - Provides backward compatibility for original FragileRegions.py functions
  - Functions are now properly organized in utils/ but accessible here

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
from genome_rearrangement import two_break_on_genome

# Define genome structure
genome = [
    [1, 2, 3, 4],     # Chromosome 1
    [-5, 6, -7]       # Chromosome 2 (negative indicates reverse orientation)
]

# Perform two-break rearrangement (with valid parameters)
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

## Educational Value

This repository serves as an excellent educational resource for:
- **Algorithm Implementation**: Learn how bioinformatics algorithms work internally
- **Computational Biology**: Understand the computational aspects of biological problems
- **Python Programming**: See examples of clean, modular scientific code
- **Software Design**: Study well-structured bioinformatics software architecture

## Refactoring Notes

This repository has been refactored from its original structure to improve:
- **Code Organization**: Moved from monolithic files to modular packages
- **Naming Consistency**: Standardized function names to Python conventions
- **Documentation**: Added comprehensive docstrings and examples
- **Maintainability**: Clear separation of concerns and reusable components

The original `FragileRegions.py` contained basic genome graph operations (not actual fragile regions analysis). These functions have been moved to `utils/genome_graph.py` and are re-exported through `genome_rearrangement/fragile_regions.py` for backward compatibility.

## Contributing

When contributing to this repository:
1. Follow the existing code style and documentation patterns
2. Add comprehensive docstrings to all functions and classes
3. Include example usage in docstrings
4. Update this README if adding new modules or changing the structure
5. Ensure all code works with Python 3.7+ and standard library only

## License

This project is designed for educational and research purposes. Please ensure proper attribution when using this code in academic work or research publications.

---

*For questions, issues, or contributions, please refer to the repository's issue tracker or contact the maintainers.*
