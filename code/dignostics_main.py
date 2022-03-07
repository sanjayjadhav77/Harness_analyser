import sys
sys.path.insert(1, '/home/pi/Desktop/.HA_Editor/code/tester_files')
import os
from PyQt4 import QtCore, QtGui, uic
import Diagnostics
import global_var
from global_files import*
import global_test_var as GV
from  Sql_db import *
global checkboard_to_engine
checkboard_to_engine=0



class dignostics_window(QtGui.QMainWindow, Diagnostics.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.frame.mousePressEvent=self.checkborad_1
        self.label_4.mousePressEvent=self.checkborad_1
        self.label_5.mousePressEvent=self.checkborad_1

        self.frame_6.mousePressEvent=self.conti_pts
        self.label_21.mousePressEvent=self.conti_pts
        self.label_25.mousePressEvent=self.conti_pts
        

        self.frame_4.mousePressEvent=self.show_grp_pts
        self.label_19.mousePressEvent=self.show_grp_pts
        self.label_24.mousePressEvent=self.show_grp_pts

        self.frame_5.mousePressEvent=self.self_tst
        self.label_50.mousePressEvent=self.self_tst        
        self.label_20.mousePressEvent=self.self_tst
        self.comboBox.addItems(str(GV.stage_list)) 
        self.comboBox.currentIndexChanged.connect(self.ShowPoints)
##        self.pushButton_3.clicked.connect(self.close_window)
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)

    def ShowPoints(self,event):
        self.tableWidget.clear()
        
        if(self.comboBox.currentIndex()==0):
            self.tableWidget.clear()

            self.frame.setEnabled(True)
            self.label_4.setEnabled(True)
            self.label_5.setEnabled(True)
        
            self.frame_4.setEnabled(True)
            self.label_19.setEnabled(True)
            
            self.frame_5.setEnabled(True)
            self.label_20.setEnabled(True)
            self.label_24.setEnabled(True)

            self.frame_6.setEnabled(True)
            self.label_21.setEnabled(True)
            self.label_25.setEnabled(True)

            self.label_50.setEnabled(True)
        else:
            
            GV.stage=self.comboBox.currentIndex()
            DownloadHarnessData(GV.Location_No,GV.stage)
            
            GV.data_Available=2
            
            self.frame.setEnabled(False)
            self.label_4.setEnabled(False)
            self.label_5.setEnabled(False)
            
            self.frame_4.setEnabled(False)
            self.label_19.setEnabled(False)
            
            self.frame_5.setEnabled(False)
            self.label_20.setEnabled(False)
            self.label_24.setEnabled(False)

            self.frame_6.setEnabled(False)
            self.label_21.setEnabled(False)
            self.label_25.setEnabled(False)
            
            self.label_50.setEnabled(False)
    def checkborad_1(self,event):
        print("GV.circuits",GV.circuits)
        
        global checkboard_to_engine
        
        if (global_var.ch_b==1):
            global_var.ch_b=0
            GV.module_no=1

            self.comboBox.setEnabled(False)
            self.frame_4.setEnabled(False)
            self.label_19.setEnabled(False)
            
            self.frame_5.setEnabled(False)
            self.label_20.setEnabled(False)
            self.label_24.setEnabled(False)

            self.frame_6.setEnabled(False)
            self.label_21.setEnabled(False)
            self.label_25.setEnabled(False)
            
            self.label_50.setEnabled(False)
 
            
            self.pixmap = QPixmap(":/images/final_assets/Checkbox/check.png")
            
            self.label_4.setPixmap(self.pixmap)
            
            
        elif (global_var.ch_b==0):
            print("global_var.ch_b",global_var.ch_b)
            global_var.ch_b=1
