# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/teaching_4.ui'
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
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.grp2_table = QtGui.QTableWidget(self.centralwidget)
        self.grp2_table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.grp2_table.setStyleSheet(_fromUtf8("font: 25 14pt \"Roboto [GOOG]\";"))
        self.grp2_table.setFrameShape(QtGui.QFrame.NoFrame)
        self.grp2_table.setFrameShadow(QtGui.QFrame.Plain)
        self.grp2_table.setMidLineWidth(2)
        self.grp2_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.grp2_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.grp2_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.grp2_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.grp2_table.setShowGrid(True)
        self.grp2_table.setGridStyle(QtCore.Qt.SolidLine)
        self.grp2_table.setRowCount(128)
        self.grp2_table.setColumnCount(128)
        self.grp2_table.setObjectName(_fromUtf8("grp2_table"))
        self.grp2_table.horizontalHeader().setVisible(False)
        self.grp2_table.horizontalHeader().setDefaultSectionSize(80)
        self.grp2_table.horizontalHeader().setMinimumSectionSize(80)
        self.grp2_table.verticalHeader().setVisible(True)
        self.grp2_table.verticalHeader().setMinimumSectionSize(30)
        self.gridLayout.addWidget(self.grp2_table, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(81, 22))
        self.label.setMaximumSize(QtCore.QSize(81, 22))
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"Roboto Condensed\";\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setStyleSheet(_fromUtf8("font: 75 12pt \"Roboto [GOOG]\";\n"
"color: rgb(0, 0, 0);"))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Group file", None))
        self.checkBox.setText(_translate("MainWindow", "Use Global Group File", None))

import resource_rc
