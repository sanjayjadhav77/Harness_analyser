import global_var
from global_files import*
import global_test_var as GV 
import abt_tester
import serial
from  Sql_db import *
from HDM import *
from CAN_Bus import *
class abt_tester_page(QtGui.QMainWindow,abt_tester.Ui_MainWindow):      # class of abt_tester page

    def __init__(self):
        super(abt_tester_page,self).__init__()
        self.setupUi(self)

        total_pt=str(GV.total_point) 
        tatal_cds=str(GV.Card_counter)
        self.label_10.setText(tatal_cds)
        self.label_9.setText(total_pt)
        self.pushButton.clicked.connect(self.check_card_status)
##        self.pushButton_2.clicked.connect(self.close_window)
    def popupmeassage(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(self.quit_msg )
        msgBox.setWindowTitle("Message")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            global_var.state_machine_flag=1
            global_var.state_machine=111
            msgBox.close() 
        if returnValue == QMessageBox.Cancel:
            msgBox.close() 
    def close_window(self):
        if(global_var.admin_loginflag==1):
            global_var.state_machine = 1
            global_var.state_machine_flag = 1
            print('log', global_var.state_machine_flag, global_var.state_machine)
        else:
            global_var.state_machine = 111
            global_var.state_machine_flag = 1
            print('ooooo', global_var.state_machine_flag, global_var.state_machine)
            

    def check_card_status(self):
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Card Status','Check Card Status')
        CAN_configuration()
        GV.Card_counter=card_status()
        print("total_card", GV.Card_counter)
        GV.total_point=GV.Card_counter*64
        card_init()
        GV.is_card_sequential=Card_sequential()
        if(GV.is_card_sequential==1):
            print("Card not sequential")
        else:
            self.quit_msg = "Your Card Is sequential. "
            self.popupmeassage()    
        total_pt=str(GV.total_point)
        tatal_cds=str(GV.Card_counter)
        self.label_10.setText(tatal_cds)
        self.label_9.setText(total_pt)
        
        
        
    
    
        
        

##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = abt_tester_page()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
