import sys
from irc_interface import *
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QListWidget
from PyQt5.QtGui import QIcon, QPainter, QColor, QFont, QBrush
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject, QThread

class irc_thread(QThread):
    def __init__(self, ircomm, text_sig):
        QThread.__init__(self)
        self.irccomm = ircomm
        self.sig = text_sig
        
    def __del__(self):
        self.wait()

    def run(self):
        while 1:
            text = self.irccomm.receive()
            self.sig.emit(str(text,'utf-8'))
            



class chatbox(QDialog):
    #config signal
    textsignal = pyqtSignal('QString')

    def __init__(self):

        super().__init__()
        #dialog properities
        self.setWindowTitle("chatbox")
        self.setWindowIcon(QIcon('sheikah.png'))
        self.setGeometry(400,400,400,400)
        
        #display accessories
        self.btn_disconnect = QPushButton("disconnect", self)
        self.chatlist = QListWidget(self)
        self.chatlist.addItem("The world could always use more heroes!")

        #socket parameters
        self.channel_name = 'einzhart'
        self.nickname = 'einzhart'
        self.server_name = 'irc.chat.twitch.tv'
        self.server_port = 6667
        self.client_token = 'oauth:tzkaxwnvm3si38sz8davspeijz00p6'

        #config socket for irc
        self.ircomm = irc_comm(self.channel_name, self.nickname,
                               self.client_token, self.server_name, self.server_port)

        
        #config thread receiving
        self.ircthread = irc_thread(self.ircomm, self.textsignal)

        #display parameters
        #self.disp_font =
        #self.disp_color =
        #self.disp_opacity =
        self.disp_lines = 1


        #signal connecting
        self.textsignal.connect(self.addLine)
        self.btn_disconnect.clicked.connect(self.click_disconnect)

        #UI initialization
        self.initUI()
        
        #socket initiate connection
        self.ircomm.connect()
        self.ircthread.start()
        
    def initUI(self):
        self.btn_disconnect.move(250,350)
        self.chatlist.resize(300,300)
        self.chatlist.move(15,15)
        self.chatlist.setFont(QFont('BigNoodleTooOblique', 15))
        self.show()

    def click_disconnect(self):
        self.ircthread.terminate()
        self.ircthread.wait()
        self.ircomm.disconnect()
        self.close()
        
    @pyqtSlot('QString')
    def addLine(self, new_line):
        self.chatlist.addItem(new_line)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    instance = chatbox()
    sys.exit(app.exec_())
    
    
