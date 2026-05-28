"""
app_starter.py
by Valerie Lee
A bare bones starter code to begin with.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QComboBox,
)
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window psetup
        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(400, 300)

        # Main layout
        layout = QVBoxLayout()

        # Title
        self.title_label = QLabel("Simple Calculator")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.output_label = QLabel(
            "Enter two numbers, choose an operation, and click Calculate."
        )

        # First number input
        input1_layout = QHBoxLayout()
        self.label1 = QLabel("First Number:")
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Enter a number")
        input1_layout.addWidget(self.label1)
        input1_layout.addWidget(self.input1)
        
        # Second number input
        input1_layout = QHBoxLayout()
        self.label2 = QLabel("First Number:")
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Enter a number")
        input1_layout.addWidget(self.label2)
        input1_layout.addWidget(self.input2)

        # Operation dropdown
        operation_layout = QHBoxLayout()
        self.operation_label = QLabel("Operation")
        self.operation_box = QComboBox()
        self.operation_box.adjustment(["+", "-", "*", "/"])
        operation_layout.addWidget(self.operation_label)
        operation_layout.addWidget(self.operation_box)

        # add widgets & layouts to main layout
        layout.addWidget(title_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()