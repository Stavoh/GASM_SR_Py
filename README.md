# Genome Assembly from Short Reads with Python

---


## Overview
DNA sequencing involves cutting a long string of DNA and reading it in small pieces due to biological limitations. This results in many different short DNA reads.  
GASM is a tool that assembles a long DNA sequence from short DNA reads produced by sequencing technologies. Using computational methods, it:

- Constructs a **de Bruijn graph** from k-mers of the input DNA fragments.
- Traverses the graph to find an **Eulerian cycle**, predicting the most probable sequence.
- Outputs the reconstructed DNA sequence as a text file.

This tool is ideal for genome assembly tasks in bioinformatics and computational biology.

### Layout
1. DNA sequencing data in the form of a FASTQ file will be used as an input.  
2. The most probable sequence will be computed by the program.  
3. The predicted sequence will be given in the form of a text file as an output.  


---

## Background

### Genome Assembly

In bioinformatics, genome assembly refers to aligning and merging fragments from a longer DNA sequence in order to reconstruct the original sequence. This is needed as DNA sequencing technology like Illumina, PacBio, or Oxford Nanopore might not be able to 'read' whole genomes in one go, but rather reads small pieces of between 20 and 30,000 bases, depending on the technology used.

The problem of genome assembly can be compared to taking many copies of a book, passing each of them through a shredder with a different cutter, and piecing the text of the book back together just by looking at the shredded pieces.

There are two main types of genome assembly, from which GASM implements the first (de novo assembly):

**1. De Novo Assembly:**  
De novo assembly is the process of piecing together short reads of DNA into a whole genome without a reference genome.

**2. Reference-Based Assembly:**  
Reference-based assembly is the process of mapping short reads to an existing reference genome.

### Applications of Genome Assembly

Genome assembly plays a vital role in many fields of biology and medicine, including:

- **Genetic Research**: Understanding the genetic makeup of organisms to identify genes, mutations, and regulatory elements.
- **Personalized Medicine**: Genomic information is used to tailor treatments based on an individual's genetic makeup.
- **Evolutionary Studies**: Comparing the genomes of different species to understand evolutionary relationships.
- **Agriculture**: Developing crop varieties with desirable traits by studying the genomes of plants and animals.

### Role of Graph Theory in De Novo Genome Assembly
To tackle the assembly problem, computational methods leverage graph theory. This project employs a de Bruijn graph approach, where:
- Nodes represent \(k-1\) prefixes and suffixes of \(k\)-mers, substrings of DNA of length \(k\).
- Directed edges connect overlapping \(k\)-mers, capturing the structure of the DNA sequence.

The task then reduces to finding an Eulerian cycle—a path that visits every edge exactly once—within this graph. This cycle represents the reconstructed DNA sequence.

---

## Code Features

### Input

- **FASTQ File Parsing:**  
Reads DNA sequences from a FASTQ file, which includes:
  - Sequence headers.
  - DNA sequences.
  - Quality scores.  

  *_Sample FASTQ files are given in this repository._

### Processing

- **Reverse Complement Calculation:**  
Generates reverse complements for DNA sequences.  

- **k-mer Generation:**  
Generates all k-mers (substrings of length k) from the short DNA sequences.  

- **De Bruijn Graph Construction:**  
Constructs a de Bruijn graph from the k-mers.  

- **Eulerian Cycle Detection:**  
Finds an Eulerian cycle in the graph.  

- **DNA Sequence Assembly:**  
Assembles the superstring from the Eulerian cycle.

### Output

- **Text File:**  
The reconstructed DNA sequence can be saved as a text file.

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
1. Run the program from the command line:
   ```bash
   python GASM.py
   ```
2. Choose file to process or to unzip.
3. Save the output file with the reconstructed DNA sequence.

### Output Example
<img width="659" alt="Screenshot 2025-01-13 at 10 25 01" src="https://github.com/user-attachments/assets/0c238aa2-b009-45e8-b5b0-d6b8f7342b7e" />

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
This project was created as part of the [WIS Python programming course](https://github.com/szabgab/wis-python-course-2024-11.git)
