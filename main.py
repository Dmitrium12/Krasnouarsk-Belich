import random
import sys
from PyQt5.QtCore import Qt
from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.color_mass = [Qt.yellow, Qt.green, Qt.red, Qt.blue, Qt.black, Qt.cyan]
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            qp.setPen(QPen(random.choice(self.color_mass),  8, Qt.SolidLine))
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
