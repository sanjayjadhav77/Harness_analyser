# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/HA_Editor/UI_files/admin_page.ui'
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
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(650, 250))
        self.frame.setMaximumSize(QtCore.QSize(911, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_6 = QtGui.QPushButton(self.frame)
        self.pushButton_6.setMinimumSize(QtCore.QSize(150, 90))
        self.pushButton_6.setMaximumSize(QtCore.QSize(293, 112))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setStyleSheet(_fromUtf8("\n"
"font: 25 24pt \"Roboto [GOOG]\";\n"
"\n"
""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("final_assets/Dashboard_btn/teaching_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 90))
        self.pushButton_4.setMaximumSize(QtCore.QSize(293, 112))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setStyleSheet(_fromUtf8("\n"
"font: 25 24pt \"Roboto [GOOG]\";\n"
""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("final_assets/Dashboard_btn/diag_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(79, 80))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 90))
        self.pushButton.setMaximumSize(QtCore.QSize(293, 112))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet(_fromUtf8("\n"
"font: 25 24pt \"Roboto [GOOG]\";\n"
""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("final_assets/Dashboard_btn/config_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(82, 80))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 125, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_5 = QtGui.QPushButton(self.frame)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 90))
        self.pushButton_5.setMaximumSize(QtCore.QSize(293, 112))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setStyleSheet(_fromUtf8("\n"
"font: 25 23pt \"Roboto [GOOG]\";\n"
""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("final_assets/Dashboard_btn/mng_grp_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(82, 80))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 90))
        self.pushButton_3.setMaximumSize(QtCore.QSize(293, 112))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setStyleSheet(_fromUtf8("\n"
"font: 25 24pt \"Roboto [GOOG]\";\n"
""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("final_assets/Dashboard_btn/testing_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QtCore.QSize(89, 80))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 90))
        self.pushButton_2.setMaximumSize(QtCore.QSize(293, 112))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet(_fromUtf8("\n"
"font: 25 24pt \"Roboto [GOOG]\";\n"
""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("final_assets/Dashboard_btn/help_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setMinimumSize(QtCore.QSize(281, 16))
        self.label_16.setMaximumSize(QtCore.QSize(281, 16))
        self.label_16.setStyleSheet(_fromUtf8("color: rgb(169, 169, 169);\n"
"font: 8pt \"Roboto Condensed\";"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_3.addWidget(self.label_16)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_6.setText(_translate("MainWindow", "Teaching", None))
        self.pushButton_4.setText(_translate("MainWindow", "Diagnostic", None))
        self.pushButton.setText(_translate("MainWindow", "Configuration", None))
        self.pushButton_5.setText(_translate("MainWindow", "Manage Group", None))
        self.pushButton_3.setText(_translate("MainWindow", "Testing", None))
        self.pushButton_2.setText(_translate("MainWindow", "Help", None))
        self.label_16.setText(_translate("MainWindow", "Copyright © 2019 Kalptech solutions Pvt Ltd. All rights reserved.", None))

