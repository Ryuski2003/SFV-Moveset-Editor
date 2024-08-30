from PyQt5 import QtWidgets, uic
import sys, os, json
from PyQt5.QtCore import QDateTime,QTimer
from json_import import ImportJSON
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QVBoxLayout, QWidget


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        uic.loadUi('mainpanel.ui', self)
        self.show()
        self.BACFile = None
        self.BACData = None
        self.BACEffFile = None
        self.BACEffData = None
        self.BCMFile = None
        self.BCMData = None
        self.characters = {'ALX':'Alex', 'BLR':'Claw', 'BRD':'Birdie', 'BSN':'Boxer', 'CMN':'Common', 'CMY':'Cammy',
                           'CNL':'Chun-Li', 'DSM':'Dhalsim', 'FAN':'F.A.N.G.', 'GUL':'Guile', 'IBK':'Ibuki', 'JRI':'Juri',
                           'KEN':'Ken', 'KRN':'Karin', 'LAR':'Laura', 'NCL':'Necalli', 'NSH':'Nash', 'RMK':'R. Mika',
                           'RSD':'Rashid', 'RYU':'Ryu', 'URN':'Urien', 'VEG':'Dictator', 'Z20':'Kolin', 'Z21':'/Gouki',
                           'Z22':'Ed', 'Z23':'Menat', 'Z24':'Abigail', 'Z25':'Zeku', 'Z26':'Sakura', 'Z27':'Blanka',
                           'Z28':'Falke', 'Z29':'Cody', 'Z30':'G', 'Z31':'Sagat', 'Z32':'Kage', 'Z33':'Poison',
                           'Z34':'E. Honda', 'Z35':'Lucia', 'Z36':'Gill', 'Z37':'Seth', 'Z38':'Dan', 'Z39':'Rose',
                           'Z40':'Oro', 'Z41':'Akira', 'Z42':'Luke', 'ZGF':'Zangief'}
        self.actionOpen_BAC.triggered.connect(self.bac_import)
        self.actionOpen_BAC_Eff.triggered.connect(self.baceff_import)
        self.actionOpen_BCM.triggered.connect(self.bcm_import)
        self.EditBAC.clicked.connect(self.openbac)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)
        self.update_date_time()
#------------------------------------------------------------Import Files------------------------------------------------------------
    def bac_import(self):
        try:
            self.BACFile, self.BACData = Importer.bac()
            self.EditBAC.setEnabled(True)
            self.BAC_Name.setText(self.displayName(os.path.splitext(os.path.basename(self.BACFile))[0]))
        except: pass

    def baceff_import(self):
        try:
            self.BACEffFile, self.BACEffData = Importer.baceff()
            self.EditBACEff.setEnabled(True)
            self.BAC_Eff_Name.setText(self.displayName(os.path.splitext(os.path.basename(self.BACEffFile))[0]))
        except: pass

    def bcm_import(self):
        try:
            self.BCMFile, self.BCMData = Importer.bcm()
            self.EditBCM.setEnabled(True)
            self.BCM_Name.setText(self.displayName(os.path.splitext(os.path.basename(self.BCMFile))[0]))
        except: pass
#------------------------------------------------------------Update Time-------------------------------------------------------------
    def update_date_time(self):
        current_time = QDateTime.currentDateTime()
        formatted_date = current_time.toString("yyyy-MM-dd")
        formatted_time = current_time.toString("HH:mm:ss")
        self.Date_Time.setText(f"Current Date: {formatted_date}\nCurrent Time: {formatted_time}")

    def displayName(self, filename=str()):
        chara = filename.split('_')[1]
        return f'{self.characters[chara]}/{filename}'
    
    def openbac(self):
        bacapp.execute()
class BACUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(BACUi, self).__init__()
        uic.loadUi('bacpanel.ui', self)
        self.BACData = None
    def execute(self):
        self.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainUi()
    bacapp = BACUi()
    Importer = ImportJSON()
    app.exec_()
