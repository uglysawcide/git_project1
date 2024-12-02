import sys, random

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button1.clicked.connect(self.paint)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.paint(qp)
        qp.end()

    def paint(self, qp):
        qp = QPainter()
        qp.begin(self)
        size = self.size()
        x = random.randint(1, size.width() - 1)
        y = random.randint(1, size.height() - 1)
        diametr = random.randint(1, 500)
        qp.drawEllipse(x, y, diametr, diametr)
        qp.end()


def exception_hook(exctype, value, traceback):
    QMessageBox.critical(None, "Критическая ошибка", f"Type: {exctype}\nValue: {value}\nTraceback: {traceback}")


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
