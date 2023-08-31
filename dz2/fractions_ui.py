"""
Потому что если проблем нет то их себе нужно создать!


# https://forum.qt.io/topic/36442/retrieving-the-text-from-qlineedit
# https://habr.com/ru/companies/skillfactory/articles/599599/
"""

from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fractions calc")
        self.b_eval = QPushButton("eval")
        self.label = QLabel()
        self.b_eval.setCheckable(True)
        self.b_eval.clicked.connect(self.f_eval)
        self.i_first = QLineEdit()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.i_first)
        self.layout.addWidget(self.b_eval)
        self.layout.addWidget(self.label)

        structure = QWidget()
        structure.setLayout(self.layout)
        self.setCentralWidget(structure)

    def f_eval(self):
        print("1:",self.i_first.text())
        self.label.setText(f"{self.i_first.text()} = {None} ")
def main():
    core = QApplication([])
    window = MainWindow()
    window.show()
    core.exec()

if __name__ == '__main__':
    main()