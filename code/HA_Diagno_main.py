import sys
sys.path.insert(1, '/home/pi/Desktop/.HA_Editor/code/tester_files')
import os
from PyQt4 import QtCore, QtGui, uic
import HA_Diagnostics
import global_var
from global_files import*
import global_test_var as GV
from  Sql_db import *
from HDM import *


class HA_dignostics_window(QtGui.QMainWindow, HA_Diagnostics.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        Get_num_stages(GV.Location_No)
        self.comboBox.clear()
        self.comboBox.addItem("Show Stage Point")
        # for i in range(int(GV.Num_Stages)):
        #     self.comboBox.insertItem(i+2, str(i+1))
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
        self.comboBox.currentIndexChanged.connect(self.ShowPoints)
        

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
            GV.data_Available=11    
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
        # print("GV.circuits.........",GV.circuits)
        card_init()       
        if (global_var.ch_b==1):
            global_var.ch_b=0
           
           
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
            
            GV.Check_bypass=1
            GV.checkboard_to_engine=1
            GV.Intruption_flag=0
            GV.module_no=2
            
            
        elif (global_var.ch_b==0):
            print("global_var.ch_b",global_var.ch_b)
            self.tableWidget.clear()
            global_var.ch_b=1
            GV.checkboard_list=[]            
            self.label_4.clear()
            self.tableWidget.clear()    
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
            if(GV.Check_bypass==1):
                GV.module_no=0
                GV.Check_bypass=0
            else:
                GV.checkboard_to_engine=1
                GV.module_no=8
                GV.Intruption_flag=1

    def conti_pts(self,event):
        if(global_var.cont==1):
            global_var.cont=0
            GV.module_no=6

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



    def show_grp_pts(self,event):
        if (global_var.sh_gpt==1):
            global_var.sh_gpt=0

            GV.data_Available=12
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
            self.frame.setEnabled(True)
            self.label_4.setEnabled(True)
            self.label_5.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.frame_5.setEnabled(True)
            self.label_20.setEnabled(True)

            self.frame_6.setEnabled(True)
            self.label_21.setEnabled(True)
            self.label_25.setEnabled(True)


            self.label_50.setEnabled(True)

    def self_tst(self,event):
        if (global_var.s_t==1):
            global_var.s_t=0
            GV.module_no=7
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
            self.frame.setEnabled(True)
            self.label_4.setEnabled(True)
            self.label_5.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.frame_4.setEnabled(True)
            self.label_19.setEnabled(True)

            self.frame_6.setEnabled(True)
            self.label_21.setEnabled(True)
            self.label_25.setEnabled(True)


            self.label_24.setEnabled(True)



def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Diagnostics')
    f = HA_dignostics_window()
    f.show()
    app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
