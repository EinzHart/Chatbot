import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt



class practice2(QWidget):
    is_transparent = False

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Practice2')
        self.setWindowIcon(QIcon('sheikah.png'))
        self.setAttribute(Qt.WA_TranslucentBackground)

        btn = QPushButton('button1', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.set_transparent)
        btn.move(50, 100)



    def set_transparent(self):
        if self.is_transparent:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAutoFillBackground(False)
            self.show()
        else:
            self.setWindowFlag(Qt.FramelessWindowHint, False)
            self.setAttribute(Qt.WA_NoSystemBackground, False)
            self.show()

        self.setAttribute(Qt.WA_TranslucentBackground, self.is_transparent)
        self.is_transparent = ~self.is_transparent
        self.repaint()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    instant = practice2()
    instant.show()
    sys.exit(app.exec_())