#!/usr/bin/python3
'''Harness Editor '''
import sys
sys.path.insert(1, '/home/pi/Desktop/.HA_Editor/code/tester_files')
from global_files import*
import main as mymain
import threading
import global_var
from PyQt4.QtCore import QThread
import global_test_var as GV 
from  Sql_db import *
import subprocess
from Soft_Arct import *
from HDM import *
from CAN_Bus import *
GV.System_Shuffle=0
failled_off()
passled_off()
CAN_configuration()
GV.Card_counter=card_status()
print("total_card", GV.Card_counter)
GV.total_point=GV.Card_counter*64
card_init()
GV.is_card_sequential=Card_sequential()
Sqdb_to_Ram(1)
thread1 = threading.Thread(target = tester_message_generation, args = ())
thread1.start()
UploadSysLog_Data(GV.Location_No,GV.Part_Name,'harness Editor','Reboot')
class Ui_MainWindow(QtGui.QMainWindow,mymain.Ui_HA_Editor):   
    def __init__(self,p0,p1,p2,p3,p4,p5,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p29):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.menuBar.setVisible(False)
        self.label_2.setOpenExternalLinks(True)

        self.setGeometry(0, 0, 800, 600)
        self.p0=p0
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
        self.p5=p5
        self.p7=p7
        self.p8=p8
        self.p9=p9
        self.p10=p10
        self.p11=p11
        self.p12=p12
        self.p13=p13
        self.p14=p14
        self.p15=p15
        self.p16=p16
        self.p17=p17
        self.p18=p18
        self.p19=p19
        self.p20=p20
        self.p21=p21
        self.p22=p22
        self.p23=p23
        self.p24=p24
        self.p25=p25
        self.p26=p26
        self.p27=p27
        self.p29=p29

        
        self.actionNew_Harness.triggered.connect(self.new_harness)
        self.actionSelect_Harness.triggered.connect(self.Select_Harness)
        self.actionSplice_Visualization.triggered.connect(self.Splice_Visualization)
        self.actionExit.triggered.connect(self.Exit)
        self.actionLogout.triggered.connect(self.close_application)
        self.actionDignostics.triggered.connect(self.Dignostics)
        
        self.actionGeneral_Setting.triggered.connect(self.general_settings)
        self.actionLearning_Ckt.triggered.connect(self.ckt_learn)
        self.actionUser_Testing_Flow.triggered.connect(self.Testing_Flow)
        self.actionLabel_and_Brcode_Data.triggered.connect(self.Label_and_Brcode_Data)
        self.actionComponent_Testing.triggered.connect(self.Component_Testing)
        self.actionGroup_Data.triggered.connect(self.Show_Group_Data)
        
        self.actionConnector_Library.triggered.connect(self.Connector_Library)
        self.actionColor_Library.triggered.connect(self.Color_Library)
        self.actionFixture_Library.triggered.connect(self.Fixture_Library)
        self.actionGroup_Library.triggered.connect(self.Group_Library)
        self.actionAdd_Splice.triggered.connect(self.Add_Splice)

        self.actionGeneral_Configuration.triggered.connect(self.gen_config)
        self.actionSystem_Configuration.triggered.connect(self.Sys_config)
        

        self.actionAbout_Kalptech.triggered.connect(self.about_KT)
        self.actionLicence.triggered.connect(self.Licence)
        self.actionDevice_Details.triggered.connect(self.Device_Details)
        self.actionHA_help.triggered.connect(self.HA_help)

        self.actionTest_Reports.triggered.connect(self.Test_Reports)
        self.actionProduction_Logs.triggered.connect(self.Production_Logs)
        self.pushButton_3.clicked.connect(self.close_window)
        self.label_3.setStyleSheet("font: 14pt \"Roboto Condensed\";")
    def popupmeassage(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(self.quit_msg )
        msgBox.setWindowTitle("Message")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.test.setWidget(self.p5)
            global_var.state_machine=5
            msgBox.close() 
        if returnValue == QMessageBox.Cancel:
            msgBox.close()       
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Warning!',
                                            "Are you sure want to logout?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            self.Logout()
        else:
            pass    
    def Logout(self):
        global_var.admin_loginflag=0
        global_var.KT_login=0
        
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Logout','Switch Login')
        
        
        self.p3.sys_label.hide()
        self.label_3.clear()
        self.pushButton_3.hide()
        self.test.setWidget(self.p1)
        print("login page")
        self.menuBar.setVisible(False)
        
    def new_harness(self):
        self.pushButton_3.show()
        self.label_3.setText("New Harness")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'new_harness','new_harness')
        self.p14.read_cable_info_frm_db()
        self.test.setWidget(self.p14)
    def Select_Harness(self):
        self.pushButton_3.show()
        self.label_3.setText("Select Harness")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Select harness','Select harness')
        self.p27.read_cable_info_frm_db()
        self.test.setWidget(self.p27)
    def Dignostics(self):
        self.pushButton_3.show()
        self.label_3.setText("Dignostics")
        self.p21.comboBox.clear()
        self.p21.comboBox.insertItem(0, "Show Stage Point")
        DownloadGlobal_Grp2()
        for i in range(int(GV.Num_Stages)):
            self.p21.comboBox.insertItem(i+1, str(i+1))
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Dignostics','Dignostics')
        self.test.setWidget(self.p21)
    def Splice_Visualization(self):
        self.pushButton_3.show()
        self.label_3.setText("Splice Visualization")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Splice Visualization','Splice Visualization')
        self.p13.lineEdit_2.setText(str(GV.Location_No))
        self.p13.lineEdit_3.setText(str(GV.Part_Name))
        self.test.setWidget(self.p13)
    def general_settings(self):
        self.pushButton_3.show()
        self.label_3.setText("General settings")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'general_settings','general_settings')
        if(str(GV.AssetCodeScan)=='0'):
            self.p15.facilities_2.hide()
        self.p15.lineEdit.setText(str(GV.Location_No))
        self.p15.lineEdit_2.setText(str(GV.Part_Name))
        self.p15.acuation_db_read()
        self.p15.facilities_db_read()
        self.p15.display_data()
        self.test.setWidget(self.p15)
        
    def Component_Testing(self):
        self.pushButton_3.show()
        self.label_3.setText("Component Testing")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Component_Testing','Component_Testing')
        self.p18.readvaluefrom_db()
        self.p18.lineEdit.setText(str(GV.Location_No))
        self.p18.lineEdit_2.setText(str(GV.Part_Name))
        self.test.setWidget(self.p18)
    def Show_Group_Data(self):
        self.pushButton_3.show()
        self.label_3.setText("Group Data")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Show_Group_Data','Show_Group_Data')
        self.test.setWidget(self.p19)
        
    def Add_Splice(self):
        self.p29.comboBox_7.clear()
        self.p29.comboBox_7.addItem("Net Number")
        for i in range(len(GV.circuits)):
            self.p29.comboBox_7.addItem(str(i+1))
        self.pushButton_3.show()
        self.label_3.setText("Add Splice")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Add_Splice','Add_Splice')
        self.test.setWidget(self.p29)    
    def ckt_learn(self):
        self.pushButton_3.show()
        self.label_3.setText("Learning Page")
        self.p17.comboBox_2.clear()
        Get_num_stages(GV.Location_No)
        for i in range(int(GV.Num_Stages)):
            self.p17.comboBox_2.insertItem(i, str(i+1))
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'learn Circuit','learn Circuits')
        self.p17.read_hrn_file_DB(1)
        self.p17.lineEdit.setText(str(GV.Location_No))
        self.p17.lineEdit_2.setText(str(GV.Part_Name))
        self.test.setWidget(self.p17)
    def Testing_Flow(self):
        self.pushButton_3.show()
        self.label_3.setText("Testing Flow")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Testing_Flow','Testing_Flow')
        self.p16.readvaluefrom_db()
        self.p16.lineEdit.setText(str(GV.Location_No))
        self.p16.lineEdit_2.setText(str(GV.Part_Name))
        self.test.setWidget(self.p16)

    def Label_and_Brcode_Data(self):
        self.pushButton_3.show()
        self.label_3.setText("Label and Brcode Data")
        self.p20.textEdit.setEnabled(False)
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Label_and_Brcode_Data','Label_and_Brcode_Data')
        self.test.setWidget(self.p20)
        
    def Group_Library(self):
        self.pushButton_3.show()
        self.label_3.setText("Group Library")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Group_Library','Group_Library')
        self.p23.read_frm_db()
        self.test.setWidget(self.p23)
    def Color_Library(self):
        self.pushButton_3.show()
        self.label_3.setText("Color Library")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Color_Library','Color_Library')
        self.test.setWidget(self.p10)
    def Connector_Library(self):
        self.pushButton_3.show()
        self.label_3.setText("Connector Library")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Connector_Library','Connector_Library')
        self.test.setWidget(self.p9)
    def Fixture_Library(self):
        self.pushButton_3.show()
        self.label_3.setText("Module Library")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Fixture_Library','Fixture_Library')
        self.p12.ShowModuledata()
        self.test.setWidget(self.p12)
        
    def gen_config(self):
        self.label_3.clear()
        self.pushButton_3.show()
        if(GV.AutoPartLoad=='0'):
            self.p3.user_label.hide()
            
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'genaral configuration','genaral configuration')
        self.p3.setsys_config()
        self.test.setWidget(self.p3)
        self.p3.stackedWidget.setCurrentIndex(0)
        self.p3.gen_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_select.png);color: rgb(255, 255, 255);font: 14pt "Roboto [GOOG]";""")
        self.p3.sys_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);font: 14pt "Roboto [GOOG]";""")
        self.p3.user_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);font: 14pt "Roboto [GOOG]";""")

    def Sys_config(self):
        self.label_3.clear()
        self.pushButton_3.show()
        if(GV.AutoPartLoad=='0'):
            self.p3.user_label.hide()
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'System configuration','System configuration')
        self.p3.setsys_config()
        self.test.setWidget(self.p3)
        self.p3.stackedWidget.setCurrentIndex(0)
        self.p3.gen_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_select.png);color: rgb(255, 255, 255);font: 14pt "Roboto [GOOG]";""")
        self.p3.sys_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);font: 14pt "Roboto [GOOG]";""")
        self.p3.user_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);font: 14pt "Roboto [GOOG]";""")

    def Test_Reports(self):
        self.pushButton_3.show()
        self.label_3.setText("Test Reports")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Test_Reports','Test_Reports')
        self.p25.get_information()
        self.test.setWidget(self.p25)
    def Production_Logs(self):
        self.pushButton_3.show()
        self.label_3.setText("Production Logs")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'System_Logs','System_Logs')
        self.test.setWidget(self.p24)
        
    def about_KT(self):
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Show_Group_Data','Show_Group_Data')
        self.p7.setWindowTitle("About Us ")
        self.p7.show()

    def Device_Details(self):
        self.pushButton_3.show()
        self.label_3.setText("About Tester")
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Device_Details','Device_Details')
        self.test.setWidget(self.p5)
    def Licence(self):
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Licence','Licence')
        self.p8.setWindowTitle("licence and legality ")
        self.p8.show()
    def HA_help(self):
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'HA_help','HA_help')
        subprocess.Popen(['xchm /home/pi/Desktop/.HA_Editor/code/HarnessEditorG2.chm', '-1'], shell=True)
        
    def message_lib(self):
        self.pushButton_3.show()
        self.label_3.setText("Message Library")
        self.test.setWidget(self.p26)
        
    
    def Exit(self):
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Exit','Exit')
        quit_msg = "Do you want to Exit ?"
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("get out")
            os._exit(0)
        else:
            pass

    @pyqtSlot() 
    def date_time_update(self):
        
