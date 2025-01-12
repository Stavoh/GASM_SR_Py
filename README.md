# Genome Assembly from Short Reads with Python

## Overview
This tool assembles a long DNA sequence from short DNA reads produced by sequencing technologies. Using computational methods, it:

- Constructs a **de Bruijn graph** from the input DNA fragments (k-mers).
- Traverses the graph to find an **Eulerian cycle**, predicting the most probable sequence.
- Outputs the reconstructed DNA sequence as a text file.

This tool is ideal for genome assembly tasks in bioinformatics and computational biology.

---

## Background

### Genome Assembly

In bioinformatics, genome assembly refers to aligning and merging fragments from a longer DNA sequence in order to reconstruct the original sequence. This is needed as DNA sequencing technology like Illumina, PacBio, or Oxford Nanopore might not be able to 'read' whole genomes in one go, but rather reads small pieces of between 20 and 30,000 bases, depending on the technology used.

The problem of genome assembly can be compared to taking many copies of a book, passing each of them through a shredder with a different cutter, and piecing the text of the book back together just by looking at the shredded pieces.

There are two main types of genome assembly, from which we are implementing the first (de novo assembly):

### 1. **De Novo Assembly**
De novo assembly is the process of assembling a genome without a reference genome. It involves piecing together short DNA reads into longer contigs, which are then further assembled into scaffolds. This approach is used when a reference genome is unavailable or when studying novel organisms. This approach is implemented by this tool.

- **Tools**: Velvet, SPAdes, ABySS, SOAPdenovo
- **Challenges**: Complexity increases with genome size, repeat sequences, and the quality of the reads.

### 2. **Reference-Based Assembly**
In reference-based assembly, short reads are mapped to an existing reference genome. This approach is used when a closely related genome is available, making it faster and more efficient than de novo assembly.

- **Tools**: BWA, Bowtie, STAR, HISAT2
- **Challenges**: Variations like structural differences, mutations, and indels might not be captured as accurately.

## Applications of Genome Assembly

Genome assembly plays a vital role in many fields of biology and medicine, including:

- **Genetic Research**: Understanding the genetic makeup of organisms to identify genes, mutations, and regulatory elements.
- **Personalized Medicine**: Genomic information is used to tailor treatments based on an individual's genetic makeup.
- **Evolutionary Studies**: Comparing the genomes of different species to understand evolutionary relationships.
- **Agriculture**: Developing crop varieties with desirable traits by studying the genomes of plants and animals.

---

uses k-mers for building the initial de Bruijn graph and on following stages it performs graph-theoretical operations which are based on graph structure, coverage and sequence lengths














Genome assembly is a critical process in bioinformatics where fragmented DNA sequences, generated by sequencing technologies, are computationally pieced together to reconstruct the original long DNA molecule. This process is foundational in understanding genetic information, enabling applications such as disease research, evolutionary studies, and synthetic biology.

Modern DNA sequencing technologies, such as Illumina and Oxford Nanopore, generate vast amounts of short DNA fragments, or reads, because reading entire genomes directly is not feasible due to biological and technical constraints. These reads overlap, making it possible to detect the original sequence.

### Role of Graph Theory in Genome Assembly
To tackle the assembly problem, computational methods leverage graph theory. This project employs a de Bruijn graph approach, where:
- Nodes represent \(k-1\) prefixes and suffixes of \(k\)-mers, substrings of DNA of length \(k\).
- Directed edges connect overlapping \(k\)-mers, capturing the structure of the DNA sequence.

The task then reduces to finding an Eulerian cycle—a path that visits every edge exactly once—within this graph. This cycle represents the reconstructed DNA sequence.

## Code Features

### Input

**FASTQ File Parsing:**
Reads DNA sequences from a FASTQ file, which includes:
  - Sequence headers.
  - DNA sequences.
  - Quality scores.
*_Sample FASTQ files are given in this repository._

**Command-Line Input:**
Allows file path input via the command line.

### Processing

**Reverse Complement Calculation:**
Generates reverse complements for DNA sequences.
**k-mer Generation:**
Generates all k-mers (substrings of length 
k) from a DNA sequence.
**De Bruijn Graph Construction:**
Constructs a de Bruijn graph from the k-mers.
**Eulerian Cycle Detection:**
Finds an Eulerian cycle in the graph.
**DNA Sequence Assembly:**
Assembles the superstring from the Eulerian cycle.

### Output

**Text File**:
The reconstructed DNA sequence is saved as a text file in the same directory as the input FASTQ file.

---

## Installation

### Prerequisites
- Python 3.7 or newer installed on your system.

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
```bash
pytest
```

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Mentions
This tool was created as part of the [WIS Python programming course](https://github.com/szabgab/wis-python-course-2024-11.git)
