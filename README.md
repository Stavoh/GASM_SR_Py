# Genome Assembly From Short Reads With Python
## Plan
DNA sequencing involves cutting a long string of DNA and reading it in small pieces due to biological limitations. This results in many different short DNA reads.  
Here, a tool that constructs the probable sequence of a DNA string from the short reads that result from the biological part of the sequencing will be developed.  
Python will be used to construct a de Bruijn graph and find its Eulerian cycle to predict the most probable sequence.  
### Layout
1. DNA sequencing data in the form of a FASTQ file will be used as an input.  
2. The most probable sequence will be computed by the program.  
3. The predicted sequence will be given in the form of a text file as an output.  


# Genome Assembly from Short Reads with Python

## Project Overview
This project assembles a long DNA sequence from short DNA reads produced by sequencing technologies. Using computational methods, it:

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

## Input and Output

### Input
- **FASTQ File**: The input file should contain DNA sequencing reads in the FASTQ format, which includes:
  - Sequence headers.
  - DNA sequences.
  - Quality scores (ignored in this implementation).

### Output
- **Text File**: The reconstructed DNA sequence is saved as a text file in the same directory as the input FASTQ file. The file name includes a timestamp for uniqueness.

---

## Installation

### Prerequisites
- Python **3.7+** installed on your system.

### Clone the Repository
```bash
git clone https://github.com/your-username/genome-assembly.git
cd genome-assembly
```

### Install Dependencies
If a `requirements.txt` file is included:
```bash
pip install -r requirements.txt
```

If not, install the required library manually:
```bash
pip install argparse
```

---

## Usage

### Running the Program
1. Prepare your input FASTQ file.
2. Run the program from the command line:
   ```bash
   python genome_assembly.py <path_to_fastq_file>
   ```
3. The output file with the reconstructed DNA sequence will appear in the same directory as the input file.

### Example
```bash
python genome_assembly.py data/sample.fastq
```
Output:
```
DNA sequence saved to: data/sample_Sequence_1672531200.txt
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