##        print("global_var.state_machine",global_var.state_machine)
        if(global_var.admin_loginflag==1):
            self.menuBar.setVisible(True)
            
##            global_var.admin_loginflag=0
            
        if(global_var.login_flag==1):
##            global_var.login_flag=0          
            self.p3.sys_label.show()
            self.p3.gen_label.show()
            
        if(global_var.KT_login==1):
            self.menuBar.setVisible(True)
            self.actionGeneral_Configuration.setVisible(False) 
            self.actionSystem_Configuration.setVisible(True)
            self.p3.sys_label.show()
            
        if(global_var.KT_login==0):
            self.p3.sys_label.hide()
            self.actionGeneral_Configuration.setVisible(True)
            self.actionSystem_Configuration.setVisible(False)          
      
            
        if(global_var.cable_change_flag==1):
            print('update_ui',global_var.cable_change_flag)
            
            global_var.cable_change_flag=0
            Sqdb_to_Ram(2)
        if(global_var.state_machine_flag==1):
            global_var.state_machine_flag=0
            if(global_var.state_machine==1):
                self.pushButton_3.hide()
                self.label_3.clear()
                self.test.setWidget(self.p0)
                
            elif(global_var.state_machine==111):
                if(GV.Card_counter>0 and GV.is_card_sequential==0):
                    self.label_3.clear()
                    self.pushButton_3.hide()
                    self.test.setWidget(self.p1)
                    print("login page")
                else:
                    if(GV.is_card_sequential==1):
                        self.quit_msg = "Your Card Is not sequential. \n Please check Card sequence.\n Reset Card Click On card status Button  "
                        self.popupmeassage()
                    else:    
                        self.test.setWidget(self.p5)
                        global_var.state_machine=5
                    print("test info")
            elif(global_var.state_machine==2):
                self.p2.newpw_lineedit_2.setFocus()
                self.p2.show()
