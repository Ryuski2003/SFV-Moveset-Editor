# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ramazan\Desktop\SFV Moveset Editor\bacpanel.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BACWindow(object):
    def setupUi(self, BACWindow):
        BACWindow.setObjectName("BACWindow")
        BACWindow.resize(1156, 698)
        self.centralwidget = QtWidgets.QWidget(BACWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Lists = QtWidgets.QTabWidget(self.centralwidget)
        self.Lists.setGeometry(QtCore.QRect(10, 110, 291, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lists.sizePolicy().hasHeightForWidth())
        self.Lists.setSizePolicy(sizePolicy)
        self.Lists.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Lists.setObjectName("Lists")
        self.Moves = QtWidgets.QWidget()
        self.Moves.setObjectName("Moves")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Moves)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.MoveList = QtWidgets.QTableView(self.Moves)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MoveList.sizePolicy().hasHeightForWidth())
        self.MoveList.setSizePolicy(sizePolicy)
        self.MoveList.setObjectName("MoveList")
        self.gridLayout_3.addWidget(self.MoveList, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.Lists.addTab(self.Moves, "")
        self.HitboxEffectses = QtWidgets.QWidget()
        self.HitboxEffectses.setObjectName("HitboxEffectses")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.HitboxEffectses)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.HitboxList = QtWidgets.QTableView(self.HitboxEffectses)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HitboxList.sizePolicy().hasHeightForWidth())
        self.HitboxList.setSizePolicy(sizePolicy)
        self.HitboxList.setObjectName("HitboxList")
        self.gridLayout.addWidget(self.HitboxList, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.Lists.addTab(self.HitboxEffectses, "")
        self.Datas = QtWidgets.QTabWidget(self.centralwidget)
        self.Datas.setGeometry(QtCore.QRect(310, 110, 841, 541))
        self.Datas.setObjectName("Datas")
        self.DataTab = QtWidgets.QWidget()
        self.DataTab.setObjectName("DataTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.DataTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.TypeList = QtWidgets.QListWidget(self.DataTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TypeList.sizePolicy().hasHeightForWidth())
        self.TypeList.setSizePolicy(sizePolicy)
        self.TypeList.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TypeList.setFont(font)
        self.TypeList.setObjectName("TypeList")
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TypeList.addItem(item)
        self.gridLayout_5.addWidget(self.TypeList, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.Commands = QtWidgets.QTableView(self.DataTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Commands.sizePolicy().hasHeightForWidth())
        self.Commands.setSizePolicy(sizePolicy)
        self.Commands.setBaseSize(QtCore.QSize(0, 0))
        self.Commands.setObjectName("Commands")
        self.gridLayout_6.addWidget(self.Commands, 0, 1, 1, 1)
        self.Datas.addTab(self.DataTab, "")
        self.HeaderTab = QtWidgets.QWidget()
        self.HeaderTab.setObjectName("HeaderTab")
        self.Datas.addTab(self.HeaderTab, "")
        BACWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BACWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1156, 26))
        self.menubar.setObjectName("menubar")
        BACWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BACWindow)
        self.statusbar.setObjectName("statusbar")
        BACWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BACWindow)
        self.Lists.setCurrentIndex(0)
        self.Datas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BACWindow)

    def retranslateUi(self, BACWindow):
        _translate = QtCore.QCoreApplication.translate
        BACWindow.setWindowTitle(_translate("BACWindow", "Character/BAC File"))
        self.Lists.setTabText(self.Lists.indexOf(self.Moves), _translate("BACWindow", "Moves"))
        self.Lists.setTabText(self.Lists.indexOf(self.HitboxEffectses), _translate("BACWindow", "Hitbox Effects"))
        __sortingEnabled = self.TypeList.isSortingEnabled()
        self.TypeList.setSortingEnabled(False)
        item = self.TypeList.item(0)
        item.setText(_translate("BACWindow", "Auto Cancels"))
        item = self.TypeList.item(1)
        item.setText(_translate("BACWindow", "Type1s"))
        item = self.TypeList.item(2)
        item.setText(_translate("BACWindow", "Forces"))
        item = self.TypeList.item(3)
        item.setText(_translate("BACWindow", "Cancels"))
        item = self.TypeList.item(4)
        item.setText(_translate("BACWindow", "Others"))
        item = self.TypeList.item(5)
        item.setText(_translate("BACWindow", "Hitboxes"))
        item = self.TypeList.item(6)
        item.setText(_translate("BACWindow", "Hurtboxes"))
        item = self.TypeList.item(7)
        item.setText(_translate("BACWindow", "Physics Boxes"))
        item = self.TypeList.item(8)
        item.setText(_translate("BACWindow", "Animations"))
        item = self.TypeList.item(9)
        item.setText(_translate("BACWindow", "Type9s"))
        item = self.TypeList.item(10)
        item.setText(_translate("BACWindow", "Sound Effects"))
        item = self.TypeList.item(11)
        item.setText(_translate("BACWindow", "Visual Effects"))
        item = self.TypeList.item(12)
        item.setText(_translate("BACWindow", "Positions"))
        self.TypeList.setSortingEnabled(__sortingEnabled)
        self.Datas.setTabText(self.Datas.indexOf(self.DataTab), _translate("BACWindow", "Data"))
        self.Datas.setTabText(self.Datas.indexOf(self.HeaderTab), _translate("BACWindow", "Header"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BACWindow = QtWidgets.QMainWindow()
    ui = Ui_BACWindow()
    ui.setupUi(BACWindow)
    BACWindow.show()
    sys.exit(app.exec_())
