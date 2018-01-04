import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QFormLayout, QLineEdit, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, QObject

class connection_setting(QDialog):


    def __init__(self):

        super().__init__()

        # variables
        self.channel_name = 'einzhart'
        self.nickname = 'einzhart'
        self.server_name = 'irc.chat.twitch.tv'
        self.server_port = 6667
        self.client_token = 'oauth:tzkaxwnvm3si38sz8davspeijz00p6'

        #textbox
        #channel name
        self.tbox_channame = QLineEdit(self)
        self.tbox_channame.setText(self.channel_name)

        #nickname
        self.tbox_nickname = QLineEdit(self)
        self.tbox_nickname.setText(self.nickname)

        #clientToken
        self.tbox_clienttoken = QLineEdit(self)
        self.tbox_clienttoken.setText(self.client_token)

        #servername
        self.tbox_servername = QLineEdit(self)
        self.tbox_servername.setText(self.server_name)

        #serverport
        self.tbox_serverport = QLineEdit(self)
        self.tbox_serverport.setText(str(self.server_port))

        #buttons
        self.btn_apply = QPushButton('Apply', self)
        self.btn_cancel = QPushButton('Cancel', self)
        self.Init_UI()

    def Init_UI(self):
        #textbox

        #buttons
        #apply
        self.btn_apply.resize(self.btn_apply.sizeHint())
        self.btn_apply.clicked.connect(self.btn_clicked_apply)
        #cancel
        self.btn_cancel.resize(self.btn_cancel.sizeHint())
        self.btn_cancel.clicked.connect(self.btn_clicked_cancel)
        #layouts
        layout = QFormLayout()
        layout.addRow(QLabel("channel name:"), self.tbox_channame)
        layout.addRow(QLabel("nickname:"), self.tbox_nickname)
        layout.addRow(QLabel("client token:"), self.tbox_clienttoken)
        layout.addRow(QLabel("server name:"), self.tbox_servername)
        layout.addRow(QLabel("server port:"), self.tbox_serverport)

        layout.addRow(self.btn_apply, self.btn_cancel)
        self.setGeometry(400, 400, 400, 250)
        self.setLayout(layout)
        #self.show()

    def call_from_mainmenu(self):
        self.mainmenu_frame.hide()
        self.show()

    def connect_mainmenu(self, mainmenu_obj):
        mainmenu_obj.btn_SetConnection.clicked.connect(self.call_from_mainmenu)
        self.mainmenu_frame = mainmenu_obj

    def btn_clicked_apply(self):
        self.channel_name = self.tbox_channame.text()
        self.nickname = self.tbox_nickname.text()
        self.client_token = self.tbox_clienttoken.text()
        self.server_name = self.tbox_servername.text()
        self.server_port = int(self.tbox_serverport.text())

        self.hide()

    def btn_clicked_cancel(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    instance = connection_setting()
    sys.exit(app.exec_())
