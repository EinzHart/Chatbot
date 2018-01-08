import sys
from PyQt5.QtWidgets import QApplication
from mainmenu import *
from chatbox import *
from connection_settings import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #dialogs
    mainmenu_ = mainmenu()
    connection_settings_ = connection_setting()
    chatbox_ = chatbox()
    #connection
    mainmenu_.connect_conn_setting(connection_settings_)
    mainmenu_.connect_chatbox(chatbox_)
    
    connection_settings_.connect_mainmenu(mainmenu_)

    chatbox_.connect_mainmenu(mainmenu_)
    
    sys.exit(app.exec_())
    
