import global_var 
from global_files import*
import admin_page

class Admin_page(QtGui.QMainWindow,admin_page.Ui_MainWindow):               # class of admin page

    def __init__(self):
        super(Admin_page,self).__init__()
        self.setupUi(self)
       
        self.pushButton.clicked.connect(self.open_admin_config_page)
##        self.pushButton_2.clicked.connect(self.)
        self.pushButton_3.clicked.connect(self.open_test_page)
        self.pushButton_4.clicked.connect(self.open_diagnostic_page)
        self.pushButton_5.clicked.connect(self.open_manage_grp_page)
        self.pushButton_6.clicked.connect(self.open_teaching1_page)

    def open_test_page(self,event):  
        global_var.state_machine=4
        global_var.state_machine_flag=1
        self.pushButton_3.setStyleSheet("""background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Dashboard_btn/btn_press.png);font: 25 24pt "Roboto [GOOG]";""")
                                      
    def open_admin_config_page(self,event):
        global_var.state_machine=11
        global_var.state_machine_flag=1
    
        self.pushButton.setStyleSheet("""background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Dashboard_btn/btn_press.png);font: 25 24pt "Roboto [GOOG]";""")

    def open_manage_grp_page(self,event):
        global_var.state_machine=10
        global_var.state_machine_flag=1
        self.pushButton_5.setStyleSheet("""background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Dashboard_btn/btn_press.png);font: 25 24pt "Roboto [GOOG]";""")

    def open_teaching1_page(self,event):
        UploadLog_Data(GV.Location_No,GV.Part_Name,'Teaching','Teaching_Page1')
        GV.msg=0         #1 march
        GV.checkboard_flag=0      #1 march
        global_var.state_machine=12
        global_var.state_machine_flag=1
        self.pushButton_6.setStyleSheet("""background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Dashboard_btn/btn_press.png);font: 25 24pt "Roboto [GOOG]";""")

    def open_diagnostic_page(self,event):
        global_var.state_machine=9
        global_var.state_machine_flag=1
        self.pushButton_4.setStyleSheet("""background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Dashboard_btn/btn_press.png);font: 25 24pt "Roboto [GOOG]";""")
        
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = Admin_page()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
