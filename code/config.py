import global_var 
from global_files import*
import configuration
import global_test_var as GV
from  Sql_db import *
from shutil import copyfile
import os
class admin_config_page(QtGui.QMainWindow,configuration.Ui_MainWindow):      # class of admin_config page

    def __init__(self):
        
        super(admin_config_page,self).__init__()
        self.setupUi(self)      
        self.sys_label.hide()
        self.lineEdit_6.setText(str(GV.Pass_Count))
        self.lineEdit_7.setText(str(GV.Fail_Count))

              
        self.gen_label.mousePressEvent=self.genral_set
        self.sys_label.mousePressEvent=self.system_set
        self.user_label.mousePressEvent=self.user_set
        
##        self.pushButton.clicked.connect(self.clr_bar)
        self.pushButton_3.clicked.connect(self.sys_config_save)
        self.pushButton_2.clicked.connect(self.export_db)
        self.pushButton_4.clicked.connect(self.genral_config_save)
        self.pushButton_5.clicked.connect(self.user_config_save)
        self.pushButton_6.clicked.connect(self.partno)
        self.pushButton_7.clicked.connect(self.uservar1)
        self.pushButton_9.clicked.connect(self.uservar2)
        self.pushButton_8.clicked.connect(self.uservar3)
        self.pushButton_10.clicked.connect(self.uservar4)
        self.pushButton_11.clicked.connect(self.Set_PassFailcnt)
        self.checkBox_46.stateChanged.connect(self.clickBox)
        self.checkBox_47.stateChanged.connect(self.clickBox1)
        self.checkBox_45.stateChanged.connect(self.userpageshow)
        self.pushButton.clicked.connect(self.factory_popup)
      
        self.lineEdit_62.setValidator(QIntValidator(1, 10)) 
        self.lineEdit_64.setValidator(QIntValidator(1, 128))
        self.lineEdit_69.setValidator(QIntValidator(1, 5))
    #-------------------------------------------Factory Reset --------------------------#
    def Factory_reset(self):
        os.rename('/home/pi/Desktop/.HA_Editor/code/tester_files/HA_Gen_2.0.db', '/home/pi/Desktop/.HA_Editor/code/tester_files/HA_Gen_2.0.db1')
        src = '/home/pi/Desktop/.HA_Editor/code/tester_files/HA_Gen_2.0.db1'
        dst = '/home/pi/Desktop/.HA_Editor/Backup/HA_Gen_2.0.db1'
        copyfile(src, dst)
        src = '/home/pi/Desktop/.HA_Editor/Restore/HA_Gen_2.0.db'
        dst = '/home/pi/Desktop/.HA_Editor/code/tester_files/HA_Gen_2.0.db'
        copyfile(src, dst)
        os.remove('/home/pi/Desktop/.HA_Editor/code/tester_files/HA_Gen_2.0.db1')
        
        # data=[]
        # fact_data=[]
        # for i in range (1,129):
        #     data=[1,i,i,i,'CT']
        #     fact_data.append(data)
        # UploadGlobal_Grp2(fact_data)
        GV.special_pins=[]
        os.system("sudo reboot")
