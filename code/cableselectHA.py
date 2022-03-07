import global_var
from global_files import*
import cable_selectHA
from  Sql_db import *
import global_test_var as GV
from HDM import *
from CAN_Bus import *

class cable_selctionHA(QtGui.QMainWindow,cable_selectHA.Ui_MainWindow):   # class of select part/tech page1
    def __init__(self):
        super(cable_selctionHA,self).__init__()
        self.setupUi(self)
        self.read_cable_info_frm_db()
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.operator_page)
        self.pushButton.setToolTip("<font color=""black"">Teaching2 Page</font>")
        self.tableWidget_2.clicked.connect(self.viewClicked)
        self.lineEdit.mousePressEvent=self.search_label
        self.lineEdit.returnPressed.connect(self.find)
        self.pushButton_3.clicked.connect(self.op_code_save)
        self.pushButton_4.clicked.connect(self.find)
        self.label_49.mousePressEvent=self.op_toggle
        global_var.op_c=0
        self.op_toggle(1)
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
    def operator_page(self):# Arrow click
        GV.Card_counter=card_status()
        GV.total_point=GV.Card_counter*64
        card_init()
        GV.is_card_sequential=Card_sequential()
        maxpoint=[]
        if(GV.Num_Stages>0):
            for a in range(GV.Num_Stages):
                DownloadHarnessData(GV.Location_No,a+1)
                for i in range(len(GV.circuits)):
                    for j in range (len(GV.circuits[i])):
                        maxpoint.append(GV.circuits[i][j])
                # print(maxpoint)
            try:
                circuitmax=max(maxpoint)
            except(ValueError):
                circuitmax=0
                pass    
                # print(circuitmax)
            if(circuitmax>GV.total_point):
                print("popup message")
                self.quit_msg="Required Card Not available"
                self.popupmeassage()
            else:
                print(GV.led )
                for i in range(len(GV.led)):
                    single_write(GV.led[i][1],1)
                global_var.state_machine = 4
                global_var.state_machine_flag = 1
                print('log', global_var.state_machine_flag, global_var.state_machine)
        
                self.pushButton.setStyleSheet("background-image: url(:/images/final_assets/Slide_Page/nxt_press.png);")
        else:
            print("data not available Learn harness")
            self.quit_msg="Data Not available\n First Learn Harness"
            self.popupmeassage()        
    def viewClicked(self):#on click table   
        GV.stage_list=[]
        print(GV.led )
        for i in range(len(GV.led)):
            single_write(GV.led[i][1],0) 
        self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
        row = self.tableWidget_2.currentRow()
        rw_data=(self.tableWidget_2.item(row,0)).text()
        part_Name=(self.tableWidget_2.item(row,1)).text()
##        print("part_Name",part_Name)
        GV.Part_Name=part_Name
        GV.Location_No=int(rw_data)
        self.pushButton.setEnabled(True)
##        UpLoadCableId(GV.Location_No,GV.Part_Name)
        global_var.cable_change_flag=1
##        cable_name_update(self)

        print('cble',GV.Location_No,GV.Part_Name)
        UpLoadCableId(GV.Location_No,GV.Part_Name)
    def read_cable_info_frm_db(self):# read cable data at the time of cable selection
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
    def op_toggle(self,event):# no of operator toggle button
        if(global_var.op_c==0):
            global_var.op_c=1            
            self.label_56.show()
            self.label_57.hide()
            self.label_49.setStyleSheet("""background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Toggle_Num/no.png);color: rgb(255, 255, 255);font: 75 10pt "Roboto [GOOG]";""")
            self.label_49.setText('01')
            self.label_49.setAlignment(Qt.AlignRight)
            self.label_49.setAlignment(Qt.AlignVCenter)
            self.label_49.setIndent(30)
        elif(global_var.op_c==1):
            global_var.op_c=0
            self.label_56.hide()
            self.label_57.show()
            self.label_49.setStyleSheet("""background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Toggle_Num/yes.png);color: rgb(255, 255, 255);font: 75 10pt "Roboto [GOOG]";""")
            self.label_49.setText('02')
            self.label_49.setAlignment(Qt.AlignLeft)
            self.label_49.setAlignment(Qt.AlignVCenter)
            self.label_49.setIndent(15) 
    def op_code_save(self):# Operator code save
        self.pushButton_3.setStyleSheet("""background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Main_Btn/btn_press.png);color: rgb(255, 255, 255);font: 14pt "Roboto [GOOG]";""")
        op_no=self.label_49.text()
        code=self.op_code_line.text()
        if(len(op_no)>0 and len(code)>0):
            if(op_no=='01'):
                code1=self.op_code_line.text()
                print("code1",code1)
            else:
                code2=self.op_code_line.text()
                print("code2",code2)
            self.quit_msg="Operator Saved"
            self.popupmeassage()
            self.op_code_line.clear()
        else:
            self.quit_msg="Enter Data"
            self.popupmeassage()
    def search_label(self,event):# for cable no search 
        self.cbl_data=DownloadCableId_All()
        self.model = []
        for x in (self.cbl_data):
            self.model.append(x[1])
        completer = QtGui.QCompleter(self.model)
        self.lineEdit.setCompleter(completer)
    def find(self):# search button
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
##    GUI = cable_selctionHA()
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()

