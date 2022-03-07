# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/abt_tester.ui'
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
        MainWindow.resize(1472, 800)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem = QtGui.QSpacerItem(20, 130, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setMinimumSize(QtCore.QSize(125, 41))
        self.label_13.setMaximumSize(QtCore.QSize(125, 41))
        self.label_13.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_4.addWidget(self.label_13)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setMinimumSize(QtCore.QSize(125, 41))
        self.label_11.setMaximumSize(QtCore.QSize(125, 41))
        self.label_11.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_4.addWidget(self.label_11)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(125, 41))
        self.label.setMaximumSize(QtCore.QSize(125, 41))
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(125, 41))
        self.label_2.setMaximumSize(QtCore.QSize(125, 41))
        self.label_2.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(135, 41))
        self.label_6.setMaximumSize(QtCore.QSize(125, 41))
        self.label_6.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(100, 41))
        self.label_4.setMaximumSize(QtCore.QSize(125, 41))
        self.label_4.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(180, 41))
        self.label_5.setMaximumSize(QtCore.QSize(125, 41))
        self.label_5.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
"color: rgb(3, 218, 50);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(180, 41))
        self.label_3.setMaximumSize(QtCore.QSize(125, 41))
        self.label_3.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
"color: rgb(3, 218, 50);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(125, 41))
        self.label_8.setMaximumSize(QtCore.QSize(125, 41))
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(3, 218, 50);\n"
"font: 14pt \"Roboto Condensed\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setMinimumSize(QtCore.QSize(125, 41))
        self.label_12.setMaximumSize(QtCore.QSize(125, 41))
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(3, 218, 50);\n"
"font: 14pt \"Roboto Condensed\";"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_5.addWidget(self.label_12)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setMinimumSize(QtCore.QSize(125, 41))
        self.label_10.setMaximumSize(QtCore.QSize(125, 41))
        self.label_10.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
"color: rgb(38, 177, 255);"))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_5.addWidget(self.label_10)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(125, 41))
        self.label_9.setMaximumSize(QtCore.QSize(125, 41))
        self.label_9.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
"color: rgb(38, 177, 255);"))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(754, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(106, 28))
        self.pushButton.setMaximumSize(QtCore.QSize(106, 28))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Page_Toggle/page_unselect_facility.png);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem5 = QtGui.QSpacerItem(578, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem6 = QtGui.QSpacerItem(20, 252, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_6.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_13.setText(_translate("MainWindow", "Serial No :", None))
        self.label_11.setText(_translate("MainWindow", "Model No", None))
        self.label.setText(_translate("MainWindow", "H/W Version", None))
        self.label_2.setText(_translate("MainWindow", "S/W Version", None))
        self.label_6.setText(_translate("MainWindow", "Card Information", None))
        self.label_4.setText(_translate("MainWindow", "No of Points", None))
        self.label_5.setText(_translate("MainWindow", "KT00001", None))
        self.label_3.setText(_translate("MainWindow", "Harness Analyzer 2.0", None))
        self.label_8.setText(_translate("MainWindow", "Gen2.0", None))
        self.label_12.setText(_translate("MainWindow", "V1.0", None))
        self.pushButton.setToolTip(_translate("MainWindow", "Open Serial Port", None))
        self.pushButton.setText(_translate("MainWindow", " Card Status ", None))

import resource_rc
