# Genome Assembly From Short Reads With Python
## Abstract
DNA sequencing involves cutting a long string of DNA and reading it in small pieces due to biological limitations. This results in many different short DNA reads.\n
Here, a tool that constructs the probable sequence of a DNA string from the short reads that result from the biological part of the sequencing will be developed.
Python will be used to construct a de Bruijn graph and find its Eulerian cycle to predict the most probable sequence.
### Plan Layout
1. DNA sequencing data in the form of a FASTQ file will be used as an input.
2. The most probable sequence will be computed by the program.
3. The predicted sequence will be given in the form of a text file as an output.
