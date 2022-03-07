# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/mainHA.ui'
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
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgba(238, 238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.test = QtGui.QDockWidget(self.frame)
        self.test.setEnabled(True)
        self.test.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);\n"
""))
        self.test.setFloating(False)
        self.test.setFeatures(QtGui.QDockWidget.DockWidgetMovable)
        self.test.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.test.setWindowTitle(_fromUtf8(""))
        self.test.setObjectName(_fromUtf8("test"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.test.setWidget(self.dockWidgetContents)
        self.gridLayout_2.addWidget(self.test, 1, 0, 1, 1)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_16.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem1)
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(24, 24))
        self.pushButton_3.setMaximumSize(QtCore.QSize(24, 24))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setStyleSheet(_fromUtf8(""))
        self.pushButton_3.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/final_assets/close-button-png-27.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 30))
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_16.addWidget(self.pushButton_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(281, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setMinimumSize(QtCore.QSize(276, 16))
        self.label_16.setMaximumSize(QtCore.QSize(275, 16))
        self.label_16.setStyleSheet(_fromUtf8("color: rgb(169, 169, 169);\n"
"font: 8pt \"Roboto Condensed\";"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout.addWidget(self.label_16)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(281, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 28))
        self.menubar.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);\n"
"color: rgb(0,0,0);\n"
"border: 1px solid #00;"))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setStyleSheet(_fromUtf8("background-color: rgb(49, 49, 49);\n"
"color: rgb(255, 255, 255);"))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setStyleSheet(_fromUtf8("background-color: rgb(49, 49, 49);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuReports = QtGui.QMenu(self.menubar)
        self.menuReports.setStyleSheet(_fromUtf8("background-color: rgb(49, 49, 49);\n"
"color: rgb(255, 255, 255);"))
        self.menuReports.setObjectName(_fromUtf8("menuReports"))
        MainWindow.setMenuBar(self.menubar)
        self.actionSelect_Harness = QtGui.QAction(MainWindow)
        self.actionSelect_Harness.setObjectName(_fromUtf8("actionSelect_Harness"))
        self.actionSplice_Visualization = QtGui.QAction(MainWindow)
        self.actionSplice_Visualization.setObjectName(_fromUtf8("actionSplice_Visualization"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout_KalpTech = QtGui.QAction(MainWindow)
        self.actionAbout_KalpTech.setObjectName(_fromUtf8("actionAbout_KalpTech"))
        self.actionLicence_And_Legality = QtGui.QAction(MainWindow)
        self.actionLicence_And_Legality.setObjectName(_fromUtf8("actionLicence_And_Legality"))
        self.actionProduct_Help = QtGui.QAction(MainWindow)
        self.actionProduct_Help.setObjectName(_fromUtf8("actionProduct_Help"))
        self.actionDevice_Details = QtGui.QAction(MainWindow)
        self.actionDevice_Details.setObjectName(_fromUtf8("actionDevice_Details"))
        self.actionProduction_Logs = QtGui.QAction(MainWindow)
        self.actionProduction_Logs.setObjectName(_fromUtf8("actionProduction_Logs"))
        self.actionTest_Reports = QtGui.QAction(MainWindow)
        self.actionTest_Reports.setObjectName(_fromUtf8("actionTest_Reports"))
        self.actionSupervisor_Login = QtGui.QAction(MainWindow)
        self.actionSupervisor_Login.setObjectName(_fromUtf8("actionSupervisor_Login"))
        self.menuFile.addAction(self.actionSelect_Harness)
        self.menuFile.addAction(self.actionSplice_Visualization)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSupervisor_Login)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_KalpTech)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDevice_Details)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionLicence_And_Legality)
        self.menuHelp.addAction(self.actionProduct_Help)
        self.menuReports.addAction(self.actionProduction_Logs)
        self.menuReports.addAction(self.actionTest_Reports)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Close window", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">sales@kalptechsolutions.com</span></p></body></html>", None))
        self.label_16.setText(_translate("MainWindow", "Copyright © 2019 Kalptech solutions Pvt Ltd. All rights reserved.", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"http://www.kalptechsolutions.com/\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">www.kalptechsolutions.com</span></a></p></body></html>", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "He&lp", None))
        self.menuReports.setTitle(_translate("MainWindow", "&Reports", None))
        self.actionSelect_Harness.setText(_translate("MainWindow", "&Select Location", None))
        self.actionSplice_Visualization.setText(_translate("MainWindow", "Splice &Visualization", None))
        self.actionExit.setText(_translate("MainWindow", "&Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionAbout_KalpTech.setText(_translate("MainWindow", "&About KalpTech", None))
        self.actionLicence_And_Legality.setText(_translate("MainWindow", "&Licence And Legality", None))
        self.actionProduct_Help.setText(_translate("MainWindow", "&Product Help", None))
        self.actionDevice_Details.setText(_translate("MainWindow", "Device Details", None))
        self.actionProduction_Logs.setText(_translate("MainWindow", "Production Logs", None))
        self.actionTest_Reports.setText(_translate("MainWindow", "Test Reports", None))
        self.actionSupervisor_Login.setText(_translate("MainWindow", "Supervisor Login", None))
        self.actionSupervisor_Login.setShortcut(_translate("MainWindow", "Ctrl+L", None))

import resource_rc
