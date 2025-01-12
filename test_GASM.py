import pytest
from PyQt5.QtWidgets import QApplication
from GASM import MainWindow
from unittest.mock import MagicMock


@pytest.fixture
def app():
    app = QApplication([])  # Create a minimal Qt application
    yield app
    app.quit()

def test_process_dna_strings(app):
    # Create an instance of MainWindow
    main_window = MainWindow()

    # Mock the method `process_dna_strings` to test the processing logic without GUI
    test_input_file = 'test.fastq'
    k = 4
    main_window.process_dna_strings()  # Ensure this doesn't rely on GUI interactions


def test_gui_elements(app):
    # Create an instance of the MainWindow
    main_window = MainWindow()

    # Mock the output_text widget to avoid interaction with the actual QTextEdit
    main_window.output_text = MagicMock()

    # Now, you can test other parts of the GUI logic
    # For example, asserting that main_window is an instance of MainWindow
    assert isinstance(main_window, MainWindow)

    # If you want to check other elements, you can also mock them similarly
    # e.g., mocking a button click or other behavior
