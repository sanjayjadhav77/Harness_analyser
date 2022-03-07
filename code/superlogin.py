# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/superlogin.ui'
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
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1440, 800)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(429, 319))
        self.frame.setMaximumSize(QtCore.QSize(429, 319))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(32, 32))
        self.label.setMaximumSize(QtCore.QSize(32, 32))
        self.label.setStyleSheet(_fromUtf8("background-image: url(:/images/final_assets/Login_Icons/pw.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/final_assets/Login_Icons/pw.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(16, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.key = QtGui.QLineEdit(self.frame)
        self.key.setMinimumSize(QtCore.QSize(150, 23))
        self.key.setMaximumSize(QtCore.QSize(221, 21))
        self.key.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.key.setStyleSheet(_fromUtf8("border-radius: 1px;\n"
"font: 12pt \"Roboto [GOOG]\";\n"
"background-color: rgbA(255, 255, 255,0);"))
        self.key.setText(_fromUtf8(""))
        self.key.setFrame(True)
        self.key.setEchoMode(QtGui.QLineEdit.Password)
        self.key.setObjectName(_fromUtf8("key"))
        self.horizontalLayout_3.addWidget(self.key)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 35))
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8("background-image: url(:/images/final_assets/Main_Btn/btn_normal.png);\n"
"font: 14pt \"Roboto [GOOG]\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(139, 30))
        self.pushButton_2.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Secondary_btn/big_normal.png);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setMinimumSize(QtCore.QSize(139, 30))
        self.pushButton_4.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Secondary_btn/big_normal.png);"))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.frame)
        self.pushButton_6.setMinimumSize(QtCore.QSize(139, 30))
        self.pushButton_6.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Secondary_btn/big_normal.png);"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.frame)
        self.pushButton_5.setMinimumSize(QtCore.QSize(139, 30))
        self.pushButton_5.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Secondary_btn/big_normal.png);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 130, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem7, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.key.setPlaceholderText(_translate("MainWindow", "Authentication Key", None))
        self.pushButton.setText(_translate("MainWindow", "Login", None))
        self.pushButton.setShortcut(_translate("MainWindow", "Return", None))
        self.pushButton_2.setText(_translate("MainWindow", "Wrong Sample", None))
        self.pushButton_4.setText(_translate("MainWindow", "Clear Scan", None))
        self.pushButton_6.setText(_translate("MainWindow", "Supervisor Access1", None))
        self.pushButton_5.setText(_translate("MainWindow", "Supervisor Access2", None))

import resource_rc
