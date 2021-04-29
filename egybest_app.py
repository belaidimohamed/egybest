from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon ,QImage ,QPalette,QBrush,QFont
from PyQt5.QtCore import QSize, Qt
import os

os.chdir(r'/home/mohamed/Desktop/egybest/')
class Utils(QDialog):
    def __init__(self):
        super().__init__()
    def label(self,txt='',color="grey",form="sanserif",a=10):
        l=QLabel(txt)
        l.setFont(QFont(form,a))
        l.setStyleSheet('color:'+color)
        return l
class init(Utils) :
    def __init__(self):
        super().__init__()
        self.initwindow()
        self.show()
    def initwindow(self):
        self.setWindowTitle('CTF')
        self.setWindowIcon(QIcon('logo.jfif'))
        self.setGeometry(200,80,1000,600)
        self.setStyleSheet("background-color: black;")
        self.vbox=QVBoxLayout()

        # --------------- title shit ---------------------
        hboxTitle = QHBoxLayout()
        hboxTitle.addWidget(self.label("Welcome to ","yellow","sanserif",20))
        hboxTitle.addWidget(self.label("Egy","red","sanserif",23))
        hboxTitle.addWidget(self.label("Best ","blue","sanserif",23))
        hboxTitle.addWidget(self.label("Downloader ! ","yellow","sanserif",20))
        hboxTitle.setAlignment(Qt.AlignCenter)

        # --------------- input serie url shit ---------------------

        serieUrlHbox=QHBoxLayout()
        serieUrlHbox.addWidget(self.label("Can you please paste the serie Url : ","orange"))
        self.line=QLineEdit()
        self.line.setStyleSheet("color:white;margin-left:5px;")
        self.line.returnPressed.connect(self.onpress)
        serieUrlHbox.addWidget(self.line)

        serieUrlHbox.setContentsMargins(20,20,250,20)

        self.vbox.addLayout(hboxTitle)
        self.vbox.addLayout(serieUrlHbox)
        self.vbox.setContentsMargins(1,30,1,230)

        self.setLayout(self.vbox)

    def onpress(self):
        self.p = General(self.line.text())
        self.close()

class General(Utils) :
    def __init__(self,url):
        super().__init__()
        self.url = url
        self.initwindow()
        self.show()
    def initwindow(self):
        self.setWindowTitle('CTF')
        self.setWindowIcon(QIcon('logo.jfif'))
        self.setGeometry(200,80,1000,600)
        self.setStyleSheet("background-color: black;")
        self.vbox=QVBoxLayout()

        print(self.url)
        # --------------- title shit ---------------------
        hboxTitle = QHBoxLayout()
        groupbox = QGroupBox("General informations :")

        gbox=QGridLayout()
        gbox.setContentsMargins(20,10,20,10)
        gbox.addWidget(self.label("Serie title :  ","orange","sanserif",14),1,1)
        gbox.addWidget(self.label("data","white","sanserif",14),1,2)
        gbox.addWidget(self.label("description :  ","orange","sanserif",14),2,1)
        gbox.addWidget(self.label("data","white","sanserif",14),2,2)
        gbox.addWidget(self.label("number of seasons : ","orange","sanserif",14),3,1)
        gbox.addWidget(self.label("5","white","sanserif",14),3,2)

        groupbox.setLayout(gbox)
        self.vbox.addWidget(groupbox)
        self.vbox.addWidget(self.label(self.url,'white',"sanserif",20))
        self.vbox.setContentsMargins(1,30,1,230)
        self.setLayout(self.vbox)

w=init()