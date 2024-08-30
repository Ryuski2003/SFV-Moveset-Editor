from arayuz_tasarim2 import Ui_BACWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtTasarim = Ui_BACWindow()
        self.qtTasarim.setupUi(self)
        self.qtTasarim.Moves.
    def asd(self):
        print("asd")
        
app = QApplication([])
deneme = main()
deneme.show()
app.exec_()
