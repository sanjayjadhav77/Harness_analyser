import sys
##sys.path.insert(1, '/home/pi/Desktop/AWHT/code/tester_files')
import os
from global_files import*
from PyQt4 import QtCore, QtGui
import Cutting_Window
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from  Sql_db import *
import global_test_var as GV
import global_var 
##from cutting_main import*

class cutting_main(QtGui.QMainWindow,Cutting_Window.Ui_MainWindow):      # class of abt_tester page

    def __init__(self):
        super(cutting_main,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.loaddatatotable)
##        self.pushButton_3.clicked.connect(self.close_window)
    def close_window(self):
        global_var.state_machine = 17
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
    def loaddatatotable(self):
        self.file_name=QFileDialog.getOpenFileName(self, 'Open file', '/home/pi/Desktop/')
        print("file_name",self.file_name)
        if(GV.stage==1):
            DeleteHarnessData(GV.Location_No)
        print("import from cuttin chart.....",GV.From_Temp)
        From_pos=int(self.lineEdit_2.text())
        Cavity_no_pos=int(self.lineEdit.text())
        To_pos=int(self.lineEdit_3.text())
        Cavity_no1_pos=int(self.lineEdit_4.text())
        Name_pos=int(self.lineEdit_5.text())
        Color_pos=int(self.lineEdit_6.text())
        WireGauge_pos=int(self.lineEdit_7.text())
        Splice_name=str(self.lineEdit_8.text())
        Splice_name=str(Splice_name)
        path=str(self.file_name)
##        print("Arguments",type(From_pos),Cavity_no_pos,To_pos,Cavity_no1_pos,Name_pos,Color_pos,Splice_name,path)
        CuttingChart_import(From_pos,Cavity_no_pos,To_pos,Cavity_no1_pos,Name_pos,Color_pos,WireGauge_pos,Splice_name,path)
        
        self.hrn_table.clear()
        for i in range(len(GV.From_Temp)):
            self.hrn_table.setItem(i,0, QTableWidgetItem(str(GV.From_Temp[i])))
            self.hrn_table.setItem(i,1, QTableWidgetItem(str(GV.To_Temp[i])))
            self.hrn_table.setItem(i,2, QTableWidgetItem(str(GV.Name_Temp[i])))
            self.hrn_table.setItem(i,3, QTableWidgetItem(str(GV.Color_Temp[i])))
            self.hrn_table.setItem(i,4, QTableWidgetItem(str(GV.WireGauge_Temp[i])))

            
        Type = 'Continuity'
        UploadCutting_ChartData(GV.Location_No,Type,GV.Name_Temp,GV.From_Temp,GV.To_Temp,GV.Color_Temp)
    
        
##def main():
##    app = QtGui.QApplication(sys.argv)
##    app.setApplicationName('phonon Player')
##    f = cutting_main()
##    f.show()
##    app.exec_()
##    sys.exit(app.exec_())
##
##if __name__ == '__main__':
##    main()
