#!/usr/bin/python3

#----------------------------------my code----------------------------------#
import sys
sys.path.insert(1, '/home/pi/Desktop/.HA_Editor/code/tester_files')
from global_files import*
import mainHA as mymain
import subprocess
import global_var
from PyQt4.QtCore import QThread
import global_test_var as GV
from Soft_Arct import *
from Test_Engine import *
from HDM import *
from CAN_Bus import *
from main_new_Mdi import *
from  Sql_db import *
GV.System_Shuffle=1
failled_off()
passled_off()
CAN_configuration()
GV.Card_counter=card_status()
print("total_card", GV.Card_counter)
GV.total_point=GV.Card_counter*64
card_init()
GV.is_card_sequential=Card_sequential()
Sqdb_to_Ram(1)
UploadProdLog_Data(GV.Location_No,GV.Part_Name,'Analyser','Reboot')


import threading
thread1 = threading.Thread(target = tester_message_generation, args = ())
thread1.start()
global width 
global height 

class Ui_MainWindow(QtGui.QMainWindow,mymain.Ui_MainWindow):   
    def __init__(self,p1,p2,p3,p4,p5,p6,p7,p8,p12,p13):
        super(Ui_MainWindow,self).__init__()


        self.setupUi(self)
        self.label_2.setOpenExternalLinks(True)
        self.setWindowIcon(QtGui.QIcon(':/images/final_assets/KalpLogo.bmp'))
        self.setWindowTitle("Harness Analyzer")
        self.setGeometry(0, 0, 850, 600)
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
        self.p5=p5
        self.p6=p6
        self.p7=p7
        self.p8=p8
        self.p12=p12
        self.p13=p13
        self.actionSelect_Harness.triggered.connect(self.select_harness)
        self.actionDevice_Details.triggered.connect(self.Device_Details)
        
        self.actionSplice_Visualization.triggered.connect(self.splice_visualization)
        self.actionAbout_KalpTech.triggered.connect(self.about_KT)
        self.actionExit.triggered.connect(self.Exit)
        self.actionProduct_Help.triggered.connect(self.Product_help)
        self.actionLicence_And_Legality.triggered.connect(self.licence_and_legality)
        self.actionTest_Reports.setVisible(False)
        self.actionTest_Reports.triggered.connect(self.Test_Reports)
        self.actionProduction_Logs.triggered.connect(self.Production_Logs)
        self.actionSupervisor_Login.triggered.connect(self.superlogin)
        self.pushButton_3.clicked.connect(self.close_window)
    def popupmeassage(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(self.quit_msg )
        msgBox.setWindowTitle("Message")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.test.setWidget(self.p2)
            # global_var.state_machine=5
            msgBox.close() 
        if returnValue == QMessageBox.Cancel:
            msgBox.close()     
    def superlogin(self):
        GV.PrvEstate=GV.Estate
        self.p8.label.show()
        self.p8.key.setFocus()
        self.p8.pushButton.show()
        self.p8.key.show()
        self.pushButton_3.show()
        self.label_3.setText("SuperVisor Login")
        self.p8.pushButton.setEnabled(True)
        self.p8.key.setEnabled(True)
        GV.Estate=17
        self.test.setWidget(self.p8)        
        self.p8.pushButton_2.hide()
        self.p8.pushButton_4.hide()
        self.p8.pushButton_5.hide()
        self.p8.pushButton_6.hide()
    def close_window(self,event):
        self.pushButton_3.hide()
        self.label_3.clear()
        if(GV.Estate==16):            
            GV.Estate=GV.PrvEstate
            global_var.state_machine_flag=1
            global_var.state_machine=4
        else:    
            self.test.setWidget(self.p1)

        
    def select_harness(self):
        self.pushButton_3.show()
        self.label_3.setText("Select Part Location")
        self.test.setWidget(self.p7)
        
    def Device_Details(self):
        self.pushButton_3.show()
        self.label_3.setText("Device Details")
        self.test.setWidget(self.p2)
        
    def Product_help(self):
        print("help window")
        subprocess.Popen(['xchm /home/pi/Desktop/.HA_Editor/code/HarnessAnalyzerG2.chm', '-1'], shell=True)

    def about_KT(self):
        self.p3.setWindowTitle("About Us ")
        self.p3.show()
        
    def splice_visualization(self):
        self.pushButton_3.show()
        self.label_3.setText("Splice Visualization")
        self.p6.lineEdit_2.setText(str(GV.Location_No))
        self.p6.lineEdit_3.setText(str(GV.Part_Name))
        self.test.setWidget(self.p6)

    def licence_and_legality(self):
        self.p5.setWindowTitle("licence and legality ")
        self.p5.show()
        
    def Test_Reports(self):
        self.pushButton_3.show()
        self.label_3.setText("Test Reports")
        self.p13.get_information()
        self.test.setWidget(self.p13)
    def Production_Logs(self):
        self.pushButton_3.show()
        self.label_3.setText("Production Logs")
        self.test.setWidget(self.p12)

    def Exit(self):
        
        # GV.exit=1
        quit_msg = "Do you want to Exit ?"
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("get out")
            UploadProdLog_Data(GV.Location_No,GV.Part_Name,'ShutDown',"System Off")
            os._exit(0)    
        else:
            pass
        
    @pyqtSlot() # Flag monitoring slot
    def date_time_update(self):
        if(global_var.state_machine==4):
            if(GV.Start_Event_flag==1):
                GV.Start_Event_flag=0
                self.p4.start_process(1)
            if(GV.Abort_Event_flag==1):
                GV.Abort_Event_flag=0
                self.p4.abort_fun(1)
                
        if(global_var.state_machine==111):
            global_var.state_machine=1
       
            
        if(global_var.cable_change_flag==1):
            self.p4.Enter_btn.setEnabled(True)
            self.p4.pushButton_5.setEnabled(True)
            GV.module_no=0
            print('update_ui',global_var.cable_change_flag)
            GV.data_delivered=0
            global_var.cable_change_flag=0
            Sqdb_to_Ram(2)
            

        if(global_var.state_machine_flag==1):
            print("global_var.state_machine",global_var.state_machine)
            global_var.state_machine_flag=0
            if(global_var.state_machine==1):
                if(GV.Card_counter>0 and GV.is_card_sequential==0):
                    self.pushButton_3.hide()
                    self.label_3.clear()
                    self.test.setWidget(self.p1)
                    
                else:
                    if(GV.is_card_sequential==1):
                        self.quit_msg = "Your Card Is not sequential. \n Please check Card sequence.\n Reset Card Click On card status Button  "
                        self.popupmeassage()
                    else:    
                        self.test.setWidget(self.p2)
                        
                    # self.test.setWidget(self.p2)
                    print("test info")
                
                
            elif(global_var.state_machine==4):
                self.p4.p1.comboBox.setEnabled(True)
                self.p4.p1.frame_4.setEnabled(True)
                self.p4.p1.label_19.setEnabled(True)
                self.p4.p1.frame.setEnabled(True)
                self.p4.p1.label_4.setEnabled(True)
                self.p4.p1.label_5.setEnabled(True)
                self.p4.p1.frame_5.setEnabled(True)
                self.p4.p1.label_20.setEnabled(True)
                self.p4.p1.label_24.setEnabled(True)
                self.p4.p1.frame_6.setEnabled(True)
                self.p4.p1.label_21.setEnabled(True)
                self.p4.p1.label_25.setEnabled(True)    
                self.p4.p1.label_50.setEnabled(True)
                self.pushButton_3.show()
                self.p4.p1.comboBox.clear()
                self.p4.p1.comboBox.addItem("Show Stage Point")
                for i in range(int(GV.Num_Stages)):
                    self.p4.p1.comboBox.insertItem(i+2, str(i+1))
                self.p4.pushButton_5.setEnabled(True)
                self.label_3.setText("Testing Window")
                self.p4.label_21.setEnabled(False)
                self.p4.label_10.hide()
                self.p4.fo_qty.hide()
                if(GV.AutoPartLoad=='1' and GV.AssetCodeScan=='1'):
                    global_var.p_s=0
                    self.p4.production_sample()
                elif(GV.AssetCodeScan=='1'):
                    self.p4.label_10.show()
                    self.p4.fo_qty.show()
                    global_var.p_s=1
                    self.p4.production_sample()
                self.p4.read_val_frm_db()
                self.p4.msg_line.setText("Put Cable")
                self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: blue""")
                self.test.setWidget(self.p4)
                print("testing")
                
            elif(global_var.state_machine==5):
                self.test.setWidget(self.p1)
                print("user_land")

            elif(global_var.state_machine==2):
                self.test.setWidget(self.p2)
                print("test info")

            elif(global_var.state_machine==3):
                self.test.setWidget(self.p3)
                print("contact")

            elif(global_var.state_machine==10):
                self.test.setWidget(self.p10)
                print("Diagnostics")
            
            elif(global_var.state_machine==11):
                self.test.setWidget(self.p11)
                print("Cutting Chart")

            elif(global_var.state_machine==7):
                self.test.setWidget(self.p7)
                print("Cable_select Page")
        
    @pyqtSlot()# all engine related message
    def msg_display(self):
         UIEngine_Display(GV.data_delivered,self)
            
    @pyqtSlot() # HA_Editor related mesage
    def msg_structure(self):
##        print("GV.data_Available..........",GV.data_Available)
        if(GV.data_Available!=0):
            GUI_Display(GV.data_Available,self)
            GV.data_Available=0    
    @pyqtSlot()# Connector visual 
    def random_data(self):
##        print("GV.Visual_Engine_Start",GV.Visual_Engine_Start)
        if(GV.Visual_Engine_Start==1):
            rand_data(self.p4)
            GV.Visual_Engine_Start=0
        elif(GV.Visual_Engine_Start==2):
            GV.Visual_Engine_Start=0
            if(GV.All_Error!= 1 ):
                clear_image(self.p4)
        elif(GV.Visual_Engine_Start==3):
            GV.Visual_Engine_Start=0
            put_image(self.p4)
        elif(GV.Visual_Engine_Start==4):
            GV.Visual_Engine_Start=0
            pass_image(self.p4)
        elif(GV.Visual_Engine_Start==5):
            GV.Visual_Engine_Start=0
            wrong_image(self.p4)
        elif(GV.Visual_Engine_Start==6):
            GV.Visual_Engine_Start=0
            release_image(self.p4)
        elif(GV.Visual_Engine_Start==7):
            GV.Visual_Engine_Start=0
            barcode_image(self.p4)
            
def main():
    global width 
    global height
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create("WindowsXP")) 
    screen_resolution = app.desktop().screenGeometry()
    width  = screen_resolution.width() 
    height = screen_resolution.height()
    print("width,height",width,height)
    p1 = Front_win()
    p2 = abt_tester_page()
    p3 = contactUs_page()
    p5 = license_page()
    p6 = Splice_visual()
    p7 = cable_selctionHA()
    p4 = mdiArea_window()
    p8 = Supervisory_login()
    p12 = log_display()
    p13 = Test_Report()
    
    GUI = Ui_MainWindow(p1,p2,p3,p4,p5,p6,p7,p8,p12,p13)
    GUI.show()
    timer = QTimer()
    GUI.connect(timer,SIGNAL("timeout()"),GUI,SLOT("date_time_update()"))
    timer.start(50)

    timer1 = QTimer()
    GUI.connect(timer1,SIGNAL("timeout()"),GUI,SLOT("msg_display()"))
    timer1.start(100)

    timer2 = QTimer()
    GUI.connect(timer2,SIGNAL("timeout()"),GUI,SLOT("msg_structure()"))
    timer2.start(100)

    timer3 = QTimer()
    GUI.connect(timer3,SIGNAL("timeout()"),GUI,SLOT("random_data()"))
    timer3.start(100)
    # GUI.show()
   # GUI.showFullScreen()
    GUI.showMaximized()
    app.exec_()

if __name__ == '__main__':
    main()
# harness analyser
    
