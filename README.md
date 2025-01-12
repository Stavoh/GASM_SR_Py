# Genome Assembly from Short Reads with Python

## Overview
This tool assembles a long DNA sequence from short DNA reads produced by sequencing technologies. Using computational methods, it:

- Constructs a **de Bruijn graph** from the input DNA fragments (k-mers).
- Traverses the graph to find an **Eulerian cycle**, predicting the most probable sequence.
- Outputs the reconstructed DNA sequence as a text file.

This tool is ideal for genome assembly tasks in bioinformatics and computational biology.

---

## Features
1. **Input**: Accepts DNA sequencing data in FASTQ format.
2. **Processing**:
   - Generates k-mers.
   - Builds a de Bruijn graph.
   - Identifies an Eulerian cycle.
3. **Output**: Saves the reconstructed DNA sequence to a text file.

---

## Input
- **FASTQ File**: The input file should contain DNA sequencing reads in the FASTQ format, which includes:
  - Sequence headers.
  - DNA sequences.
  - Quality scores.
  Sample FASTQ files are given in this repository.

## Output
- **Text File**: The reconstructed DNA sequence is saved as a text file in the same directory as the input FASTQ file.

---

## Installation

### Prerequisites
- Python **3.7+** installed on your system.

### Clone the Repository
```bash
git clone https://github.com/Stavoh/GASM_SR_Py.git
cd GASM_SR_Py
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Running the Program
1. Prepare your input FASTQ file. Sample files can be found in the current repository.
2. Run the program from the command line:
   ```bash
   python GASM.py <path_to_fastq_file>
   ```
4. The output file with the reconstructed DNA sequence will appear in the same directory as the input file.

### Example
```bash
python GASM.py Sample1.fastq
```
Output:
```
DNA sequence saved to: data/Sample1_Sequence_1672531200.txt
```

---

## Testing

### Running Tests
If test scripts are included:
```bash
pytest
```
Or run a specific test script:
```bash
python test_genome_assembly.py
```

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
