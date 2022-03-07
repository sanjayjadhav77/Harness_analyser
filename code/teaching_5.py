# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/teaching_5.ui'
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
        MainWindow.resize(1440, 783)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.checkBox_34 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_34.setMaximumSize(QtCore.QSize(21, 26))
        self.checkBox_34.setText(_fromUtf8(""))
        self.checkBox_34.setObjectName(_fromUtf8("checkBox_34"))
        self.horizontalLayout_6.addWidget(self.checkBox_34)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(81, 22))
        self.label.setMaximumSize(QtCore.QSize(81, 22))
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.checkBox_35 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_35.setMaximumSize(QtCore.QSize(21, 26))
        self.checkBox_35.setText(_fromUtf8(""))
        self.checkBox_35.setObjectName(_fromUtf8("checkBox_35"))
        self.horizontalLayout_6.addWidget(self.checkBox_35)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(81, 22))
        self.label_5.setMaximumSize(QtCore.QSize(81, 22))
        self.label_5.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setMinimumSize(QtCore.QSize(191, 27))
        self.checkBox.setMaximumSize(QtCore.QSize(191, 27))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_6.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 41))
        self.lineEdit.setMaximumSize(QtCore.QSize(241, 41))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(150, 41))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(241, 41))
        self.lineEdit_2.setStyleSheet(_fromUtf8("font: 14pt \"Roboto [GOOG]\";\n"
"background-color: rgb(255, 255, 255);"))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.bar1_add = QtGui.QPushButton(self.centralwidget)
        self.bar1_add.setMinimumSize(QtCore.QSize(124, 45))
        self.bar1_add.setMaximumSize(QtCore.QSize(124, 45))
        self.bar1_add.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"font: 14pt \"Roboto [GOOG]\";\n"
"border-image: url(:/images/final_assets/Secondary_btn/normal.png);"))
        self.bar1_add.setFlat(True)
        self.bar1_add.setObjectName(_fromUtf8("bar1_add"))
        self.verticalLayout_3.addWidget(self.bar1_add)
        self.bar2_add = QtGui.QPushButton(self.centralwidget)
        self.bar2_add.setMinimumSize(QtCore.QSize(124, 45))
        self.bar2_add.setMaximumSize(QtCore.QSize(124, 45))
        self.bar2_add.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"font: 14pt \"Roboto [GOOG]\";\n"
"border-image: url(:/images/final_assets/Secondary_btn/normal.png);"))
        self.bar2_add.setFlat(True)
        self.bar2_add.setObjectName(_fromUtf8("bar2_add"))
        self.verticalLayout_3.addWidget(self.bar2_add)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(300, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 40))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"border-image: url(:/images/final_assets/Secondary_btn/exp_db.png);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.Edit_btn = QtGui.QPushButton(self.centralwidget)
        self.Edit_btn.setMinimumSize(QtCore.QSize(125, 0))
        self.Edit_btn.setMaximumSize(QtCore.QSize(125, 41))
        self.Edit_btn.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"border-image: url(:/images/final_assets/Secondary_btn/exp_db.png);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.Edit_btn.setFlat(True)
        self.Edit_btn.setObjectName(_fromUtf8("Edit_btn"))
        self.horizontalLayout_4.addWidget(self.Edit_btn)
        self.usb_btn = QtGui.QPushButton(self.centralwidget)
        self.usb_btn.setMinimumSize(QtCore.QSize(125, 0))
        self.usb_btn.setMaximumSize(QtCore.QSize(125, 41))
        self.usb_btn.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"border-image: url(:/images/final_assets/Secondary_btn/exp_db.png);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.usb_btn.setFlat(True)
        self.usb_btn.setObjectName(_fromUtf8("usb_btn"))
        self.horizontalLayout_4.addWidget(self.usb_btn)
        self.save_btn = QtGui.QPushButton(self.centralwidget)
        self.save_btn.setMinimumSize(QtCore.QSize(125, 45))
        self.save_btn.setMaximumSize(QtCore.QSize(125, 45))
        self.save_btn.setStyleSheet(_fromUtf8("background-image: url(:/images/final_assets/Main_Btn/btn_normal.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.save_btn.setFlat(True)
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.horizontalLayout_4.addWidget(self.save_btn)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Label 1", None))
        self.label_5.setText(_translate("MainWindow", "Label 2", None))
        self.checkBox.setText(_translate("MainWindow", "Use Global Group File", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Barcode 01", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Barcode 02", None))
        self.bar1_add.setText(_translate("MainWindow", "ADD", None))
        self.bar2_add.setText(_translate("MainWindow", "ADD", None))
        self.pushButton.setText(_translate("MainWindow", "Printer Test", None))
        self.Edit_btn.setText(_translate("MainWindow", "EDIT", None))
        self.usb_btn.setText(_translate("MainWindow", "USB", None))
        self.save_btn.setText(_translate("MainWindow", "SAVE", None))

import resource_rc
