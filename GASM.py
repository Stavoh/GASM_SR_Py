import sys
import gzip
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QLineEdit, QFileDialog, QTextEdit, QLabel, QProgressBar, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal

# Helper functions for genome assembly
def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def generate_kmers(s, k):
    return [s[i:i+k] for i in range(len(s) - k + 1)]

def de_bruijn_graph(kmers):
    graph = {}
    for kmer in kmers:
        prefix, suffix = kmer[:-1], kmer[1:]
        if prefix not in graph:
            graph[prefix] = []
        graph[prefix].append(suffix)
    return graph

def find_eulerian_cycle(graph):
    stack = []
    path = []
    current_node = list(graph.keys())[0]
    stack.append(current_node)

    while stack:
        if current_node in graph and graph[current_node]:
            stack.append(current_node)
            current_node = graph[current_node].pop()
        else:
            path.append(current_node)
            current_node = stack.pop()
    
    return path[::-1]

def read_fastq(file_path):
    with open(file_path, 'r') as f:
        dna_strings = []
        while True:
            header = f.readline()
            if not header:  # End of file
                break
            sequence = f.readline().strip()
            f.readline()  # Skip "+" line
            f.readline()  # Skip quality scores
            dna_strings.append(sequence)
    return dna_strings

def solve_dna_strings(dna_strings, k):
    kmers = []
    for s in dna_strings:
        kmers.extend(generate_kmers(s, k))
        kmers.extend(generate_kmers(reverse_complement(s), k))
    
    # Construct the de Bruijn graph
    graph = de_bruijn_graph(kmers)
    
    # Find the Eulerian cycle
    cycle = find_eulerian_cycle(graph)
    
    # Construct the superstring from the cycle
    superstring = cycle[0]
    for i in range(1, len(cycle)):
        superstring += cycle[i][-1]
    
    return superstring


# Threaded class for decompressing to keep UI responsive
class DecompressThread(QThread):
    progress_updated = pyqtSignal(int)
    decompression_done = pyqtSignal(str)

    def __init__(self, file_path, output_path):
        super().__init__()
        self.file_path = file_path
        self.output_path = output_path

    def run(self):
        try:
            total_size = os.path.getsize(self.file_path)
            bytes_written = 0
            chunk_size = 1024 * 1024  # 1MB per chunk

            with gzip.open(self.file_path, 'rb') as f_in:
                with open(self.output_path, 'wb') as f_out:
                    while chunk := f_in.read(chunk_size):
                        f_out.write(chunk)
                        bytes_written += len(chunk)
                        self.progress_updated.emit(bytes_written)
            self.decompression_done.emit(f"Decompression completed. File saved as {self.output_path}")
        except Exception as e:
            self.decompression_done.emit(f"Error during decompression: {str(e)}")


# GUI Application with both tabs
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genome Assembly Tool")

        # Set up the tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Create both tabs
        self.assembly_tab = QWidget()  # Genome Assembly Tab
        self.decompression_tab = QWidget()  # Decompression Tab

        # Add tabs to the widget (Assembly Tab first, Decompression Tab second)
        self.tabs.addTab(self.assembly_tab, "Genome Assembly")
        self.tabs.addTab(self.decompression_tab, "Decompress GZ File")

        # Initialize both tabs
        self.init_assembly_tab()
        self.init_decompression_tab()

    def init_decompression_tab(self):
        layout = QVBoxLayout()

        # Button to select file and start decompression
        self.decompress_button = QPushButton("Choose and Decompress File")
        self.decompress_button.clicked.connect(self.select_file_to_decompress)
        layout.addWidget(self.decompress_button)

        # Status label to show decompression status
        self.status_label = QLabel("Select a .gz file to decompress")
        layout.addWidget(self.status_label)

        # Progress bar for decompression
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.decompression_tab.setLayout(layout)

    def init_assembly_tab(self):
        layout = QVBoxLayout()

        # Label
        self.label = QLabel('Select a FASTQ file and input k-mer size', self)
        layout.addWidget(self.label)

        # File selection button
        self.file_button = QPushButton('Choose FASTQ File', self)
        self.file_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.file_button)

        # K-mer size input
        self.kmer_input = QLineEdit(self)
        self.kmer_input.setPlaceholderText("Enter k-mer size (if you are not sure, enter 31)")
        layout.addWidget(self.kmer_input)

        # Process button
        self.process_button = QPushButton('Process DNA Strings', self)
        self.process_button.clicked.connect(self.process_dna_strings)
        layout.addWidget(self.process_button)

        # Output text area
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # Save button
        self.save_button = QPushButton('Save Output', self)
        self.save_button.clicked.connect(self.save_output)
        layout.addWidget(self.save_button)

        self.assembly_tab.setLayout(layout)

    def open_file_dialog(self):
        # Open file dialog to choose FASTQ file
        options = QFileDialog.Options()
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select FASTQ File", "", "FASTQ Files (*.fastq);;All Files (*)", options=options)
        if self.file_path:
            self.label.setText(f"Selected file: {os.path.basename(self.file_path)}")

    def process_dna_strings(self):
        # Get the k-mer size from input
        try:
            k = int(self.kmer_input.text())
        except ValueError:
            self.output_text.setText("Please enter a valid integer for k-mer size.")
            return

        # Read the FASTQ file
        dna_strings = read_fastq(self.file_path)

        # Solve the problem
        result = solve_dna_strings(dna_strings, k)

        # Display the result in the output text area
        self.output_text.setText(result)

    def save_output(self):
        # Save the output sequence to a text file
        output_file, _ = QFileDialog.getSaveFileName(self, "Save Output", "", "Text Files (*.txt);;All Files (*)")
        if output_file:
            with open(output_file, "w") as f:
                f.write(self.output_text.toPlainText())
            self.output_text.append(f"\nDNA sequence saved to: {output_file}")

    def select_file_to_decompress(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select .gz File", "", "GZ Files (*.gz)")
        if file_path:
            # Create the output file path by removing '.gz'
            output_path = file_path.rstrip('.gz')
            self.decompress_file(file_path, output_path)

    def decompress_file(self, file_path, output_path):
        self.status_label.setText("Decompressing... Please wait.")
        self.progress_bar.setValue(0)

        self.decompress_thread = DecompressThread(file_path, output_path)
        self.decompress_thread.progress_updated.connect(self.update_progress)
        self.decompress_thread.decompression_done.connect(self.decompression_done)
        self.decompress_thread.start()

    def update_progress(self, bytes_written):
        self.progress_bar.setValue(bytes_written)

    def decompression_done(self, message):
        self.status_label.setText(message)
        QMessageBox.information(self, "Decompression Status", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
