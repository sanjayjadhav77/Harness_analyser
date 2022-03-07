
import global_var
from global_files import*
import fixturelib

class Fixture_library(QtGui.QMainWindow,fixturelib.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(Fixture_library,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.send_data)
##        self.pushButton_3.clicked.connect(self.close_window)
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
    def ShowModuledata(self):
        

        GV.FixtureInfo=DownloadFixtureType()

##        self.tableWidget_2.clear()
##        item=QtGui.QTableWidgetItem("No")
##        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
##        font = QtGui.QFont()
##        font.setPointSize(14)
##        font.setBold(False)
##        font.setWeight(50)
##        item.setFont(font)
##        item.setBackground(QtGui.QColor(180, 180, 180))
##        self.tableWidget_2.setHorizontalHeaderItem(0, item)
##        item=QtGui.QTableWidgetItem("Fixture Type")
##        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
##        font = QtGui.QFont()
##        font.setPointSize(14)
##        font.setBold(False)
##        font.setWeight(50)
##        item.setFont(font)
##        item.setBackground(QtGui.QColor(180, 180, 180))
##        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        for i in range(len(GV.FixtureInfo)):
            GrpNo=GV.FixtureInfo[i][0]
            Fixtype=GV.FixtureInfo[i][1]
            self.tableWidget_2.setItem(i,0, QTableWidgetItem(str(GrpNo)))
            self.tableWidget_2.setItem(i,1, QTableWidgetItem(str(Fixtype)))



    def send_data(self):
        module_type=self.lineEdit.text()
        GroupNo=self.lineEdit_2.text()
        Leak=self.comboBox_7.currentText()
        Navsts=self.comboBox_2.currentText()
        Connpres=self.comboBox_4.currentText()
        Seclock=self.comboBox_5.currentText()
        serIP=self.comboBox_3.currentText()
        Ejests=self.comboBox.currentText()
        Actuation=self.comboBox_6.currentText()
        if(len(module_type)>0 and len(GroupNo)>0):
            Fixture_Setting=[(GroupNo,module_type,Leak,Navsts,Connpres,Seclock,serIP,Ejests,Actuation)]
            UploadFixtureType(Fixture_Setting)
            self.ShowModuledata()
            self.quit_msg="Saved Successfully"
            self.popupmeassage()
        else:
            self.quit_msg="Fill All Fields"
            self.popupmeassage()
            
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = Fixture_library()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
