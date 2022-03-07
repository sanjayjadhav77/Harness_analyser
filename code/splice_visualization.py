# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/splice_visualization.ui'
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
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(75, 22))
        self.label_8.setMaximumSize(QtCore.QSize(75, 39))
        self.label_8.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(65, 21))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(65, 25))
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_2.setStyleSheet(_fromUtf8("border-radius: 1px;\n"
"font: 14pt \"Roboto Condensed\";\n"
"background-color: rgbA(255, 255, 255,0);\n"
"color: rgb(255, 165, 83);"))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(81, 22))
        self.label_9.setMaximumSize(QtCore.QSize(81, 39))
        self.label_9.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(131, 21))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(131, 25))
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_3.setStyleSheet(_fromUtf8("border-radius: 1px;\n"
"font: 14pt \"Roboto Condensed\";\n"
"background-color: rgbA(255, 255, 255,0);\n"
"color: rgb(255, 165, 83);"))
        self.lineEdit_3.setMaxLength(16)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(97, 32))
        self.lineEdit.setMaximumSize(QtCore.QSize(91, 32))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_3.addWidget(self.lineEdit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(131, 32))
        self.pushButton.setMaximumSize(QtCore.QSize(131, 32))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Secondary_btn/fix_color.png);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(300, 400))
        self.label.setMaximumSize(QtCore.QSize(300, 400))
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(206, 206, 206);"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Cable no</span></p></body></html>", None))
        self.lineEdit_2.setText(_translate("MainWindow", "1", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Part Name</span></p></body></html>", None))
        self.lineEdit_3.setText(_translate("MainWindow", "123456", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Net Number", None))
        self.pushButton.setText(_translate("MainWindow", "Display", None))
        self.label.setText(_translate("MainWindow", "Splice Image", None))

import resource_rc
