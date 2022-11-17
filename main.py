import random
import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            qp.setPen(QPen(Qt.yellow,  8, Qt.SolidLine))
            chislo = random.randint(100, 400)
            qp.drawEllipse(40, 40, chislo, chislo)
            qp.end()

    def run(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
