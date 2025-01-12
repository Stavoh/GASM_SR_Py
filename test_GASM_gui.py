# test_GASM_gui_interactions.py
from pytestqt import qtbot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt

def test_button_click(qtbot):
    window = QMainWindow()
    button = QPushButton('Click Me', window)
    label = QLabel('', window)
    window.setCentralWidget(button)
    button.clicked.connect(lambda: label.setText('Button Clicked!'))
    
    qtbot.addWidget(window)
    
    qtbot.mouseClick(button, Qt.LeftButton)
    
    assert label.text() == 'Button Clicked!'

def test_input_field(qtbot):
    window = QMainWindow()
    input_field = QLineEdit(window)
    input_field.setText("31")
    assert input_field.text() == "31"
