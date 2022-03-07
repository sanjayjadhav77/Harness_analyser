# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/teaching_3.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1440, 800)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(75, 22))
        self.label_8.setMaximumSize(QtCore.QSize(75, 39))
        self.label_8.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMinimumSize(QtCore.QSize(81, 21))
        self.lineEdit.setMaximumSize(QtCore.QSize(81, 25))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setStyleSheet(_fromUtf8("border-radius: 1px;\n"
"font: 14pt \"Roboto Condensed\";\n"
"background-color: rgbA(255, 255, 255,0);\n"
"color: rgb(255, 165, 83);"))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(81, 22))
        self.label_9.setMaximumSize(QtCore.QSize(81, 39))
        self.label_9.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(131, 21))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(131, 25))
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_2.setStyleSheet(_fromUtf8("border-radius: 1px;\n"
"font: 14pt \"Roboto Condensed\";\n"
"background-color: rgbA(255, 255, 255,0);\n"
"color: rgb(255, 165, 83);"))
        self.lineEdit_2.setMaxLength(16)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setMinimumSize(QtCore.QSize(60, 22))
        self.label_14.setMaximumSize(QtCore.QSize(91, 23))
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
""))
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_6.addWidget(self.label_14)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 32))
        self.comboBox.setMaximumSize(QtCore.QSize(220, 29))
        self.comboBox.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);\n"
""))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.comboBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setMinimumSize(QtCore.QSize(60, 22))
        self.label_15.setMaximumSize(QtCore.QSize(91, 23))
        self.label_15.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
""))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_6.addWidget(self.label_15)
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(75, 32))
        self.comboBox_2.setMaximumSize(QtCore.QSize(75, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);\n"
""))
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setModelColumn(0)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.comboBox_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 37))
        self.pushButton.setMaximumSize(QtCore.QSize(212, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-image: url(:/images/final_assets/Main_Btn/btn_normal.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Roboto Condensed\";"))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_6.addWidget(self.pushButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton_7.setMaximumSize(QtCore.QSize(85, 31))
        self.pushButton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_7.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"border-image: url(:/images/final_assets/Secondary_btn/exp_db.png);\n"
"font: 12pt \"Roboto [GOOG]\";\n"
""))
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_6.addWidget(self.pushButton_7)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hrn_table = QtGui.QTableWidget(self.centralwidget)
        self.hrn_table.setEnabled(True)
        self.hrn_table.setMinimumSize(QtCore.QSize(300, 200))
        self.hrn_table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.hrn_table.setStyleSheet(_fromUtf8("font: 25 16pt \"Roboto [GOOG]\";"))
        self.hrn_table.setFrameShape(QtGui.QFrame.NoFrame)
        self.hrn_table.setFrameShadow(QtGui.QFrame.Sunken)
        self.hrn_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.hrn_table.setRowCount(2048)
        self.hrn_table.setColumnCount(128)
        self.hrn_table.setObjectName(_fromUtf8("hrn_table"))
        self.hrn_table.horizontalHeader().setVisible(False)
        self.hrn_table.horizontalHeader().setCascadingSectionResizes(False)
        self.hrn_table.horizontalHeader().setDefaultSectionSize(66)
        self.hrn_table.horizontalHeader().setStretchLastSection(True)
        self.hrn_table.verticalHeader().setVisible(False)
        self.hrn_table.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.hrn_table, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton_4.setMaximumSize(QtCore.QSize(85, 31))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"border-image: url(:/images/final_assets/Secondary_btn/exp_db.png);\n"
"font: 12pt \"Roboto [GOOG]\";\n"
""))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 38))
        self.pushButton_6.setMaximumSize(QtCore.QSize(100, 38))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setStyleSheet(_fromUtf8("background-image: url(:/images/final_assets/Main_Btn/btn_normal.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Roboto [GOOG]\";"))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Cable no</span></p></body></html>", None))
        self.lineEdit.setText(_translate("MainWindow", "1", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Part Name</span></p></body></html>", None))
        self.lineEdit_2.setText(_translate("MainWindow", "123456", None))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Method</span></p></body></html>", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "On Board", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cutting Chart", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "USB", None))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Stage</span></p></body></html>", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1 ", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "5", None))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "6", None))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "7", None))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "8", None))
        self.pushButton.setText(_translate("MainWindow", "Learn", None))
        self.pushButton.setShortcut(_translate("MainWindow", "Return", None))
        self.pushButton_7.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_4.setText(_translate("MainWindow", "EDIT", None))
        self.pushButton_6.setText(_translate("MainWindow", "SAVE", None))

import resource_rc
