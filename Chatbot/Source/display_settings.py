import sys
from PyQt5.QtWidgets import QApplication, QFontDialog, QPushButton, QLabel, QLineEdit, QDialog, \
     QSlider, QVBoxLayout, QHBoxLayout, QGroupBox, QColorDialog, QWidget
from PyQt5.QtGui import QIcon, QColor, QFont
from PyQt5.QtCore import Qt, pyqtSignal, QObject

class display_preference(QDialog):
    def __init__(self):
        
        super().__init__()
        #dialog properities
        self.setWindowTitle('display settings')
        self.setWindowIcon(QIcon('sheikah.png'))

        #variables
        self.chatbox_opacity = 0
        self.chatbox_font = QFont('BigNoodleTooOblique', 15)
        self.chatbox_bkgcolor = QColor(255, 255, 255)
        #self.chatbox_bkgcolor

        #widgets
        #font selector
        self.btn_fontsel = QPushButton('font', self)
        #slider for window opacity
        self.sld_opacity = QSlider(self)
        self.sld_opacity.setMinimum(0)
        self.sld_opacity.setMaximum(100)
        self.sld_opacity.setOrientation(Qt.Horizontal)
        #button for chatbox color
        self.btn_colorsel = QPushButton('bkg color', self)
        #apply and cancel
        self.btn_apply = QPushButton('apply')
        self.btn_cancel = QPushButton('cancel')
        
        #connection
        self.btn_fontsel.clicked.connect(self.font_select)
        self.sld_opacity.valueChanged.connect(self.opacity_alter)
        self.btn_colorsel.clicked.connect(self.color_select)
        #init functions call
        self.initUI()
        self.show()

    def initUI(self):
        #font groupbox
        self.gbox_font = QGroupBox('font')
        self.lbl_font = QLabel(self.chatbox_font.family()+','+str(self.chatbox_font.pointSize())+'pts')
        self.lbl_font.setFont(self.chatbox_font)
        gbox_font_layout = QVBoxLayout()
        gbox_font_layout.addWidget(self.lbl_font)
        gbox_font_layout.addWidget(self.btn_fontsel)
        self.gbox_font.setLayout(gbox_font_layout)
        
        #slider groupbox
        self.gbox_opa = QGroupBox('opacity')
        self.lbl_opacity = QLineEdit(str(float(self.chatbox_opacity)))
        self.lbl_opacity.setFixedSize(40,20)
        self.lbl_opacity.setReadOnly(True)
        gbox_opa_layout = QHBoxLayout()
        gbox_opa_layout.addWidget(self.lbl_opacity)
        gbox_opa_layout.addWidget(self.sld_opacity)
        self.gbox_opa.setLayout(gbox_opa_layout)
        #bkgcolor groupbox
        self.gbox_col = QGroupBox('bkg color')
        self.lbl_colorbox = QLabel()
        self.lbl_colorbox.setStyleSheet('background-color:'+self.chatbox_bkgcolor.name()+';')
        gbox_col_layout = QHBoxLayout()
        gbox_col_layout.addWidget(self.lbl_colorbox)
        gbox_col_layout.addWidget(self.btn_colorsel)
        self.gbox_col.setLayout(gbox_col_layout)
        #apply and cancel
        aplycan_layout = QHBoxLayout()
        aplycan_layout.addWidget(self.btn_apply)
        aplycan_layout.addWidget(self.btn_cancel)
        self.aplycan = QWidget()
        self.aplycan.setLayout(aplycan_layout)
        
        
        #organze groupboxes
        ovr_layout = QVBoxLayout()
        ovr_layout.addWidget(self.gbox_font)
        ovr_layout.addWidget(self.gbox_opa)
        ovr_layout.addWidget(self.gbox_col)
        ovr_layout.addWidget(self.aplycan)
        self.setLayout(ovr_layout)
        pass
        
    def font_select(self):
        _font, ok = QFontDialog().getFont()
        if ok:
            self.chatbox_font = _font
            self.lbl_font.setFont(_font)
            self.lbl_font.setText(self.chatbox_font.family()+','+str(self.chatbox_font.pointSize())+'pts')
            

    def opacity_alter(self, slider_val):
        _opacity = format(float(slider_val / 100), '.2f');
        self.lbl_opacity.setText(str(_opacity))
        print(_opacity)

    def color_select(self):
        _bkgcolor = QColorDialog.getColor()
        self.lbl_colorbox.setStyleSheet('background-color:'+_bkgcolor.name()+';')
        print(_bkgcolor.name())
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    instance = display_preference()
    sys.exit(app.exec_())
