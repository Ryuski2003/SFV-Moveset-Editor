import sys, os, re
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QVBoxLayout, QWidget, QMessageBox

class ImportJSON(QMainWindow):
    def __init__(self):
        super().__init__()

        self.bac_keys = ['MoveLists', 'HitboxEffectses', 'RawUassetHeaderDontTouch', 'BACVER']
        self.bac_eff_keys = ['MoveLists', 'HitboxEffectses', 'RawUassetHeaderDontTouch', 'BACVER']
        self.bcm_keys = ['Charges', 'Inputs', 'Moves', 'CancelLists', 'RawUassetHeaderDontTouch']
        self.characters = ['ALX', 'BLR', 'BRD', 'BSN', 'CMN', 'CMY', 'CNL', 'DSM', 'FAN', 'GUL', 'IBK', 'JRI', 'KEN', 'KRN', 'LAR', 'NCL', 'NSH', 'RMK', 'RSD', 'RYU', 'URN', 'VEG', 'Z20', 'Z21', 'Z22', 'Z23', 'Z24', 'Z25', 'Z26', 'Z27', 'Z28', 'Z29', 'Z30', 'Z31', 'Z32', 'Z33', 'Z34', 'Z35', 'Z36', 'Z37', 'Z38', 'Z39', 'Z40', 'Z41', 'Z42', 'ZGF']
        self.BACNames = [f"BAC_{i}" for i in list(self.characters)]
        self.BACeffNames = [f"BAC_{i}_eff" for i in list(self.characters)]
        self.BCMNames = [f"BCM_{i}" for i in list(self.characters)]
        # Create a toolbar action to load the JSON file

    def bac(self):
        # Open a file dialog to select a JSON file
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open BAC_XXX.json File", "asd", "JSON Files (*.json)", options=options)
        if file_name:
            if os.path.splitext(os.path.basename(file_name))[0] in self.BACNames:
                try:
                    with open(file_name, 'r') as json_file:
                        bac = json.load(json_file)
                        key = self.get_categories(bac)
                        if key == self.bac_keys:
                            # Display JSON content in the text edit widget
                            return file_name, bac
                        else:   self.error("Warning", "Invalid BAC format")
                except Exception as e:  self.error("Critical", "Failed to open BAC fle.")
            else:   self.error("Warning", "Invalid BAC file name.(Should be BAC_XXX.json)")
        else:   pass
    def baceff(self):
        # Open a file dialog to select a JSON file
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open BAC_XXX_eff.json File", "asd", "JSON Files (*.json)", options=options)
        if file_name:
            if os.path.splitext(os.path.basename(file_name))[0] in self.BACeffNames:
                try:
                    with open(file_name, 'r') as json_file:
                        baceff = json.load(json_file)
                        key = self.get_categories(baceff)
                        if key == self.bac_eff_keys:
                            # Display JSON content in the text edit widget
                            return file_name, baceff
                        else:   self.error("Warning", "Invalid BAC format")
                except Exception as e:  self.error("Critical", "Failed to open BAC fle.")
            else:   self.error("Warning", "Invalid BAC file name.(Should be BAC_XXX_eff.json)")
        else:   pass
    def bcm(self):
        # Open a file dialog to select a JSON file
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "BCM_XXX.json", "", "JSON Files (*.json)", options=options)
        if file_name:
            if os.path.splitext(os.path.basename(file_name))[0] in self.BCMNames:
                try:
                    with open(file_name, 'r') as json_file:
                        bcm = json.load(json_file)
                        key = self.get_categories(bcm)
                        if key == self.bcm_keys:
                            # Display JSON content in the text edit widget
                            return file_name, bcm
                        else:   self.error("Warning", "Invalid BAC format")
                except Exception as e:  self.error("Critical", "Failed to open BAC fle.")
            else:   self.error("Warning", "Invalid BAC file name.(Should be BCM_XXX.json)")
        else:   pass
    def get_categories(self, data):
        categories = [i for i in data]
        return categories

    def error(self, error_type, message):
        msg = QMessageBox()
        if error_type == "Warning":    msg.setIcon(QMessageBox.Warning)
        elif error_type == "Critical":    msg.setIcon(QMessageBox.critical)
        msg.setText("Info")
        msg.setInformativeText(message)
        msg.setWindowTitle("Failed")
        msg.exec_()
        
def main():
    app = QApplication(sys.argv)
    window = ImportJSON()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ImportJSON().bac()
