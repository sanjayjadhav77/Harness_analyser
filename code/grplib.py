# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/.HA_Editor/UI_files/grplib.ui'
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
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(70, 10))
        self.label_2.setMaximumSize(QtCore.QSize(87, 24))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_3.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(70, 0))
        self.label_4.setMaximumSize(QtCore.QSize(87, 24))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.verticalLayout_5.addWidget(self.lineEdit_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setMinimumSize(QtCore.QSize(70, 0))
        self.label_16.setMaximumSize(QtCore.QSize(110, 24))
        self.label_16.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_7.addWidget(self.label_16)
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.lineEdit_6.setText(_fromUtf8(""))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.verticalLayout_7.addWidget(self.lineEdit_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setMinimumSize(QtCore.QSize(33, 0))
        self.label_18.setMaximumSize(QtCore.QSize(132, 24))
        self.label_18.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_8.addWidget(self.label_18)
        self.comboBox_9 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_9.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.verticalLayout_8.addWidget(self.comboBox_9)
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.verticalLayout_8.addWidget(self.spinBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setMinimumSize(QtCore.QSize(20, 0))
        self.label_20.setMaximumSize(QtCore.QSize(122, 22))
        self.label_20.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_10.addWidget(self.label_20)
        self.comboBox_7 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_7.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.verticalLayout_10.addWidget(self.comboBox_7)
        self.spinBox_2 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_2.setMaximum(9999)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.verticalLayout_10.addWidget(self.spinBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setMinimumSize(QtCore.QSize(60, 0))
        self.label_17.setMaximumSize(QtCore.QSize(103, 22))
        self.label_17.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_3.addWidget(self.label_17)
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.spinBox_3 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_3.setMaximum(9999)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.verticalLayout_3.addWidget(self.spinBox_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setMinimumSize(QtCore.QSize(67, 0))
        self.label_22.setMaximumSize(QtCore.QSize(109, 22))
        self.label_22.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_12.addWidget(self.label_22)
        self.comboBox_4 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_4.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.verticalLayout_12.addWidget(self.comboBox_4)
        self.spinBox_4 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_4.setMaximum(9999)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.verticalLayout_12.addWidget(self.spinBox_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setMinimumSize(QtCore.QSize(62, 0))
        self.label_21.setMaximumSize(QtCore.QSize(86, 22))
        self.label_21.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_11.addWidget(self.label_21)
        self.comboBox_5 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_5.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.verticalLayout_11.addWidget(self.comboBox_5)
        self.spinBox_5 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_5.setMaximum(9999)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.verticalLayout_11.addWidget(self.spinBox_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setMinimumSize(QtCore.QSize(63, 0))
        self.label_23.setMaximumSize(QtCore.QSize(95, 22))
        self.label_23.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_13.addWidget(self.label_23)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_13.addWidget(self.comboBox)
        self.spinBox_6 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_6.setMaximum(9999)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.verticalLayout_13.addWidget(self.spinBox_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setMinimumSize(QtCore.QSize(72, 0))
        self.label_19.setMaximumSize(QtCore.QSize(119, 22))
        self.label_19.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_9.addWidget(self.label_19)
        self.comboBox_6 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_6.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.verticalLayout_9.addWidget(self.comboBox_6)
        self.spinBox_7 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_7.setMaximum(9999)
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.verticalLayout_9.addWidget(self.spinBox_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(250, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(300, 300))
        self.label.setMaximumSize(QtCore.QSize(300, 400))
        self.label.setStyleSheet(_fromUtf8("border-color: rgb(13, 13, 13);"))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_25 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_8.addWidget(self.label_25)
        self.comboBox_8 = QtGui.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.horizontalLayout_8.addWidget(self.comboBox_8)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_6.addWidget(self.label_15)
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.verticalLayout_6.addWidget(self.lineEdit_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 50, 255);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_14.addWidget(self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_14.addWidget(self.lineEdit_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_14)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(117)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(36)
        self.tableWidget.verticalHeader().setMinimumSectionSize(12)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_15.addWidget(self.tableWidget)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_15.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_15)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(289, 54))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("color: rgb(38,177,255);\n"
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Group No.</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Module Type</span></p></body></html>", None))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Fixture Position</span></p></body></html>", None))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">LeakagetestStatus</span></p></body></html>", None))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "No", None))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Yes", None))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">NavigationStatus</span></p></body></html>", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "No", None))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Yes", None))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">ConnPresence</span></p></body></html>", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "No", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Yes", None))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">SecondaryLock</span></p></body></html>", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "No", None))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Yes", None))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">SensorInput</span></p></body></html>", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "No", None))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Yes", None))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">EjectorStatus</span></p></body></html>", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "No", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Yes", None))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">FixtureActivation</span></p></body></html>", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "No", None))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Yes", None))
        self.label.setText(_translate("MainWindow", "                                                                                                                                            Image                                                                                                                                                                                            ", None))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Connector Library:</span></p></body></html>", None))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Connector Name</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Number of cavity</span></p></body></html>", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cavity", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Point", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "HW_pin", None))
        self.pushButton_2.setText(_translate("MainWindow", "Save Data", None))

import resource_rc