#---------------------------------------------------------------------------------------#
    def Set_PassFailcnt(self):
        print("reset pass count")
        GV.Pass_Count=self.lineEdit_6.text()
        GV.Fail_Count=self.lineEdit_7.text()
        x=[(GV.Pass_Count,GV.Fail_Count,GV.Stage1_status,GV.Stage1_Points_No,GV.Stage2_status,GV.Stage2_Points_No)]
        UploadCable_Info(GV.Location_No,x)

    def userpageshow(self):
        if (self.checkBox_45.isChecked()):
            self.user_label.show()
        else:
            self.user_label.hide()
    def clickBox(self):
        if (self.checkBox_46.isChecked()):
            self.checkBox_47.setChecked(False)

    def clickBox1(self):
        if self.checkBox_47.isChecked():
            self.checkBox_46.setChecked(False)
        
    def factory_popup(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Do you want Factory Reset ?")
        msgBox.setWindowTitle("Message")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.Factory_reset()
        if returnValue == QMessageBox.Cancel:
            msgBox.close()           
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
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
    
            
    def clr_DB(self):
        Delete_Database_Table()
        self.mess="Database Has been Clear"
        self.clickMethod()
    def clickMethod(self):
        QtGui.QMessageBox.about(self, "Clear", self.mess)
       
    def genral_set (self,event):
        self.stackedWidget.setCurrentIndex(0)
        self.gen_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_select.png);color: rgb(255, 255, 255);font: 14pt "Roboto [GOOG]";""")
        self.sys_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);font: 14pt "Roboto [GOOG]";""")
        self.user_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);font: 14pt "Roboto [GOOG]";""")

    def system_set (self,event):
        self.stackedWidget.setCurrentIndex(1)
        self.sys_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_select.png);color: rgb(255, 255, 255);font: 14pt "Roboto [GOOG]";""")
        self.gen_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);font: 14pt "Roboto [GOOG]";""")
        self.user_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);font: 14pt "Roboto [GOOG]";""")

    def user_set(self,event):
        self.textEdit.setFocus()
        self.stackedWidget.setCurrentIndex(2)
        self.user_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_select.png);color: rgb(255, 255, 255);font: 14pt "Roboto [GOOG]";""")
        self.gen_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);font: 14pt "Roboto [GOOG]";""")
        self.sys_label.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);font: 14pt "Roboto [GOOG]";""")

        
#----------------------------------------------system config----------------------------------------------------------------#
        


    def Reboot(self):
        self.pushButton_12.setStyleSheet("background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Sys_btn/P.png);color: rgb(255, 255, 255);")        
        os.system("sudo pkill python")
        
    def clr_bar(self):
##        self.pushButton.setStyleSheet("""background-image:url(/home/pi/Desktop/AWHT/UI_files/final_assets/Secondary_btn/big_press.png);color: rgb(38, 177, 255);font: 12pt "Roboto [GOOG]";""")        
        GV.msg=3
        GV.Barcode_Clear_Flag=1
        UploadSystemInfo(GV.Barcode_Clear_Flag,5)
    def reset_database(self):
        rst_no=self.lineEdit.text()



    def setsys_config(self):
        #===========================================user page==================
        self.lineEdit_70.setText(GV.Weekday_STD)
        self.lineEdit_61.setText(GV.A_timing)
        self.lineEdit_72.setText(GV.B_timing)
        self.lineEdit_63.setText(GV.C_timing)
        if (GV.AutoPartLoad=='1'):
            self.checkBox_45.setChecked(True)
        else:
            self.checkBox_45.setChecked(False)
        
        
        #============================================sys page=================
        self.lineEdit_64.setText(GV.CableNos)
        self.lineEdit_62.setText(GV.LeakageTestTime)
        self.lineEdit_69.setText(GV.LeakIterations)
        if(GV.LeakageChannel == '1'):
            self.checkBox_46.setChecked(True)
            self.checkBox_47.setChecked(False)
        elif(GV.LeakageChannel == '2'):
            self.checkBox_47.setChecked(True)
            self.checkBox_46.setChecked(False)
        else:
            self.checkBox_47.setChecked(False)
            self.checkBox_46.setChecked(False)
        if (GV.Report=='1'):
            self.checkBox_49.setChecked(True)
        else:
            self.checkBox_49.setChecked(False)

        if (GV.AssetCodeScan=='1'):
            self.checkBox_48.setChecked(True)
        else:
            self.checkBox_48.setChecked(False)

        if (GV.ConectorVisual=='1'):
            self.checkBox_34.setChecked(True)
        else:
            self.checkBox_34.setChecked(False)

        if (GV.TesterNetwork=='1'):
            self.checkBox_30.setChecked(True)
        else:
            self.checkBox_30.setChecked(False)

        if (GV.ProductionMonitoring=='1'):
            self.checkBox_35.setChecked(True)
        else:
            self.checkBox_35.setChecked(False)

        if (GV.DeviceInterface=='1'):
            self.checkBox_44.setChecked(True)
        else:
            self.checkBox_44.setChecked(False)

        if (GV.Tracebility=='1'):
            self.checkBox_36.setChecked(True)
        else:
            self.checkBox_36.setChecked(False) 

        
    def sys_config_save(self):

        
        if((len(self.lineEdit_61.text()))>0):
            GV.A_timing=self.lineEdit_61.text()
            
        else:
            GV.A_timing='0'
        if((len(self.lineEdit_72.text()))>0):
            GV.B_timing=self.lineEdit_72.text()
            
        else:
            GV.B_timing='0'
        if((len(self.lineEdit_63.text()))>0):
            GV.C_timing=self.lineEdit_63.text()
            
        else:
            GV.C_timing='0'
        
        if((len(self.lineEdit_64.text()))>0):
            GV.CableNos=self.lineEdit_64.text()
            
        else:   
            GV.CableNos='0'
        
        if((len(self.lineEdit_62.text()))>0):
            GV.LeakageTestTime=self.lineEdit_62.text()
            
        else:
            GV.LeakageTestTime='0'
        if((len(self.lineEdit_69.text()))>0):
            GV.LeakIterations=self.lineEdit_69.text()
            
        else:
            GV.LeakIterations='0'


        if (self.checkBox_48.isChecked()):
            GV.AssetCodeScan = '1'
        else:
            GV.AssetCodeScan = '0'

        if (self.checkBox_46.isChecked()):
##            self.checkBox_47.setChecked(False)
            GV.LeakageChannel = '1'
        elif (self.checkBox_47.isChecked()):
##            self.checkBox_46.setChecked(False)
            GV.LeakageChannel = '2'
        else:
            GV.LeakageChannel = '0'

        if (self.checkBox_34.isChecked()):
            GV.ConectorVisual = '1'
        else:
            GV.ConectorVisual = '0'

        if (self.checkBox_30.isChecked()):
            GV.TesterNetwork = '1'
        else:
            GV.TesterNetwork = '0'

        if (self.checkBox_36.isChecked()):
            GV.Tracebility = '1'
        else:
            GV.Tracebility = '0'

        if (self.checkBox_35.isChecked()):
            GV.ProductionMonitoring = '1'
        else:
            GV.ProductionMonitoring = '0'

        if (self.checkBox_44.isChecked()):
            GV.DeviceInterface = '1'
        else:
            GV.DeviceInterface = '0'
        
            
        if (self.checkBox_49.isChecked()):
            GV.Report = '1'
        else:
            GV.Report = '0'
        
        
        
        
        
        
        uploadConfiguration(1)
        self.quit_msg="Records Saved Successfully"
        self.popupmeassage()
    def read_config_file_db(self):

        if(GV.Leakage_Testing==0):
            global_var.lk_y_n=0
            self.leakage_tst(1)
        else:
            global_var.lk_y_n=1
            self.leakage_tst(1)           
 
#----------------------------------------------Genral config----------------------------------------------------------------#           
    def partno(self):
        cursor = self.textEdit.textCursor()
        PartNoLoc = cursor.selectedText()
        self.lineEdit.setText(str(PartNoLoc))     
##        print(PartNoLoc)
    def uservar1(self):
        cursor = self.textEdit.textCursor()
        var1 = cursor.selectedText()
        self.lineEdit_2.setText(str(var1))     
##        print(var1)
    def uservar2(self):
        cursor = self.textEdit.textCursor()
        var2 = cursor.selectedText()
        self.lineEdit_3.setText(str(var2))     
##        print(var2)
    def uservar3(self):
        cursor = self.textEdit.textCursor()
        var3 = cursor.selectedText()
        self.lineEdit_4.setText(str(var3))     
##        print(var3)
    def uservar4(self):
        cursor = self.textEdit.textCursor()
        var4 = cursor.selectedText()
        self.lineEdit_5.setText(str(var4))     
##        print(var4)
    def user_config_save(self):
        
        GV.user_config_flag=0
        
        GV.barcode_master_data=self.textEdit.toPlainText()
        try:
            
            GV.PartNoLoc=self.lineEdit.text()
            print("GV.PartNoLoc",GV.PartNoLoc)
            GV.PartNO_Length=GV.barcode_master_data.index(GV.PartNoLoc)
            
            GV.UserVar1_Loc=self.lineEdit_2.text()
            print("GV.UserVar1_Loc",GV.UserVar1_Loc)
            GV.Var1_Length=GV.barcode_master_data.index(GV.UserVar1_Loc)
            
            GV.UserVar2_Loc=self.lineEdit_3.text()
            GV.Var2_Length=GV.barcode_master_data.index(GV.UserVar2_Loc)
            
            GV.UserVar3_Loc=self.lineEdit_4.text()
            GV.Var3_Length=GV.barcode_master_data.index(GV.UserVar3_Loc)
            
            GV.UserVar4_Loc=self.lineEdit_5.text()
            GV.Var4_Length=GV.barcode_master_data.index(GV.UserVar4_Loc)
        
            if(len(GV.PartNoLoc)>0 or len(GV.UserVar1_Loc)>0 or len(GV.UserVar2_Loc)>0 or len(GV.UserVar3_Loc)>0 or len(GV.UserVar4_Loc)>0):
                uploadUserConfiguration(1)
                self.textEdit.clear()
                self.quit_msg="Records Saved Successfully"
                self.popupmeassage()
            else:
                self.quit_msg="Fill Atleast One Field"
                self.popupmeassage()
        except(ValueError):
            self.quit_msg="No data in master barcode"
            self.popupmeassage()
    def genral_config_save(self):
        GV.user_config_flag=1
        GV.Shift_A='A'
        GV.Shift_B='B'
        GV.Shift_C='C'
        
        if((len(self.lineEdit_61.text()))>0):
            GV.A_timing=self.lineEdit_61.text()
            
        else:
            GV.A_timing='00:00:00'

        if((len(self.lineEdit_72.text()))>0):
            GV.B_timing=self.lineEdit_72.text()
            
        else:
            GV.B_timing='00:00:00'

        if((len(self.lineEdit_63.text()))>0):
            GV.C_timing=self.lineEdit_63.text()
            
        else:
            GV.C_timing='00:00:00'
            
        if((len(self.lineEdit_70.text()))>0):
            GV.Weekday_STD=self.lineEdit_70.text()
            
        else:
            GV.Weekday_STD='0'
            
        if (self.checkBox_45.isChecked()):
            GV.AutoPartLoad = '1'
        else:
            GV.AutoPartLoad = '0'
        
        

        
        if(GV.A_timing==GV.B_timing or GV.B_timing==GV.C_timing or GV.C_timing==GV.A_timing):
            self.quit_msg="Check The Shift Timings"
            self.popupmeassage()
        else:
            uploadUserConfiguration(1)
            self.quit_msg="Records Saved Successfully"
            self.popupmeassage()


    def export_log_file(self):   
        frm_dd= self.lineEdit_10.text()
        frm_mm= self.lineEdit_11.text()
        frm_yy= self.lineEdit_19.text()
        to_dd= self.lineEdit_22.text()
        to_mm= self.lineEdit_20.text()
        to_yy= self.lineEdit_21.text()

        FromDate= frm_yy + '-' + frm_mm + '-' + frm_dd
        ToDate = to_yy + '-' + to_mm + '-' + to_dd
        Final_date= FromDate +' '+ToDate
        print('FromDate',FromDate)
        print('ToDate',ToDate)
        print('Final_date',Final_date)
        
        

        DownloadLog(FromDate,ToDate)
        usb_detect = len(next(os.walk('/media/usb0'))[1])
        if(len(frm_dd)>1):
            if(usb_detect>0):
                src_loc= '/home/pi/Desktop/ExportData.xls'
                des_loc= ' /media/usb0'
                os.system("sudo cp -R "+src_loc + des_loc)
                UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Export Log File',Final_date)
                print('log_file saved')
                self.quit_msg="logs Saved Successfully"
                self.popupmeassage()
        else:
            print('log_file not saved')
            self.quit_msg="log_file not saved"
            self.popupmeassage()


        if(frm_dd > '31'):
            self.lineEdit_10.clear()         
        if(frm_mm > '12'):  
            self.lineEdit_11.clear()          
        if(len(frm_yy) > 4):  
            self.lineEdit_19.clear()      
        print(frm_dd,frm_mm,frm_yy)
        
        if(to_dd > '31'):
            self.lineEdit_22.clear()         
        if(to_mm > '12'):  
            self.lineEdit_20.clear()          
        if(len(to_yy) > 4):  
            self.lineEdit_21.clear()      
        print(to_dd,to_mm,to_yy)

    def export_db(self):
        print(GV.Local_Group_data)
        Export_HarnessData(GV.Location_No)
        Export_Group_data(GV.Location_No)
        usb_detect = len(next(os.walk('/media/usb0'))[1])
        print('usb_detect',usb_detect)

        if(usb_detect>0):
            self.copy_data_to_USB(GV.source)
            self.copy_data_to_USB(GV.GRP_source)
            UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Export Data',"database Exported")
            print('export_db saved')
            self.quit_msg="Database Exported"
            self.popupmeassage()
        else:
            self.quit_msg="USB Not Detected"
            self.popupmeassage()
        
    def reset_DB(self):
        rst=self.lineEdit.text()
        if(rst > '100'):
            self.lineEdit.clear()
    def copy_data_to_USB(self,source):
        print(source)
        dest="/media/usb0/HA_GEN2.0"
        d = 'sudo cp -R '+source+' '+ dest
        os.system(str(d))
        os.remove(source)
       

                     
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = admin_config_page()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
        
