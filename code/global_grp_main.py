import sys
import os
from PyQt4 import QtCore, QtGui
import New_global_group
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from global_var import*
from global_files import*
import global_test_var as GV
from  Sql_db import *

class manage_group(QtGui.QMainWindow, New_global_group.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.read_frm_db()
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton.clicked.connect(self.edit_table)
        self.pushButton_2.clicked.connect(self.add_data)
        self.tableWidget_2.clicked.connect(self.viewClicked)
##        self.pushButton_4.clicked.connect(self.close_main_window)
    def close_main_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)

    def viewClicked(self):
        try:
            self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
            row = self.tableWidget_2.currentRow()
            rw_data=(self.tableWidget_2.item(row,0)).text()
            GV.grp_id=int(rw_data)
            print("GV.grp_id",GV.grp_id)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
        except:
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            print("Blank Row selected")
    
    def edit_table(self):
        global_var.state_machine=11
        GV.GroupEditFlag=1
        global_var.state_machine_flag=1

        print(global_var.state_machine_flag,global_var.state_machine)
        self.pushButton.setStyleSheet("background-image: url(:/images/final_assets/Main_Btn/btn_press.png);color: rgb(255, 255, 255);")        
    def add_data(self):
        print('addd')
        self.pushButton_2.setStyleSheet("background-image: url(:/images/final_assets/Main_Btn/btn_press.png);color: rgb(255, 255, 255);")
        global_var.state_machine=11
        GV.GroupEditFlag=0
        global_var.state_machine_flag=1

        print(global_var.state_machine_flag,global_var.state_machine)
    def read_frm_db(self):
        Grp_1=DownloadGlobal_Grp1()
        for i in range(len(Grp_1)):
            self.tableWidget_2.setItem(i,0, QTableWidgetItem(str(Grp_1[i][0])))
            self.tableWidget_2.setItem(i,1, QTableWidgetItem(str(Grp_1[i][4])))
            self.tableWidget_2.setItem(i,2, QTableWidgetItem(str(Grp_1[i][3])))
            self.tableWidget_2.setItem(i,3, QTableWidgetItem(str(Grp_1[i][2])))
def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('manage_group')
    f = manage_group()
    f.show()
    app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
