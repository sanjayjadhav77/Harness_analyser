from global_files import*
import superlogin
import global_test_var as GV
import global_var

class Supervisory_login(QtGui.QMainWindow,superlogin.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(Supervisory_login,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_options)
        self.pushButton_2.clicked.connect(self.wrong_sample)
        self.pushButton_4.clicked.connect(self.clear_scan)
        self.pushButton_6.clicked.connect(self.superAccess1)
        self.pushButton_5.clicked.connect(self.superAccess2)
       

    def superAccess1(self):
        self.pushButton_2.setStyleSheet("border-image: url(:/images/final_assets/Secondary_btn/big_press.png);")

        print("Super Access 1")

    def superAccess2(self):
        self.pushButton_2.setStyleSheet("border-image: url(:/images/final_assets/Secondary_btn/big_press.png);")
        print("Super Access 2")

    def clear_scan(self):
        print("Clear Scan")
        GV.Abort_Event_flag=1
        self.pushButton_2.setStyleSheet("border-image: url(:/images/final_assets/Secondary_btn/big_press.png);")
       

    def wrong_sample(self):
        self.pushButton_2.setStyleSheet("border-image: url(:/images/final_assets/Secondary_btn/big_press.png);")
        print("wrong Sample provide")

    def show_options(self):
        auth_key = self.key.text()
        print("GV.super_user[0][1]",GV.super_user[0][1])
        # auth_key="12"
        if(GV.super_user[0][1]==auth_key):
            print("Match------------")
            
            self.pushButton_2.show()
            self.pushButton_4.show()
            self.pushButton_5.show()
            self.pushButton_6.show()
            self.key.clear()
            self.label.hide()
            self.pushButton.hide()
            self.key.hide()
            self.pushButton.setEnabled(False)
            self.key.setEnabled(False)
        else:
            self.quit_msg = "Invalid Key "
            self.popupmeassage()
    def popupmeassage(self):
        self.key.clear()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(self.quit_msg )
        msgBox.setWindowTitle("Warning")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            msgBox.close() 
            self.key.setFocus()
        if returnValue == QMessageBox.Cancel:
            msgBox.close()           
            self.key.setFocus()
    

                
# def main():
#    app = QtGui.QApplication(sys.argv)
#    GUI = Supervisory_login()  
#    GUI.show()
#    app.exec_()

# if __name__ == '__main__':
#    main()
