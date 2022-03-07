
import global_var
from global_files import*
import testing_flow
import global_test_var as GV 
class Testing_Flow(QtGui.QMainWindow,testing_flow.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(Testing_Flow,self).__init__()
        self.setupUi(self)
##        self.pushButton_4.clicked.connect(self.close_window)
        self.listWidget.itemClicked.connect(self.listwidgetclicked)
        self.pushButton_3.clicked.connect(self.Save_Message)
        self.pushButton_5.clicked.connect(self.set_preferance)
    def set_preferance(self):
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        row = self.tableWidget.currentRow()
        self.tableWidget.setItem(row, 0,QtGui.QTableWidgetItem(str(row+1)))
        self.tableWidget.setItem(row, 1,QtGui.QTableWidgetItem(str(GV.List_message)))
        print(row)
    def Save_Message(self):
        
        row=self.tableWidget.rowCount()
        col=self.tableWidget.columnCount()
        preference=[]
        for i in range(row):
            try:
                item = self.tableWidget.item(i, 1).text()
                if(item=='W/H presense'):
                    item=1
                if(item=='Leak Test'):
                    item=2
                if(item=='1st Stage'):
                    item=3
                if(item=='2nd Stage'):
                    item=4
                if(item=='Printing'):
                    item=5
                if(item=='Match Label'):
                    item=6
                if(item=='Actuations'):
                    item=7
                if(item=='Remove Harness'):
                    item=8
                if(item=='Custom Test'):
                    item=9
                if(item=='Report Generation'):
                    item=10
                preference.append(item)
                row+= 1
            except AttributeError:
                preference.append(0)

        print("preference",preference)
        UploadCable_OP_Settings(GV.Location_No,preference)
    def listwidgetclicked(self, item):
##        print('click -> {}'.format(item.text()))
        GV.List_message=(item.text())
##        print("GV.List_message -> ",GV.List_message)
    
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)

    def readvaluefrom_db(self):
        self.listWidget.clear()
        ls=['W/H presense','Leak Test','1st Stage','2nd Stage','Printing',
            'Match Label','Actuations','Remove Harness','Custom Test','Report Generation']  
##        for i in range (len(ls)):
##            self.listWidget.addItem(ls[i])
        self.listWidget.addItems(ls)

        
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = Testing_Flow()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
