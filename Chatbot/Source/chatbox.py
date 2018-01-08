import sys
from irc_interface import *
from parsing import *
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
            text_string = str(text,'utf-8')
            if text_string.find('PING') != -1:
                self.irccomm.pong() #need to return irc ping request
            else:
                msgtype, chatname, chatcont = parse_privmsg(text_string)
                if msgtype == 'message':
                   self.sig.emit(chatname + ':' + chatcont)
            



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

        #socket default parameters
        self.channel_name = 'einzhart'
        self.nickname = 'einzhart'
        self.server_name = 'irc.chat.twitch.tv'
        self.server_port = 6667
        self.client_token = 'oauth:leo8i5zthdzeakbmy2lq1b84fbpaum'

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
        
    def initUI(self):
        self.btn_disconnect.move(250,350)
        self.chatlist.resize(300,300)
        self.chatlist.move(15,15)
        self.chatlist.setFont(QFont('BigNoodleTooOblique', 15))
        self.chatlist.setWordWrap(True)
        #self.show()

    
    #button click event handler
    def click_disconnect(self):
        self.ircthread.terminate()
        self.ircthread.wait()
        self.ircomm.disconnect()
        #destroy the old sockets and thread
        self.ircthread.__del__()
        self.ircthread.__del__()
        self.hide()

    #connect to mainmenu
    def connect_mainmenu(self, mainmenu):
        self.mainmenu_ = mainmenu
        mainmenu.btn_InitConnect.clicked.connect(self.call_from_mainmenu)
    
    #mainmenu call handler
    def call_from_mainmenu(self):
        #handling displays
        self.mainmenu_.hide()
        self.chatlist.clear()
        self.chatlist.addItem("The world could always use more heroes!")
        self.show()
        
        #get connection config from mainmenu dialog
        self.channel_name = self.mainmenu_.channel_name
        self.nickname = self.mainmenu_.nickname
        self.client_token = self.mainmenu_.client_token
        self.server_name = self.mainmenu_.server_name
        self.server_port = self.mainmenu_.server_port
        
        #config socket for irc
        self.ircomm = irc_comm(self.channel_name, self.nickname,
                               self.client_token, self.server_name, self.server_port)
        #config thread receiving
        self.ircthread = irc_thread(self.ircomm, self.textsignal)
        self.ircomm.connect()
        self.ircthread.start()
        
    #incoming string event 
    @pyqtSlot('QString')
    def addLine(self, new_line):
        self.chatlist.addItem(new_line)
        self.chatlist.scrollToBottom()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    instance = chatbox()
    sys.exit(app.exec_())
    
    
