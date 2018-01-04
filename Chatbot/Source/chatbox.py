import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPainter, QColor, QFont, QBrush
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject

class chatbox(QDialog):

    def __init__(self):

        super().__init__()
        #display accessories
        self.btn_disconnect = QPushButton("disconnect")
        self.lbl_textbox = QLabel("The world could always use more heroes!")
        self.initUI()

        #socket parameters
        self.channel_name = 'einzhart'
        self.nickname = 'einzhart'
        self.servername = 'irc.chat.twitch.tv'
        self.server_port = 6667
        self.client_token = 'oauth:tzkaxwnvm3si38sz8davspeijz00p6'

        #display parameters
        #self.disp_font =
        #self.disp_color =
        #self.disp_opacity =
        self.disp_lines = 
        
        #dialog setup
        
        
    def initUI():
        

    
