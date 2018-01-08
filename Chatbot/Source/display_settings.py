import sys
from PyQt5.QtWidgets import QApplication, QFontDialog, QPushButton, QLabel, QLineEdit, QDialog, QSlider, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, QObject

class display_preference(QDialog):
    def __init__(self):
        
        super().__init__()
        #dialog properities
        self.setWindowTitle('connection settings')
        self.setWindowIcon(QIcon('sheikah.png'))

        #variables
        self.chatbox_fontname = ''
        self.chatbox_fontsize = ''
        self.chatbox_fontcolor = ''
        self.chatbox_opacity = 1
        self.chatbox_bkgcolor = ''

        #widgets
        self.btn_fontsel = QPushButton('font', self)
        
        self.sld_opacity = QSlider(self)
        self.sld_opacity.setMinimum(0)
        self.sld_opacity.setMaximum(100)
        self.sld_opacity.setOrientation(Qt.Horizontal)

        #connection
        self.btn_fontsel.clicked.connect(self.font_select)
        self.sld_opacity.valueChanged.connect(self.opacity_alter)
        self.initUI()
        self.show()

    def initUI(self):
        #font groupbox
        self.gbox_font = QGroupBox('font')
        gbox_font_layout = QHBoxLayout()
        gbox_font_layout.addWidget(self.btn_fontsel)
        self.gbox_font.setLayout(gbox_font_layout)
        
        #slider groupbox
        self.gbox_opa = QGroupBox('opacity')
        gbox_opa_layout = QHBoxLayout()
        gbox_opa_layout.addWidget(self.sld_opacity)
        self.gbox_opa.setLayout(gbox_opa_layout)
        #bkgcolor groupbox

        #organze groupboxes
        ovr_layout = QVBoxLayout()
        ovr_layout.addWidget(self.gbox_font)
        ovr_layout.addWidget(self.gbox_opa)
        self.setLayout(ovr_layout)
        pass
        
    def font_select(self):
        self.chatbox_qfont, ok = QFontDialog().getFont()
        if ok:
            print(self.chatbox_qfont.toString())

    def opacity_alter(self, slider_val):
        self.opacity = float(slider_val / 100);
        print(self.opacity)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    instance = display_preference()
    sys.exit(app.exec_())
