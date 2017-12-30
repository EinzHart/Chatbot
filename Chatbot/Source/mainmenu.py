import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIcon, QPainter, QColor, QFont, QBrush
from PyQt5.QtCore import Qt, pyqtSignal, QObject

class mainmenu(QMainWindow):
    def __init__(self):
        super().__init__()
        # variables
        self.channel_name = 'einzhart'
        self.nickname = 'einzhart'
        self.server_name = 'irc.chat.twitch.tv'
        self.server_port = 6667
        self.client_token = 'oauth:tzkaxwnvm3si38sz8davspeijz00p6'

        #buttons and Labels
        self.btn_SetConnection = QPushButton("connection setting", self)
        self.btn_SetChatbox = QPushButton("chatbox preference", self)
        self.btn_InitConnect = QPushButton("Connect!", self)
        self.btn_About = QPushButton("About..",self)

        self.lbl_channel = QLabel()
        self.lbl_nickname = QLabel()


        self.init_UI()

    def init_UI(self):
        #window
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle("EZHT's chatbox")
        self.setWindowIcon(QIcon("sheikah.png"))

        #labels
        #channel
        self.lbl_channel.resize(self.lbl_channel.sizeHint())
        self.lbl_channel.setAlignment(Qt.AlignLeft)
        #nickname
        self.lbl_nickname.resize(self.lbl_nickname.sizeHint())
        self.lbl_nickname.setAlignment(Qt.AlignLeft)
        #buttons
        #SetConnection
        self.btn_SetConnection.resize(self.btn_SetConnection.sizeHint())

        #SetChatbox
        self.btn_SetChatbox.resize(self.btn_SetChatbox.sizeHint())

        #InitConnect
        self.btn_InitConnect.resize(self.btn_InitConnect.sizeHint())

        #About
        self.btn_About.resize(self.btn_About.sizeHint())

        #labels
        self.lbl_channel.setText('channel:' + self.channel_name)

        self.lbl_nickname.setText('nickname:' + self.nickname)


        #Layouts
        layout_anchor = QWidget()
        vertlayout = QVBoxLayout(layout_anchor)
        vertlayout.addWidget(self.lbl_nickname)
        vertlayout.addWidget(self.lbl_channel)
        vertlayout.addWidget(self.btn_InitConnect)
        vertlayout.addWidget(self.btn_SetConnection)
        vertlayout.addWidget(self.btn_SetChatbox)
        vertlayout.addWidget(self.btn_About)
        vertlayout.addStretch()
        layout_anchor.resize(layout_anchor.sizeHint())

        self.setGeometry(300, 300, 300, 300)
        self.layout().addWidget(layout_anchor)
        #show
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    instant = mainmenu()

    sys.exit(app.exec_())