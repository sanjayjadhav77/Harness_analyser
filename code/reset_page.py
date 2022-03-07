import global_var
from global_files import*
import reset_pw
import global_test_var as GV
from  Sql_db import *
class RsesetPw_page(QtGui.QMainWindow,reset_pw.Ui_MainWindow):      # class of reset_pw page

    def __init__(self):
        super(RsesetPw_page,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.reset)
        self.pushButton_2.clicked.connect(self.cancel_resetpw)
        self.setWindowTitle(" Reset Password ")
    
    def keyPressEvent(self, event):
        val1 = self.newpw_lineedit_2.hasFocus()
        val2 = self.newpw_lineedit.hasFocus()
        val3 = self.current_lineedit.hasFocus()
        
        if event.key() == Qt.Key_Tab:
            self.test_method(val1,val2,val3)
            print("Tab key pressed")
        elif event.key() == Qt.Key_Return:
            print("Enter Key Pressed")
            self.reset(event)
    def test_method(self,val1,val2,val3):
        print("event",val1,val2)
        if(val1==True):
            self.newpw_lineedit.setFocus()
        elif(val2==True):
            self.current_lineedit.setFocus()
        elif(val3==True):
            self.newpw_lineedit_2.setFocus()   
    def reset(self,event):
        GV.System_Info=DownloadSystemInfo(1)
        ktuser=DownloadSystemInfo(2)
        Admin_user=GV.System_Info[0][0]
        Admin_pass=GV.System_Info[0][1]
        KT_user=ktuser[0][0]
        KT_pass=ktuser[0][1]
        super_pass=GV.super_user[0][1]
        print("Admin_user",Admin_user,Admin_pass)
        len_current_pw=len(self.current_lineedit.text())
        len_new_pw=len(self.newpw_lineedit.text())
        new_pass = self.newpw_lineedit.text()
        old_pass = self.newpw_lineedit_2.text()
        confirm_pass = self.current_lineedit.text()
        print("old_pass",old_pass,confirm_pass,new_pass)
        if(len_current_pw > 0 and len_new_pw > 0):
            print("global_var.username",global_var.username,global_var.user_1)
            
            if(Admin_pass==old_pass and new_pass==confirm_pass):
                global_var.user_1_pw = new_pass
                pw=global_var.user_1_pw
                UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Reset password','Admin')
                UploadSystemInfo(pw,1)
                print('admin pw save')
                self.quit_msg = "Admin Password Changed !"
                self.popupmeassage()
            elif(KT_pass==old_pass and new_pass==confirm_pass):
                global_var.user_2_pw = new_pass
                pw=global_var.user_2_pw
                UploadSystemInfo(pw,2)
                print('kt pw save')
                self.quit_msg = "KalpTech Password Changed !"
                self.popupmeassage()
            elif(super_pass==old_pass and new_pass==confirm_pass):
                global_var.user_2_pw = new_pass
                pw=global_var.user_2_pw
                UploadSystemInfo(pw,6)
                print('Super pass')
                self.quit_msg = "Supervisor Password Changed !"
                self.popupmeassage()
            else:
                self.quit_msg = "Invalid Credentials !"
                self.popupmeassage()
        else:
            self.mess='Enter Credentials'
            QtGui.QMessageBox.about(self, "WARNING", self.mess)
        self.newpw_lineedit.clear()
        self.current_lineedit.clear()
        self.newpw_lineedit_2.clear()
    def popupmeassage(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(self.quit_msg )
        msgBox.setWindowTitle("Message")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.close()
        if returnValue == QMessageBox.Cancel:
            msgBox.close()
        
##        reply = QMessageBox.question(self, 'Message', self.quit_msg, QMessageBox.Ok)
##        
##        if reply == QMessageBox.Ok:
##            print("get out")
##            self.close     
    def cancel_resetpw(self,event):
        self.close()
        
        
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = RsesetPw_page()
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
