import sys
import os
from PyQt4 import QtCore, QtGui
import wire_color_library
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import global_var 
from global_files import*
import global_test_var as GV
from  Sql_db import *
import numpy as np
class wirecolor(QtGui.QMainWindow, wire_color_library.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.lineEdit.hide()
        self.Enter_btn_2.hide()
        self.pushButton_3.hide()

        self.rgb=tuple()
        self.pushButton_2.clicked.connect(self.Add_Color)
        self.Enter_btn_2.clicked.connect(self.Select_Color)
        self.pushButton_3.clicked.connect(self.Save_Color)
        self.output=Downloadwirecolor()
##        print("output",output)
        self.writetoTable(self.output)
##        self.pushButton_4.clicked.connect(self.close_window)
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)

    def popupmeassage(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(self.quit_msg )
        msgBox.setWindowTitle("Message")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            msgBox.close() 
        if returnValue == QMessageBox.Cancel:
            msgBox.close()   
    def writetoTable(self,output):
##        self.tableWidget_2.clear()
        for i in range(len(output)):
            Color_Name=output[i][0]
            Color_Shade=eval(output[i][1])
            self.tableWidget_2.setItem(i,0, QTableWidgetItem(str(Color_Name)))
            self.tableWidget_2.setItem(i,1, QTableWidgetItem(str(Color_Shade)))
    def Add_Color(self):
        self.lineEdit.show()
        self.Enter_btn_2.show()
        self.pushButton_3.show()
        
    def Select_Color(self):
        color = QtGui.QColorDialog.getColor()
        self.rgb = tuple([color.red(),color.green(),color.blue()])
        
    def Save_Color(self):
        
        ColorName = self.lineEdit.text()
        ColorShade = self.rgb
##        print("ColorName,ColorShade",ColorName,ColorShade)
##        print("output",self.output)
        z=list((np.zeros(len(self.output),dtype='i')))
        print("before",z)
        for i in range (len(self.output)):
##            print("self.output[i][1]",self.output[i][1],ColorShade)
            if(len(ColorName)>0  and any(ColorShade)==True):
                if(ColorName  in self.output[i]):
                    z[i]=0
                elif((str(ColorShade) == self.output[i][1])==True):
                    z[i]=0
                else:
                    z[i]=1
                    



                    

        print("After",z)    
        if(z.count(z[0]) == len(z)) :
            if (z[0]==1):
                
                Uploadwirecolor(ColorName,ColorShade)
                self.lineEdit.hide()
                self.Enter_btn_2.hide()
                self.pushButton_3.hide()
                self.lineEdit.clear()
                self.output=Downloadwirecolor()
                
                self.writetoTable(self.output)
                ColorShade=tuple()
            else:
                self.quit_msg = " Color Name OR Color Not Selected " 
                self.popupmeassage()
                ColorShade=tuple()

        else:
            self.quit_msg = " Color or Shade Already Present " 
            self.popupmeassage()
            ColorShade=tuple()
##def main():
##    app = QtGui.QApplication(sys.argv)
##    app.setApplicationName('Wire Color')
##    f = wirecolor()
##    f.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
