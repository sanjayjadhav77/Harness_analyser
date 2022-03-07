import login
from global_files import *
import global_var
import global_test_var as GV
from Sql_db import *
from main import*

class login_page(QtGui.QMainWindow, login.Ui_MainWindow):  # class of login page

    def __init__(self):
        super(login_page, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Login_btn)
        self.reset_pw.mousePressEvent = self.open_reset_pw_window


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Tab:
            self.test_method()
            print("Tab key pressed")
        elif event.key() == Qt.Key_Return:
            print("Enter Key Pressed")
            self.Login_btn(event)

    def test_method(self):
        self.pw_lineEdit.setFocus()

    def Login_btn(self, event):
        
        print(global_var.user_1, global_var.user_1_pw)

        
        print(global_var.user_2, global_var.user_2_pw)

        username = str(self.uid_lineEdit.text())
        password = self.pw_lineEdit.text()

        if (username == global_var.user_1) and (password == global_var.user_1_pw):
            UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Admin','Admin Login')
            self.uid_lineEdit.clear()
            self.pw_lineEdit.clear()
            ##            print('valid')
            global_var.bck_to_login = 1
            global_var.KT_login = 0
            global_var.admin_loginflag=1
            ##            print('bck_to_login',global_var.bck_to_login)
            global_var.state_machine = 1
            global_var.state_machine_flag = 1
        elif ((username == global_var.user_2) and (password == global_var.user_2_pw)):
            UploadSysLog_Data(GV.Location_No,GV.Part_Name,'KalpTech Login','Super Login')
            self.uid_lineEdit.clear()
            self.pw_lineEdit.clear()
            global_var.KT_login = 1
            global_var.login_flag=1
            global_var.state_machine = 1
            global_var.state_machine_flag = 1
        else:
            print('invalid')
            choice = QtGui.QMessageBox.question(self, 'Error!', "Invalid ID or Password ?")

            self.pw_lineEdit.clear()

    def open_reset_pw_window(self, event):
        username = str(self.uid_lineEdit.text())
        global_var.state_machine = 2
        global_var.state_machine_flag = 1
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Reset Password','PasSword Change')
        print('logggg', global_var.state_machine_flag, global_var.state_machine)

##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = login_page()
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
