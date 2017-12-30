import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon


class practice1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Practice1')
        self.setWindowIcon(QIcon('sheikah.png'))
        self.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    instant = practice1()
    sys.exit(app.exec_())