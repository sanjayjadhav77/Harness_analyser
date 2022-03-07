
import global_var
from global_files import*
import Prod_Logs
import datetime
class log_display(QtGui.QMainWindow,Prod_Logs.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(log_display,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Display_log)
##        self.pushButton_3.clicked.connect(self.close_window)
        self.pushButton_2.clicked.connect(self.export_logfile)
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
    def keyPressEvent(self, event):
        print("ebent Occeured")
        val1 = self.lineEdit_10.hasFocus()
        val2 = self.lineEdit_11.hasFocus()
        val3 = self.lineEdit_19.hasFocus()
        val4 = self.lineEdit_24.hasFocus()
        val5 = self.lineEdit_26.hasFocus()
        val6 = self.lineEdit_25.hasFocus()
        
        
        if event.key() == Qt.Key_Tab:
            self.test_method(val1,val2,val3,val4,val5,val6)
            print("Tab key pressed")
        elif event.key() == Qt.Key_Return:
            print("Enter Key Pressed")
            self.Display_log()

    def test_method(self,val1,val2,val3,val4,val5,val6):
        print("event",val1,val2)
        if(val1==True):
            self.lineEdit_11.setFocus()
        elif(val2==True):
            self.lineEdit_19.setFocus()
        elif(val3==True):
            self.lineEdit_24.setFocus()
        elif(val4==True):
            self.lineEdit_26.setFocus()
        elif(val6==True):
            self.lineEdit_25.setFocus()
        elif(val6==True):
            self.lineEdit_10.setFocus()
    
    def Display_log(self):   
        frm_dd= self.lineEdit_10.text()
        
        frm_mm= self.lineEdit_11.text()
        frm_yy= self.lineEdit_19.text()
        if(len(frm_dd)<=1):
            frm_dd='0' + frm_dd
        if(len(frm_mm)<=1):
            frm_mm='0' + frm_mm
        
        try:
            to_dd= int(self.lineEdit_24.text())+1
            
            to_mm= self.lineEdit_26.text()
            to_yy= self.lineEdit_25.text()
            if(len(str(frm_dd))<=1):
                to_dd='0' + str(to_dd)
            if(len(to_mm)<=1):
                to_mm='0' + to_mm
            FromDate= frm_yy + '-' + frm_mm + '-' + frm_dd
            ToDate = to_yy + '-' + to_mm + '-' + str(to_dd)
            Final_date= FromDate +' '+ToDate
            print('FromDate',FromDate)
            print('ToDate',ToDate)
            print('Final_date',Final_date)
        except(ValueError,UnboundLocalError):
            print("Date not entered")
        if(len(frm_dd)>1 and len(frm_mm)>1 and len(frm_yy)>1  and len(to_mm)>1 and len(to_yy)>1):

            x = int(self.lineEdit_24.text())
            current_time = datetime.datetime.now()
            if (x>current_time.day or int(to_mm)>current_time.month or int(to_yy)>current_time.year):
                self.quit_msg="Future Datetime Entered"
                self.popupmeassage()
            else:
                if(GV.System_Shuffle==1):
                    output = display_prodlogfile(FromDate,ToDate)
                else:
                    output = display_Syslogfile(FromDate,ToDate)
                for i in range (len(output)):
                    read = output[i]
                    for j in range (len(read)):
                        display_points=read[j]
                        self.tableWidget.setItem(i,j, QTableWidgetItem(str(display_points)))

        else:
            self.quit_msg="Fill All Fields"
            self.popupmeassage()
        
    def export_logfile(self):
        frm_dd= self.lineEdit_10.text()
        frm_mm= self.lineEdit_11.text()
        frm_yy= self.lineEdit_19.text()
        
        if(len(frm_dd)<=1):
            frm_dd='0' + frm_dd
        if(len(frm_mm)<=1):
            frm_mm='0' + frm_mm
        try:
            to_dd= int(self.lineEdit_24.text())+1
        
            to_mm= self.lineEdit_26.text()
            to_yy= self.lineEdit_25.text()
            if(len(str(to_dd))<=1):
                to_dd='0' + str(to_dd)
            if(len(to_mm)<=1):
                to_mm='0' + to_mm
            FromDate= frm_yy + '-' + frm_mm + '-' + frm_dd
            ToDate = to_yy + '-' + to_mm + '-' + str(to_dd)
            Final_date= FromDate +' '+ToDate
        except(ValueError,UnboundLocalError):
            print("Date not entered")
        if(len(frm_dd)>0 and len(frm_mm)>0 and len(frm_yy)>0  and len(to_mm)>0 and len(to_yy)>0):
            x = int(self.lineEdit_24.text())
            current_time = datetime.datetime.now()
            if (x>current_time.day or int(to_mm)>current_time.month or int(to_yy)>current_time.year):
                self.quit_msg="Future Datetime Entered"
                self.popupmeassage()
            else:
                        
                DownloadProdLog(FromDate,ToDate)
                usb_detect = len(next(os.walk('/media/usb0'))[1])
                if(len(frm_dd)>1):
                    if(usb_detect>0):
                        if(GV.System_Shuffle==0):
                            src_loc= '/home/pi/Desktop/ExportData.xls'
                            UploadSysLog_Data(GV.Location_No,GV.Part_Name,'log Export','Export Log File')
                        else:
                            src_loc= '/home/pi/Desktop/ExportData.xls'
                            UploadProdLog_Data(GV.Location_No,GV.Part_Name,'log Export','Export Log File')
                        des_loc= ' /media/usb0'
                        
                        os.system("sudo cp -R "+src_loc + des_loc)
                        print('log_file saved')
                        self.lineEdit_10.clear()
                        self.lineEdit_11.clear()
                        self.lineEdit_19.clear()
                        self.lineEdit_24.clear()
                        self.lineEdit_25.clear()
                        self.lineEdit_26.clear() 
                        self.quit_msg="Exported Successfully"
                        self.popupmeassage()
                    else:
                        self.quit_msg="USB not Detected"
                        self.popupmeassage()
                else:
                    print('log_file not saved')
                    self.lineEdit_10.clear()
                    self.lineEdit_11.clear()
                    self.lineEdit_19.clear()
                    self.lineEdit_24.clear()
                    self.lineEdit_25.clear()
                    self.lineEdit_26.clear() 
                    self.quit_msg="log_file not saved"
                    self.popupmeassage()
                if(frm_dd > '31'):
                    self.lineEdit_10.clear()         
                if(frm_mm > '12'):  
                    self.lineEdit_11.clear()          
                if(len(frm_yy) > 4):  
                    self.lineEdit_19.clear()      
                print(frm_dd,frm_mm,frm_yy)
                
                if(str(to_dd) > '31'):
                    self.lineEdit_24.clear()         
                if(to_mm > '12'):  
                    self.lineEdit_26.clear()          
                if(len(to_yy) > 4):  
                    self.lineEdit_25.clear()      
                print(to_dd,to_mm,to_yy)

        else:
            self.quit_msg="Fill All Fields"
            self.popupmeassage()
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = log_display()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
