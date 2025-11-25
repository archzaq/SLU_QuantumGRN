# slugrn (Quantum Gene Regulatory Networks)

A quantum circuit model for inferring gene regulatory networks (GRNs) from single-cell transcriptomic data. Originally published as QuantumGRN in [Nature npj Quantum Information](https://www.nature.com/articles/s41534-023-00740-6).

## Overview

We introduce a quantum circuit model for inferring gene regulatory networks from single-cell transcriptomic data. The model employs qubit entanglement to simulate interactions between genes, resulting in competitive performance and promising potential for further exploration. 

Our quantum GRN modeling approach has been applied to single-cell transcriptomic data from human lymphoblastoid cells, focusing on genes involved in innate immunity regulation. The quantum circuit model successfully predicts the presence and absence of regulatory interactions between genes while estimating interaction strengths.

Quantum computing in biology has the potential to provide better understanding of single-cell GRNs by more effectively modeling fully interconnected gene relationships compared to conventional statistical methods like correlation and regression.

## Installation

### Prerequisites

**System Dependencies (required for network visualization):**

For full visualization support including network graphs, you need the Cairo graphics library:

**macOS:**
```bash
brew install cairo pkg-config
```

### Python Environment Setup

Python 3.8+ is required (tested on Python 3.13):
```bash
# Create a virtual environment (recommended)
python3 -m venv ~/slugrn-env
source ~/slugrn-env/bin/activate  # On Windows: slugrn-env\Scripts\activate

# Or using conda
conda create -n slugrn python=3.10
conda activate slugrn
```

### Install slugrn

**From source:**
```bash
git clone https://github.com/archzaq/QuantumGRN.git
cd QuantumGRN
pip install .
```

**Note:** If you skip the Cairo installation, the package will work but network visualization (`draw_network`) will fail. All quantum circuit analysis and other visualizations will function normally.

## Quick Start

### Run Example
```bash
cd test
python 02_example.py
```

This will:
- Load single-cell gene expression data
- Train a quantum circuit model on 6 genes
- Generate visualizations including circuit diagrams and distribution plots
- Output results as SVG files

### Basic Usage
```python
import numpy as np
import pandas as pd
from slugrn import *

# Load gene expression data
df = pd.read_csv("dataset/expr_matrix_pearsonresidual_7.txt", delimiter='\t')
df = df.set_index('genes').T
ncells, ngenes = df.shape

# Prepare data
df = qsc_order_gene(df)
genes = df.columns.to_list()
p_obs = qsc_distribution(df)
activation = qsc_activation_ratios(df)

# Initialize quantum circuit parameters
theta = theta_init(genes, activation_ratios=activation)
edges = edges_init(genes)

# Create and train the quantum GRN model
qgrn = slugrn_model(ncells, genes, theta, edges, p_obs)
qgrn.train()

# Run quantum simulation
p_qiskit = qgrn.run_qiskit(filename="circuit.svg")

# Visualize the gene regulatory network
draw_network(genes, edges, qgrn.theta, filename="network.svg")
```

## Features

- **Quantum Circuit Modeling**: Uses quantum entanglement to model gene-gene interactions
- **Single-Cell Data Support**: Optimized for single-cell transcriptomic datasets
- **Network Inference**: Predicts regulatory relationships and interaction strengths
- **Visualization Suite**: 
  - Quantum circuit diagrams
  - Gene regulatory network graphs
  - Distribution comparisons (observed vs. predicted)
  - Statistical plots

## Output Files

When you run the examples, several visualization files are generated:

- `*_circuit.svg` - Quantum circuit representation
- `*_network.svg` - Gene regulatory network topology
- `*_p_obs.svg` - Observed gene activation distribution
- `*_comparison_*.svg` - Comparison plots between observed and predicted distributions

## Examples and Tutorials

- `test/` - Quick example scripts demonstrating core functionality
- `tutorial/` - Detailed Jupyter notebooks with step-by-step explanations
- `dataset/` - Example single-cell expression data

## Technical Details

**Key Components:**
- Quantum circuit initialization with gene-specific parameters
- Optimization using gradient descent to match observed distributions
- Qiskit integration for quantum simulation
- Network analysis using igraph

**Dependencies:**
- qiskit >= 0.37.0
- qiskit-aer >= 0.10.4
- numpy >= 1.23.0
- pandas >= 1.4.3
- matplotlib >= 3.5.2
- scipy >= 1.8.1
- igraph >= 0.9.11
- pycairo >= 1.21.0

## Citation

If you use this software in your research, please cite:
```
Nature npj Quantum Information (2023)
https://www.nature.com/articles/s41534-023-00740-6
```

## Contributing

Go for it!

## Troubleshooting

**Import errors with qiskit:**
- Make sure you have qiskit-aer installed: `pip install qiskit-aer`

**Network visualization fails:**
- Install Cairo system libraries (see Prerequisites)
- Alternatively, comment out `draw_network()` calls to skip network plots

**Python version issues:**
- slugrn requires Python 3.8 or higher
- Tested and working on Python 3.13

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Maintainer

Zac Reeves - [GitHub](https://github.com/archzaq)

## Acknowledgments

Based on the original QuantumGRN research published in Nature npj Quantum Information.