##            GV.checkboard_flag=0
            self.tableWidget.clear()
            GV.module_no=0
            
            self.label_4.clear()

            self.comboBox.setEnabled(True)
            self.frame_4.setEnabled(True)
            self.label_19.setEnabled(True)
            
            self.frame_5.setEnabled(True)
            self.label_20.setEnabled(True)
            self.label_24.setEnabled(True)

            self.frame_6.setEnabled(True)
            self.label_21.setEnabled(True)
            self.label_25.setEnabled(True)

            self.label_50.setEnabled(True)

    def conti_pts(self,event):
        if(global_var.cont==1):
            global_var.cont=0
            GV.module_no=5
            self.comboBox.setEnabled(False)
            self.frame_4.setEnabled(False)
            self.label_19.setEnabled(False)
            
            self.frame_5.setEnabled(False)
            self.label_20.setEnabled(False)
            self.label_24.setEnabled(False)

            self.frame.setEnabled(False)
            self.label_4.setEnabled(False)
            self.label_5.setEnabled(False)
            
            self.label_50.setEnabled(False)

            self.pixmap = QPixmap(":/images/final_assets/Checkbox/check.png")
            self.label_21.setPixmap(self.pixmap)

            
        elif(global_var.cont==0):
            global_var.cont=1
            self.label_21.clear()
            self.tableWidget.clear()
 
            self.comboBox.setEnabled(True)
            self.frame_4.setEnabled(True)
            self.label_19.setEnabled(True)
            
            self.frame_5.setEnabled(True)
            self.label_20.setEnabled(True)
            self.label_24.setEnabled(True)

            self.frame.setEnabled(True)
            self.label_4.setEnabled(True)
            self.label_5.setEnabled(True)

            self.label_50.setEnabled(True) 


    def show_pts(self,event):
        if (global_var.sh_pt==1):
            global_var.sh_pt=0
            GV.data_Available=2
            print("flag set",global_var.sh_pt)
            self.comboBox.setEnabled(False)
            self.frame.setEnabled(False)
            self.label_4.setEnabled(False)
            
            self.frame_4.setEnabled(False)
            self.label_19.setEnabled(False)
            self.label_5.setEnabled(False)
            
            self.frame_5.setEnabled(False)
            self.label_20.setEnabled(False)
            self.label_24.setEnabled(False)

            self.frame_6.setEnabled(False)
            self.label_21.setEnabled(False)
            self.label_25.setEnabled(False)
            
            self.label_50.setEnabled(False)
            self.pixmap = QPixmap(":/images/final_assets/Checkbox/check.png")
            self.label_14.setPixmap(self.pixmap)
##            
        elif (global_var.sh_pt==0):
            global_var.sh_pt=1
            self.comboBox.setEnabled(True)
            self.label_14.clear()
            self.tableWidget.clear()
            self.frame.setEnabled(True)
            self.label_4.setEnabled(True)
            
            self.frame_4.setEnabled(True)
            self.label_19.setEnabled(True)
            self.label_5.setEnabled(True)
            
            self.frame_5.setEnabled(True)
            self.label_20.setEnabled(True)
            self.label_24.setEnabled(True)

            self.frame_6.setEnabled(True)
            self.label_21.setEnabled(True)
            self.label_25.setEnabled(True)


            self.label_50.setEnabled(True)

    def show_grp_pts(self,event):
        if (global_var.sh_gpt==1):
            global_var.sh_gpt=0

            GV.data_Available=6
            self.frame.setEnabled(False)
            self.label_4.setEnabled(False)
            
            self.comboBox.setEnabled(False)
            self.label_5.setEnabled(False)
            
            self.frame_5.setEnabled(False)
            self.label_20.setEnabled(False)

            self.frame_6.setEnabled(False)
            self.label_21.setEnabled(False)
            self.label_25.setEnabled(False)
            
            self.label_50.setEnabled(False)
            self.pixmap = QPixmap(":/images/final_assets/Checkbox/check.png")
            self.label_19.setPixmap(self.pixmap)
            
            
            
        elif (global_var.sh_gpt==0):
            global_var.sh_gpt=1
            self.label_19.clear()
            self.tableWidget.clear()
            self.comboBox.setEnabled(True)
            self.frame.setEnabled(True)
            self.label_4.setEnabled(True)
            
            self.label_5.setEnabled(True)
            
            self.frame_5.setEnabled(True)
            self.label_20.setEnabled(True)

            self.frame_6.setEnabled(True)
            self.label_21.setEnabled(True)
            self.label_25.setEnabled(True)


            self.label_50.setEnabled(True)

    def self_tst(self,event):
        if (global_var.s_t==1):
            global_var.s_t=0
            GV.module_no=3
            self.comboBox.setEnabled(False)
            self.frame.setEnabled(False)
            self.label_4.setEnabled(False)
            self.label_5.setEnabled(False)
            
            self.frame_4.setEnabled(False)
            self.label_19.setEnabled(False)

            self.frame_6.setEnabled(False)
            self.label_21.setEnabled(False)
            self.label_25.setEnabled(False)
            
            self.label_24.setEnabled(False)
            self.pixmap = QPixmap(":/images/final_assets/Checkbox/check.png")
            self.label_20.setPixmap(self.pixmap)
            
        elif (global_var.s_t==0):
            global_var.s_t=1
            self.label_20.clear()
            self.tableWidget.clear()
            self.comboBox.setEnabled(True)
            self.frame.setEnabled(True)
            self.label_4.setEnabled(True)
            
            self.label_5.setEnabled(True)
            
            self.frame_4.setEnabled(True)
            self.label_19.setEnabled(True)

            self.frame_6.setEnabled(True)
            self.label_21.setEnabled(True)
            self.label_25.setEnabled(True)


            self.label_24.setEnabled(True)



def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Diagnostics')
    f = dignostics_window()
    f.show()
    app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
