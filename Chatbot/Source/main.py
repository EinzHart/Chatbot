import sys
from PyQt5.QtWidgets import QApplication
from mainmenu import *
from chatbox import *
from connection_settings import *
from display_settings import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #dialogs
    mainmenu_ = mainmenu()
    connection_settings_ = connection_setting()
    chatbox_ = chatbox()
    disp_settings_ = display_preference()
    #connection
    mainmenu_.connect_conn_setting(connection_settings_)
    mainmenu_.connect_chatbox(chatbox_)
    mainmenu_.connect_disp_settings(disp_settings_)
    
    connection_settings_.connect_mainmenu(mainmenu_)
    chatbox_.connect_mainmenu(mainmenu_)
    disp_settings_.connect_mainmenu(mainmenu_)
    
    sys.exit(app.exec_())
    
