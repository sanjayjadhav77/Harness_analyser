# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/cable_select.ui'
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
        MainWindow.resize(1436, 800)
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
        self.label.setMinimumSize(QtCore.QSize(185, 24))
        self.label.setMaximumSize(QtCore.QSize(185, 21))
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 34))
        self.frame_2.setMaximumSize(QtCore.QSize(105, 34))
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.lineEdit = QtGui.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 200, 32))
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 32))
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 32))
        self.lineEdit.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Secondary_btn/exp_db.png);"))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_4 = QtGui.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(164, 0, 36, 31))
        self.pushButton_4.setMinimumSize(QtCore.QSize(36, 31))
        self.pushButton_4.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_4.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Search_bar/searchIcon.png);"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tableWidget_2 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(650, 100))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(1500, 750))
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
        self.tableWidget_2.setRowCount(128)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(188, 188, 188))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(180, 180, 180))
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(195, 195, 195))
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(185, 185, 185))
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(82)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)
        self.horizontalLayout_5.addWidget(self.tableWidget_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Select Part Location", None))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Search Bar</p></body></html>", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Location", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Part Name", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "1st Stage Point", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "2nd Stage Point", None))

import resource_rc
