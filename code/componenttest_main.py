
import global_var
from global_files import*
import component_test
import global_test_var as GV

class Component_Testing(QtGui.QMainWindow,component_test.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(Component_Testing,self).__init__()
        self.setupUi(self)
        
##        self.pushButton_3.clicked.connect(self.close_window)
        self.pushButton.clicked.connect(self.loadtodb)
        self.tableWidget_2.clicked.connect(self.viewClicked)
        self.comboBox.currentIndexChanged.connect(self.changeUnit)
        self.lineEdit_3.setValidator(QIntValidator(1, 999999))
        self.lineEdit_6.setValidator(QIntValidator(1, 99))
        self.lineEdit_4.setValidator(QIntValidator(1, 9999))
        self.lineEdit_5.setValidator(QIntValidator(1, 9999))
    def changeUnit(self):
        if(self.comboBox.currentIndex()==0):
            self.comboBox_2.setCurrentIndex(0)
        elif(self.comboBox.currentIndex()==1):
            self.comboBox_2.setCurrentIndex(1)
        elif(self.comboBox.currentIndex()==2):
            self.comboBox_2.setCurrentIndex(2)
            
            
    def clickMethod(self):
        QtGui.QMessageBox.about(self, "Message", self.mess)
    def readvaluefrom_db(self):
##        DownloadComp_data(GV.Location_No,GV.stage)
        GV.data_Available=8
    def viewClicked(self):
        try:
            self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
            row = self.tableWidget_2.currentRow()
            GV.Component_Type=(self.tableWidget_2.item(row,0)).text()
            if(GV.Component_Type=='Resistor'):
                GV.Unit='ohm'
            elif(GV.Component_Type=='Capacitor'):
                GV.Unit='F'
            GV.Comp_value=(self.tableWidget_2.item(row,1)).text()
            GV.Tollerance=(self.tableWidget_2.item(row,2)).text()
            GV.point1=(self.tableWidget_2.item(row,3)).text()
            GV.point2=(self.tableWidget_2.item(row,4)).text()
            index = self.comboBox.findText(GV.Component_Type, QtCore.Qt.MatchFixedString)
            if index >= 0:
                 self.comboBox.setCurrentIndex(index)
            index1 = self.comboBox_2.findText(GV.Unit, QtCore.Qt.MatchFixedString)
            if index1 >= 0:
                 self.comboBox_2.setCurrentIndex(index1)
            self.lineEdit_3.setText(str(GV.Comp_value))
            self.lineEdit_6.setText(str(GV.Tollerance))
            self.lineEdit_4.setText(str(GV.point1))
            self.lineEdit_5.setText(str(GV.point2))

        except(AttributeError):
            print("Blank Row Selected")
        
  
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
    def loadtodb(self):
        try:

            self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
            row1 = self.tableWidget_2.currentRow()
            print(row1,type(row1),"jdbfILDJVB")
            if(row1>=0):
                GV.Component_Type=self.comboBox.currentText()
                GV.Comp_value=self.lineEdit_3.text()
                GV.Tollerance=self.lineEdit_6.text()
                GV.Unit=self.comboBox_2.currentText()
                GV.point1=self.lineEdit_4.text()
                GV.point2=self.lineEdit_5.text()
                if(len(GV.Comp_value)>0 and len(GV.Tollerance)>0 and len(GV.point1)>0 and len(GV.point2)>0):
                    self.tableWidget_2.setItem(row1, 0,QtGui.QTableWidgetItem(str(GV.Component_Type)))
                    self.tableWidget_2.setItem(row1, 1,QtGui.QTableWidgetItem(str(GV.Comp_value)))
                    self.tableWidget_2.setItem(row1, 2,QtGui.QTableWidgetItem(str(GV.Tollerance)))
                    self.tableWidget_2.setItem(row1, 3,QtGui.QTableWidgetItem(str(GV.point1)))
                    self.tableWidget_2.setItem(row1, 4,QtGui.QTableWidgetItem(str(GV.point2)))

                    pt1=GV.virtual_pins[GV.Actual_pins.index(int(GV.point1))]
                    pt2=GV.virtual_pins[GV.Actual_pins.index(int(GV.point2))]
                    print("pt1,pt2",pt1,pt2)
                    Uploadcomponent_data(GV.Location_No,GV.Component_Type,GV.Comp_value,GV.Tollerance,pt1,pt2)
                    self.lineEdit_3.clear()
                    self.lineEdit_6.clear()
                    self.lineEdit_4.clear()
                    self.lineEdit_5.clear()
                    self.mess="Saved Successfully"
                    self.clickMethod()
                else:
                    self.mess="Fill All Values"
                    self.clickMethod()
            else:
                self.mess="Select Row First"
                self.clickMethod()
        except(ValueError):
            self.mess="Select Row You want to Edit\n  Or Enter Values"
            self.clickMethod()
            
##        
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = Component_Testing()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
