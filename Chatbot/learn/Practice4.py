import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPainter, QColor, QFont, QBrush
from PyQt5.QtCore import Qt, pyqtSignal, QObject

class Communicate(QObject):
    reopen = pyqtSignal()

class neu_window(QWidget):
    def __init__(self, c) -> object:
        super().__init__()
        self.init_UI()
        self.c = c
    def init_UI(self):
        #self.setWindowFlag()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('button test')
        self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setWindowOpacity(0.1)




    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()
            self.c.reopen.emit()

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.transparent)
        qp.setOpacity(0.3)
        qp.setBrush(Qt.cyan)
        qp.drawRect(self.rect())
        qp.setPen(Qt.black)
        qp.setOpacity(1)
        qp.setFont(QFont('BigNoodleTooOblique', 30))
        qp.drawText(self.rect(), Qt.AlignLeft, 'testt')

        qp.end()


class practice4(QMainWindow):
    is_transparent = False

    def __init__(self):
        super().__init__()
        self.init_UI()


    def init_UI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Practice3')
        self.setWindowIcon(QIcon('sheikah.png'))
        #self.setAttribute(Qt.WA_TranslucentBackground)

        self.c = Communicate()
        self.c.reopen.connect(self.show)

        self.btn = QPushButton('button1', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.new_window)
        self.btn.move(50, 100)

    def new_window(self):
        self.wind = neu_window(self.c);
        self.wind.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    instant = practice4()
    instant.show()
    sys.exit(app.exec_())