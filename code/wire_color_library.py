# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/wire_color_library.ui'
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
        MainWindow.resize(1516, 800)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(175, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(181, 22))
        self.label_4.setMaximumSize(QtCore.QSize(181, 22))
        self.label_4.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem1 = QtGui.QSpacerItem(1150, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.tableWidget_2 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(350, 100))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(500, 586))
        self.tableWidget_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableWidget_2.setStyleSheet(_fromUtf8("font: 25 14pt \"Roboto [GOOG]\";"))
        self.tableWidget_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWidget_2.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidget_2.setMidLineWidth(2)
        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setRowCount(2048)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(188, 188, 188))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(180, 180, 180))
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(82)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)
        self.horizontalLayout_7.addWidget(self.tableWidget_2)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(300, 200))
        self.frame.setMaximumSize(QtCore.QSize(641, 401))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(129, 37))
        self.pushButton_2.setMaximumSize(QtCore.QSize(129, 37))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Page_Toggle/page_unselect_facility.png);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(124, 33))
        self.lineEdit.setMaximumSize(QtCore.QSize(120, 33))
        self.lineEdit.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem3 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.Enter_btn_2 = QtGui.QPushButton(self.frame)
        self.Enter_btn_2.setMinimumSize(QtCore.QSize(129, 37))
        self.Enter_btn_2.setMaximumSize(QtCore.QSize(123, 37))
        self.Enter_btn_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Enter_btn_2.setStyleSheet(_fromUtf8("border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.Enter_btn_2.setFlat(True)
        self.Enter_btn_2.setObjectName(_fromUtf8("Enter_btn_2"))
        self.horizontalLayout.addWidget(self.Enter_btn_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem5 = QtGui.QSpacerItem(362, 14, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(127, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(127, 42))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-image: url(:/images/final_assets/Main_Btn/btn_normal.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Roboto [GOOG]\";"))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.frame)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "List of Existing Colors", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Color Name", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Color Shade", None))
        self.pushButton_2.setText(_translate("MainWindow", "Add Color", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Name", None))
        self.Enter_btn_2.setText(_translate("MainWindow", "Select Color", None))
        self.pushButton_3.setText(_translate("MainWindow", "SAVE", None))

import resource_rc