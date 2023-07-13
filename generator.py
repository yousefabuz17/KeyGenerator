import sys

from random import sample
from string import ascii_letters, digits, punctuation
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit

class Gen:
    def __init__(self):
        self._all_chars = [i for i in (ascii_letters + digits + punctuation) * 100] #9400 total chars

    key_gen = lambda self, length: ''.join(sample(self._all_chars, 9400)[:length])
    pat_gen = lambda self, length: ''.join(sample(self._all_chars, 6200)[:length]).translate(str.maketrans(punctuation, ' '*len(punctuation))).replace(' ', '')

class GenGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key Generator GUI")
        self.initUI()

    def initUI(self):
        key_gen_label = QLabel("Key Generator (Max Output: 9400 in length)\nDefault Length: 64")
        self.key_gen_input = QLineEdit()
        self.key_gen_output = QTextEdit()
        self.key_gen_output.setReadOnly(True)

        pat_label = QLabel("Personal Access Token (Max Output: 6200 in length)\nDefault Length: 52")
        self.pat_input = QLineEdit()
        self.pat_output = QTextEdit()
        self.pat_output.setReadOnly(True)

        self.key_gen_button = QPushButton("Generate Key")
        self.key_gen_button.clicked.connect(self.run_key_gen)

        self.pat_button = QPushButton("Generate Personal Access Token")
        self.pat_button.clicked.connect(self.run_pat_gen)

        layout = QVBoxLayout()
        layout.addWidget(key_gen_label)
        layout.addWidget(self.key_gen_input)
        layout.addWidget(self.key_gen_button)
        layout.addWidget(self.key_gen_output)
        layout.addWidget(pat_label)
        layout.addWidget(self.pat_input)
        layout.addWidget(self.pat_button)
        layout.addWidget(self.pat_output)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.key_gen_input.returnPressed.connect(self.run_key_gen)
        self.pat_input.returnPressed.connect(self.run_pat_gen)

    def run_key_gen(self):
        try:
            key_length = int(self.key_gen_input.text()) if self.key_gen_input.text().strip() else 64 #Default length
            generated_key = Gen().key_gen(key_length)
            self.key_gen_output.setPlainText(generated_key)
        except ValueError:
            self.key_gen_output.setPlainText('Integers only')

    def run_pat_gen(self):
        try:
            pat_length = int(self.pat_input.text()) if self.pat_input.text().strip() else 52 #Default length
            generated_pat = Gen().pat_gen(pat_length)
            self.pat_output.setPlainText(generated_pat)
        except ValueError:
            self.key_gen_output.setPlainText('Integers only')

def main():
    app = QApplication(sys.argv)
    window = GenGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()