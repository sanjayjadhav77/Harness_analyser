import global_var
from global_files import*
import teaching_5
import global_test_var as GV
from  Sql_db import *
import popup_window
from printer import *

class teaching_page5(QtGui.QMainWindow,teaching_5.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(teaching_page5,self).__init__()
        self.setupUi(self)
        self.read_lbl_data_frm_db()
        self.usb_btn.clicked.connect(self.usb_transfer)
        self.Edit_btn.clicked.connect(self.edit_txt_data)
        self.save_btn.clicked.connect(self.save_lbl_to_db)
        self.bar1_add.clicked.connect(self.add_bar1)
        self.bar2_add.clicked.connect(self.add_bar2)


##        self.pushButton_3.clicked.connect(self.close_window)
        self.checkBox_34.stateChanged.connect(self.clickBox)
        self.checkBox_35.stateChanged.connect(self.clickBox1)
        self.checkBox.stateChanged.connect(self.use_gbl_settings)
        self.pushButton.clicked.connect(self.printer)
    def printer(self):
        print("printer test")
        GV.Local_Label_Data=self.textEdit.toPlainText()
        Serial_Init()
        Serial_Printing()



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
    def clickBox(self):
        if (self.checkBox_34.isChecked()):
            self.checkBox_35.setChecked(False)
    def clickBox1(self):
        if (self.checkBox_35.isChecked()):
            self.checkBox_34.setChecked(False)
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
        
  
    def use_gbl_settings(self):
        if (self.checkBox.isChecked() == True):
            print("upload sample label data")
        else:
            print("Clear data")
            
            
    def read_lbl_data_frm_db(self):
        self.textEdit.setText(str(GV.Local_Label_Data))
        self.lineEdit.setText(str(GV.Local_Barcode1_Data))
        self.lineEdit_2.setText(str(GV.Local_Barcode2_Data))
 
    def add_bar1(self):
        cursor = self.textEdit.textCursor()
        bar1_data = cursor.selectedText()
        self.lineEdit.setText(str(bar1_data))     
        print(bar1_data)        
        self.bar1_add.setStyleSheet("border-image: url(:/images/final_assets/Secondary_btn/pressed.png);color: rgb(38, 177, 255);")
        
    def add_bar2(self):
        cursor1 = self.textEdit.textCursor()
        bar2_data = cursor1.selectedText()
        self.lineEdit_2.setText(str(bar2_data))     
        print(bar2_data)        
        self.bar2_add.setStyleSheet("border-image: url(:/images/final_assets/Secondary_btn/pressed.png);color: rgb(38, 177, 255);")
        
    def edit_txt_data(self):
        self.textEdit.setEnabled(True) 
        self.Edit_btn.setStyleSheet("border-image: url(:/images/final_assets/Secondary_btn/pressed.png);color: rgb(38, 177, 255);")
        
    def usb_transfer(self):
        usb_detect = len(next(os.walk('/media/usb0'))[1])
        if(usb_detect>0):
            try:
                self.usb_btn.setStyleSheet("border-image: url(:/images/final_assets/Secondary_btn/pressed.png);color: rgb(38, 177, 255);")
                file_name=QFileDialog.getOpenFileName(self, 'Open file', '/media/usb0','*.lbl')
                read_file=open(file_name,'r')
                pd_data=read_file.read()
                self.textEdit.setText(pd_data)
                print('file done')
            except Exception as e:
                print(e)
        else:
            self.quit_msg="Usb Drive Not Detected"
            self.popupmeassage()
        
    def save_lbl_to_db(self):
        self.textEdit.setEnabled(False) 
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,' Save','Saved Successfully')
        self.save_btn.setStyleSheet("border-image: url(:/images/final_assets/Main_Btn/btn_press.png);color: rgb(255, 255, 255);")
        
        if (self.checkBox_34.isChecked()):
##            self.checkBox_35.setEnabled(False)
            GV.Local_Label_Data=self.textEdit.toPlainText()
        
            GV.Local_Barcode1_Data=self.lineEdit.text()
            
            GV.Local_Barcode2_Data=self.lineEdit_2.text()
            
            UploadQC1_Data(GV.Location_No,GV.Local_Label_Data,GV.Local_Barcode1_Data,GV.Local_Barcode2_Data)
            UploadSystemInfo(GV.Local_Barcode1_Data,3)
            self.ok_button()
        elif(self.checkBox_35.isChecked()):
##            self.checkBox_34.setEnabled(False)
            GV.Local_Label_Data=self.textEdit.toPlainText()
        
            GV.Local_Barcode1_Data=self.lineEdit.text()
            
            GV.Local_Barcode2_Data=self.lineEdit_2.text()
            
            UploadQC2_Data(GV.Location_No,GV.Local_Label_Data,GV.Local_Barcode1_Data,GV.Local_Barcode2_Data)
            UploadSystemInfo(GV.Local_Barcode2_Data,4)
            self.ok_button()
        else:
            print("select Label")
            quit_msg = "Select Label"

            reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Ok,)
     
    def read_lbl_data_frm_db(self):
        self.textEdit.setText(str(GV.Local_Label_Data))
        self.lineEdit.setText(str(GV.Local_Barcode1_Data))
        self.lineEdit_2.setText(str(GV.Local_Barcode2_Data))

    def ok_button(self):
        self.new_window =popup_window.Ui_Dialog()
        self.new_window.show()





        
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = teaching_page5()
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
