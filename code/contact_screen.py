# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/contact_screen.ui'
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
        MainWindow.resize(458, 298)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 150, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(158, 21))
        self.label.setMaximumSize(QtCore.QSize(141, 21))
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(150, 61))
        self.label_4.setMaximumSize(QtCore.QSize(311, 61))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"font: 12pt \"Roboto Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(150, 50))
        self.label_5.setMaximumSize(QtCore.QSize(311, 61))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"font: 12pt \"Roboto Condensed\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(86, 21))
        self.label_3.setMaximumSize(QtCore.QSize(71, 21))
        self.label_3.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(150, 91))
        self.label_6.setMaximumSize(QtCore.QSize(300, 91))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"font: 12pt \"Roboto Condensed\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(150, 25))
        self.label_7.setMaximumSize(QtCore.QSize(311, 25))
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(38, 177, 255);\n"
"font: 12pt \"Roboto Condensed\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "About Us", None))
        self.label_2.setText(_translate("MainWindow", "Manufacturers of :\n"
"Display Systems : LED walls, Andon displays, advertisement \n"
"displays etc\n"
"Wire Harness : Test benches and  test equipments", None))
        self.label.setText(_translate("MainWindow", "Service & Support", None))
        self.label_4.setText(_translate("MainWindow", "service@kalptechsolutions.com\n"
"+91 - 9011261642", None))
        self.label_5.setText(_translate("MainWindow", "sales@kalptechsolutions.com\n"
"+91 - 9503963958", None))
        self.label_3.setText(_translate("MainWindow", "Location", None))
        self.label_6.setText(_translate("MainWindow", "Plot no 277, sector 4, Sant Nager,\n"
"Kendriya vihar Rd,\n"
"PCNTDA, Moshi, Pune,\n"
"Maharashtra 412105 ", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"www.kalptechsolutions.com\"><span style=\" text-decoration: underline; color:#0000ff;\">www.kalptechsolutions.com</span></a></p></body></html>", None))

import resource_rc
