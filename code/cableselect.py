import global_var
from global_files import*
import cable_select
from  Sql_db import *
import global_test_var as GV

class cable_selction(QtGui.QMainWindow,cable_select.Ui_MainWindow):   # class of select part/tech page1
    def __init__(self):
        super(cable_selction,self).__init__()
        self.setupUi(self)
        self.read_cable_info_frm_db()
        self.tableWidget_2.clicked.connect(self.viewClicked)
        self.lineEdit.mousePressEvent=self.search_label
        self.lineEdit.returnPressed.connect(self.find)
        self.pushButton_4.clicked.connect(self.find)
##        self.pushButton_3.clicked.connect(self.close_window)
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)

    def viewClicked(self):
        
        self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
        row = self.tableWidget_2.currentRow()
        rw_data=(self.tableWidget_2.item(row,0)).text()
        part_Name=(self.tableWidget_2.item(row,1)).text()
##        print("part_Name",part_Name)
        GV.Part_Name=part_Name
        GV.Location_No=int(rw_data)
##        self.pushButton.setEnabled(True)
        UpLoadCableId(GV.Location_No,GV.Part_Name)
        global_var.cable_change_flag=1
##        cable_name_update(self)
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
                global_var.cable_change_flag=1
                self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
                self.tableWidget_2.setCurrentCell (x, 0)
                self.viewClicked()
        self.lineEdit.clear()
       
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = cable_selction()
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()