##                self.test.setWidget(self.p2)
                print("rst")
                
            elif(global_var.state_machine==3):
                self.test.setWidget(self.p3)
                print("admin_config_page")

            elif(global_var.state_machine==4):
                self.test.setWidget(self.p4)
                print("Admin_page")

                
            elif(global_var.state_machine==5):
                self.test.setWidget(self.p5)
                print("test info")

            elif(global_var.state_machine==6):
                self.test.setWidget(self.p6)
                print("help_tab")

            elif(global_var.state_machine==8):
                self.test.setWidget(self.p8)
                print("license_page ")
                
            elif(global_var.state_machine==10):
##                self.p10.read_frm_db() #manage group
                self.test.setWidget(self.p10)
                print("wirecolor")

            elif(global_var.state_machine==11):            
                if (GV.GroupEditFlag==1):
                    self.p11.edit()
                else:
                    self.p11.add()
                self.test.setWidget(self.p11)
                print("Groupcreation")

            elif(global_var.state_machine==12):
                self.test.setWidget(self.p12)
                print("Fixture_library")

            elif(global_var.state_machine==13):           
                self.test.setWidget(self.p13)
                print("Splice_visualization")

            elif(global_var.state_machine==14):

                self.test.setWidget(self.p14)
                print("tepaching_page1")

            elif(global_var.state_machine==15):
                
                if(str(GV.AssetCodeScan)=='0'):
                    self.p15.facilities_2.hide()
                self.p15.acuation_db_read()
                self.p15.facilities_db_read()
                self.p15.display_data()
                self.test.setWidget(self.p15)
                print("teaching_page2")

            elif(global_var.state_machine==16):
                self.test.setWidget(self.p16)
                print("Testing_Flow")

            elif(global_var.state_machine==17):
                self.test.setWidget(self.p17)
                print("teaching_page3")

            elif(global_var.state_machine==18):
                self.test.setWidget(self.p18)
                print("Component_Testing")
                
            elif(global_var.state_machine==19):
                self.test.setWidget(self.p19)
                print("teaching_page4")
                
            elif(global_var.state_machine==20):
                self.test.setWidget(self.p20)
                print("teaching_page5")
                
            elif(global_var.state_machine==21):
                self.test.setWidget(self.p21)
                print("dignostics_window")

            elif(global_var.state_machine==22):
                self.p22.lineEdit_9.setText(str(GV.Location_No))
                self.p22.lineEdit_10.setText(str(GV.Part_Name))
                self.test.setWidget(self.p22)
                print("cutting_main")
            
          
            elif(global_var.state_machine==23):
                
                self.p23.read_frm_db()
                self.test.setWidget(self.p23)
                
                print("Group Creation Library")
        if(global_var.state_machine==11):
            if (self.p11.comboBox_9.currentText() == 'No'):
                self.p11.spinBox.setEnabled(False)
            else:
                self.p11.spinBox.setEnabled(True)                  
            if (self.p11.comboBox_7.currentText() == 'No'):
                self.p11.spinBox_2.setEnabled(False)
            else:
                self.p11.spinBox_2.setEnabled(True)
                
            if (self.p11.comboBox_2.currentText() == 'No'):
                self.p11.spinBox_3.setEnabled(False)
            else:
                self.p11.spinBox_3.setEnabled(True)
                
            if (self.p11.comboBox_4.currentText() == 'No'):
                self.p11.spinBox_4.setEnabled(False)
            else:
                self.p11.spinBox_4.setEnabled(True)
                
            if (self.p11.comboBox_5.currentText() == 'No'):
                self.p11.spinBox_5.setEnabled(False)
            else:
                self.p11.spinBox_5.setEnabled(True)
                
            if (self.p11.comboBox.currentText() == 'No'):
                self.p11.spinBox_6.setEnabled(False)
            else:
                self.p11.spinBox_6.setEnabled(True)
                
            if (self.p11.comboBox_6.currentText() == 'No'):
                self.p11.spinBox_7.setEnabled(False)
            else:
                self.p11.spinBox_7.setEnabled(True)    

        
    @pyqtSlot()
    def msg_structure(self):
