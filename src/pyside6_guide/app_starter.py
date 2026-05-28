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
    QHBoxLayout,
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
        self.resize(450, 300)

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
        input2_layout = QHBoxLayout()
        self.label2 = QLabel("Second Number:")
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Enter a number")
        input1_layout.addWidget(self.label2)
        input1_layout.addWidget(self.input2)

        # Operation dropdown
        operation_layout = QHBoxLayout()
        self.operation_label = QLabel("Operation")
        self.operation_box = QComboBox()
        self.operation_box.addItems(["+", "-", "*", "/"])
        operation_layout.addWidget(self.operation_label)
        operation_layout.addWidget(self.operation_box)

        # Buttons
        button_layout = QHBoxLayout()

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.clear_inputs)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_inputs)

        button_layout.addWidget(self.calculate_button)
        button_layout.addWidget(self.clear_button)

        layout.addWidget(self.title_label)
        layout.addWidget(self.output_label)

        layout.addLayout(input1_layout)
        layout.addLayout(input2_layout)
        layout.addLayout(operation_layout)
        layout.addLayout(button_layout)

        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def calculate(self):
        num1_text = self.input1.text()
        num2_text = self.input2.text()
        operation = self.operation_box.currentText()

        if num1_text == "" or num2_text == "":
            self.output_label.setText("Error: Please fill in both number boxes.")
            return
        
        try:
            num1 = float(num1_text)
            num2 = float(num2_text)
        except ValueError:
            self.output_label.setText(
                "Error: Only numbers are allowed. No letters or symbols."
            )
            return
        
        try:
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2 
            elif operation == "/":
                if num2 == 0:
                    self.output_label.setText("Error: Cannot divide by zero.")
                    return
                result = num1 / num2

            self.output_label.setText(f"Result: {result}")

        except Exception:
            self.output_label.setText("Error: Something went wrong.")

    def clear_inputs(self):
        self_input1.clear()
        self_input2.clear()

        self.output_label.setText(
            "Enter two numbers, choose an operation, and click calculate."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()