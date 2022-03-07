import global_var
from global_files import*
import teaching_1
from  Sql_db import *
import global_test_var as GV

class teaching_page1(QtGui.QMainWindow,teaching_1.Ui_MainWindow):   # class of select part/tech page1
    def __init__(self):
        super(teaching_page1,self).__init__()
        self.setupUi(self)
        self.read_cable_info_frm_db()
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.open_teaching2_page)
        self.pushButton.setToolTip("<font color=""black"">Teaching2 Page</font>")
        self.tableWidget_2.clicked.connect(self.viewClicked)
        self.lineEdit.mousePressEvent=self.search_label
        self.pushButton_4.clicked.connect(self.find)
##        self.pushButton_3.clicked.connect(self.close_window)
        self.lineEdit.returnPressed.connect(self.find)
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)

    def open_teaching2_page(self):
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Next Button','Teaching page 2')
        global_var.state_machine=15
        global_var.state_machine_flag=1
##        print("global_var.state_machine",global_var.state_machine)
        self.pushButton.setStyleSheet("background-image: url(:/images/final_assets/Slide_Page/nxt_press.png);")
                
    def viewClicked(self):
        self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
        row = self.tableWidget_2.currentRow()
        rw_data=(self.tableWidget_2.item(row,0)).text()
        part_Name=(self.tableWidget_2.item(row,1)).text()
##        print("part_Name",part_Name)
        GV.Part_Name=part_Name
        GV.Location_No=int(rw_data)
        self.pushButton.setEnabled(True)
        UpLoadCableId(GV.Location_No,GV.Part_Name)
        global_var.cable_change_flag=1
        print('cble',GV.Location_No,GV.Part_Name)
        UpLoadCableId(GV.Location_No,GV.Part_Name)
    def read_cable_info_frm_db(self):
        cbl_data=DownloadCableId_All()
        
        
        pts=DownloadCable_Info_all()
        final_data=[]     
        for i in range (len(cbl_data)):
            temp=cbl_data[i]
            final_data.append([])
            for j in range(len(temp)):
                final_data[i].append(temp[j])
            for j in range(len(temp)):
                final_data[i].append((pts[i])[j])
                
        for i in range(len(final_data)):
            abc=final_data[i]
            for j in range(len(abc)):
                abc2=abc[j]
                self.tableWidget_2.setItem(i,j, QTableWidgetItem(str(abc2)))
    
    def search_label(self,event):
        self.cbl_data=DownloadCableId_All()
        self.model = []
        for x in (self.cbl_data):
            self.model.append(x[1])
        completer = QtGui.QCompleter(self.model)
        self.lineEdit.setCompleter(completer)
    def find(self):
        search_text=self.lineEdit.text()
        
        for x in range (len(self.cbl_data)):
            if (search_text == self.cbl_data[x][1]):
                self.pushButton.setEnabled(True)
                global_var.cable_change_flag=1
                self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
                self.tableWidget_2.setCurrentCell (x, 0)
                self.viewClicked()
        self.lineEdit.clear()
       
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = teaching_page1()
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()

