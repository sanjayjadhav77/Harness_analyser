# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/New_global_group.ui'
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
        MainWindow.resize(1511, 800)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(161, 22))
        self.label.setMaximumSize(QtCore.QSize(161, 22))
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableWidget_2 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableWidget_2.setStyleSheet(_fromUtf8("font: 25 16pt \"Roboto [GOOG]\";"))
        self.tableWidget_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWidget_2.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidget_2.setMidLineWidth(2)
        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setRowCount(100)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(153, 153, 153))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(152, 152, 152))
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(152, 152, 152))
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(153, 153, 153))
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(175)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(125, 45))
        self.pushButton.setMaximumSize(QtCore.QSize(125, 45))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet(_fromUtf8("background-image: url(:/images/final_assets/Main_Btn/btn_normal.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(125, 45))
        self.pushButton_2.setMaximumSize(QtCore.QSize(125, 45))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-image: url(:/images/final_assets/Main_Btn/btn_normal.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setMinimumSize(QtCore.QSize(281, 21))
        self.label_16.setMaximumSize(QtCore.QSize(281, 21))
        self.label_16.setStyleSheet(_fromUtf8("color: rgb(169, 169, 169);\n"
"font: 8pt \"Roboto Condensed\";"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout.addWidget(self.label_16)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Select Group Number", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Group No.", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Module Type", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Connector  Name", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fixture Position", None))
        self.pushButton.setText(_translate("MainWindow", "EDIT", None))
        self.pushButton_2.setText(_translate("MainWindow", "ADD", None))
        self.label_16.setText(_translate("MainWindow", "Copyright © 2019 Kalptech solutions Pvt Ltd. All rights reserved.", None))

import resource_rc
