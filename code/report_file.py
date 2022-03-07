
import global_var
from global_files import*
import Test_report
import global_test_var as GV
class Test_Report(QtGui.QMainWindow,Test_report.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(Test_Report,self).__init__()
        self.setupUi(self)
        
        self.pushButton_2.clicked.connect(self.export_report)
        self.pushButton_3.clicked.connect(self.searchpdf)
        self.lineEdit.returnPressed.connect(self.find)
        self.pushButton_4.clicked.connect(self.find)
        self.tableWidget_2.cellClicked.connect(self.cell_was_clicked)
        self.lineEdit.mousePressEvent=self.search_label
    def find(self):
        x=self.lineEdit.text()

        for i in range (len(self.seacing)):
            
            if(x==self.seacing[i]):
                self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
                self.tableWidget_2.setCurrentCell (i, 0)
                self.viewClicked()
        self.lineEdit.clear()


    def viewClicked(self):
        
        self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
        row = self.tableWidget_2.currentRow()
        
        self.serialnum=(self.tableWidget_2.item(row,1)).text()
        print("srno",self.serialnum)

  
    def search_label(self,event):
        completer = QtGui.QCompleter(self.seacing)
        self.lineEdit.setCompleter(completer)
    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))
##        item = self.tableWidget_2.itemAt(row, column)
        self.serialnum =(self.tableWidget_2.item(row,column)).text()
         
        print("self.serialnum",self.serialnum)
    def get_information(self):
        self.tableWidget_2.clear()
        item=QtGui.QTableWidgetItem("Date")
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(180, 180, 180))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item=QtGui.QTableWidgetItem("Serial No")
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(180, 180, 180))
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item=QtGui.QTableWidgetItem("Status")
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(180, 180, 180))
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        try:
            path='/home/pi/Desktop/.HA_Editor/Reports'+ '/' + str(GV.Location_No)
            print("path......",path)
            self.Norecord=0
            self.file_list = []
            self.seacing=[]
            GV.filename=[]
            for i in os.listdir(path):
                a = os.stat(os.path.join(path,i))
                if '.pdf' in i:
                    self.file_list.append([i,time.ctime(a.st_atime)]) #[file,most_recent_access,created]
            print("file_list",self.file_list)
            for i in range(len(self.file_list)):
                
                
                self.val=self.file_list[i][0]
                self.No=self.val.split('.')
                GV.filename.append(self.No[0])
                
                self.stno=self.No[0].split('_')
                self.seacing.append(self.stno[0])
                
                self.dt=self.file_list[i][1][4:10]+','+' '+self.file_list[i][1][20:24]
                self.tableWidget_2.setItem(i,0, QTableWidgetItem(self.dt))
                self.tableWidget_2.setItem(i,1, QTableWidgetItem(self.stno[0]))
                self.tableWidget_2.setItem(i,2, QTableWidgetItem(self.stno[1]))
            print("self.seacing",self.seacing)
        except(FileNotFoundError):
            self.Norecord=1
            self.mess = "No Record Found"
            self.clickMethod()
    def clickMethod(self):
        QtGui.QMessageBox.about(self, "Message", self.mess)
    def searchpdf(self):
        
        for i in GV.filename:
            a=i.split('_')
            if (a[0]==self.serialnum):
                GV.name=i
		

        try:
            file_path='/home/pi/Desktop/HA_Editor/Reports'+ '/' + str(GV.Location_No) + '/' + str(GV.name) + '.pdf'
            print(file_path)
            os.system('xdg-open '+file_path+'')
            open(file_path)
        except(OSError):
            pass
        
            
        self.lineEdit.clear()
    def export_report(self):
        if(self.Norecord==0):
            
            usb_detect = len(next(os.walk('/media/usb0'))[1])
            if(usb_detect>0):
                x=0
                for i in range (len(self.file_list)):
                    No=self.file_list[i][0].split('.')
                    y=No[0].split('_')
                    if(self.serialnum==y[0]):
                            
                        
                        src_loc='/home/pi/Desktop/.HA_Editor/Reports'+ '/' + str(GV.Location_No) + '/'+self.file_list[i][0]
                        des_loc= ' /media/usb0/Test_Reports'
                        os.system("sudo cp -R "+src_loc + des_loc)
                        
                        x=1
                if(x==0):
                    self.mess = "Serial number Not Selected"
                    self.clickMethod()
                else:
                    self.mess = "Report Exported "
                    self.clickMethod()
                
            else:
                print('log_file not saved')
                quit_msg = "Usb Drive Not Detected"

                reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Ok,)
        else:
            self.mess = "No Record To Export"
            self.clickMethod()
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = Test_Report()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