##        print("GV.data_Available..........",GV.data_Available)
        if(GV.data_Available!=0):
            GUI_Display(GV.data_Available,self)
            GV.data_Available=0
        
    @pyqtSlot()
    def random_data(self):

        if(GV.Visual_Engine_Start==1):
            rand_data(self.p4)
            GV.Visual_Engine_Start=0
        elif(GV.Visual_Engine_Start==2):
            GV.Visual_Engine_Start=0
            clear_image(self.p4)
        elif(GV.Visual_Engine_Start==3):
            GV.Visual_Engine_Start=0
            put_image(self.p4)
        elif(GV.Visual_Engine_Start==4):
            GV.Visual_Engine_Start=0
            pass_image(self.p4)
        




def main():
    global width 
    global height
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create("WindowsXP")) 
    screen_resolution = app.desktop().screenGeometry()  
    width  = screen_resolution.width() 
    height = screen_resolution.height()
    print("width,height",width,height)
    p0 = Front_win()
    p1 = login_page()
    p2 = RsesetPw_page()
    p3 = admin_config_page()
    p4 = Admin_page()
    p5 = abt_tester_page()
##    p6 = help_tab()
    p7 = contactUs_page()
    p8 = license_page()
    p9 = Connlibrary()    
    p10= wirecolor()
    p11= Groupcreation()
    p12 = Fixture_library()
    p13 = Splice_visual()
    p14 = teaching_page1() #cable selection
    p15 = teaching_page2()  #hs file
    p16 = Testing_Flow()     #user testing Flow
    p17 = teaching_page3()  #hrn file
    p18 = Component_Testing()
    p19 = teaching_page4()  #local grp file
    p20 = teaching_page5()  #lbl file n bar file
    p21 = dignostics_window()
    p22 = cutting_main()
    p23 = manage_group()
    p24 = log_display()
    p25 = Test_Report()
    p26 = message_library_page()
    p27 = cable_selction()
    p29 = splice_library()
    
   
    GUI = Ui_MainWindow(p0,p1,p2,p3,p4,p5,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p29)

    GUI.show()
    timer = QTimer()
    GUI.connect(timer,SIGNAL("timeout()"),GUI,SLOT("date_time_update()"))
    timer.start(100)

    timer1 = QTimer()
    GUI.connect(timer1,SIGNAL("timeout()"),GUI,SLOT("msg_structure()"))
    timer1.start(100)

    timer2 = QTimer()
    GUI.connect(timer2,SIGNAL("timeout()"),GUI,SLOT("random_data()"))
    # GUI.showMaximized()
    #GUI.showFullScreen()
    timer2.start(100)

    app.exec_()

if __name__ == '__main__':
    main()















        
