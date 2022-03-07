import global_var
from global_files import*
import teaching_4
import global_test_var as GV
from  Sql_db import *
class teaching_page4(QtGui.QMainWindow,teaching_4.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(teaching_page4,self).__init__()
        self.setupUi(self)
        self.checkBox.stateChanged.connect(self.use_gbl_settings)

##        self.pushButton_5.clicked.connect(self.close_window)
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
       
    def read_grp_data_frm_db(self):
        self.grp2_table.clear()
##        print('read_grp_data_frm_db',GV.Location_No,GV.Local_Group2_File)
        for i in range(len(GV.Local_Group2_File)):
            grp2_data=(GV.Local_Group2_File[i])
            for j in range(len(grp2_data)):
                grp_pts=grp2_data[j]
                self.grp2_table.setItem(i,j, QTableWidgetItem(str(grp_pts)))
        print('set grp table')
        
    def save(self):
        
        self.pushButton.setStyleSheet("background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Main_Btn/btn_press.png);color: rgb(255, 255, 255);")
        row=self.grp2_table.rowCount()
        col=self.grp2_table.columnCount()
        grp2_list= [[] for i in range(128)]
        print("check..............................................")
        for i in range(row):
            for j in range(col):
                try:
                    item = self.grp2_table.item(i, j).text()
                    try:
                        grp2_list[i].append(int(item))
                        row+=1
                    except ValueError:
                        print('grp2_table valueerror')
                except AttributeError:
                    row+= 1                
        grp_lst=[]
        
        for i in range(len(grp2_list)):
##            if(len(grp2_list[i])>0):
            grp_lst.append(sorted(grp2_list[i]))
       
        GV.Local_Group2_File=grp_lst
        print("grp_lst",GV.Local_Group2_File)
        self.grp2_table.clear()
        for i in range(len(grp_lst)):
            grp2_data=grp_lst[i]
            for j in range(len(grp2_data)):
                grp_pts=grp2_data[j]
                self.grp2_table.setItem(i,j, QTableWidgetItem(str(grp_pts)))
        output1=DownloadGlobal_Grp2_Cavity()
        output2=[]
        for i in output1:
            if len(i)>0:
                output2.append(i)
        print('grp_lst222',output2)
        
        UploadLocal_Grp2(GV.Location_No,grp_lst,output2)
        DownloadLocal_Grp2(GV.Location_No)
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Group File Updated','Group File Updated')
        
        
    def use_gbl_settings(self,event):
        circuit=[]
        if (self.checkBox.isChecked() == True):
##            self.read_local_data_frm_db()
            Get_num_stages(GV.Location_No)
            for i in range(GV.Num_Stages):
                DownloadHarnessData(GV.Location_No,i+1)
                for j in range (len(GV.circuits)):
                    circuit.append(GV.circuits[j])
            z=[]
            print("usegbsetting circuits",circuit)
            for i in range (len(circuit)):
                for j in range (len(circuit[i])):
                    for k in range (len(GV.Group_data)):
                            if (circuit[i][j] in (GV.Group_data[k])):
                                    if(((GV.Group_data.index(GV.Group_data[k]))+1) not in z):
                                        z.append(GV.Group_data.index((GV.Group_data[k]))+1)
            z=sorted(z)
            
            DownloadGlobal_Grp2_forlocalgrp(z)
            GV.data_Available=7
        elif (self.checkBox.isChecked() == False):
            self.grp2_table.clear()
            
    def read_local_data_frm_db(self):
        self.grp2_table.clear()
##        print('read_grp_data_frm_db',GV.Location_No,GV.Local_Group2_File)
        Global_Group2_File = DownloadGlobal_Grp2()
        for i in range(len(Global_Group2_File)):
            local_data=(Global_Group2_File[i])
            for j in range(len(local_data)):
                pts=local_data[j]
                self.grp2_table.setItem(i,j, QTableWidgetItem(str(pts)))
        print('set grp table')
            
    def data_frm_usb(self):
        self.pushButton_4.setStyleSheet("background-image: url(/home/pi/Desktop/AWHT/UI_files/final_assets/Tertiary_Btn/P.png);color: rgb(38, 177, 255);")
##        file_name=QFileDialog.getOpenFileName(self, 'Open file', '/media/usb0')
        file_name=QFileDialog.getOpenFileName(self, 'Open file', '/media/pi/Ubuntu 18_04_4 LTS amd64')
        try:
            book = xlrd.open_workbook(str(file_name))
            print('file_name',file_name)
            s = book.sheet_by_index(0)
            colm_counts=s.ncols
            rows_counts=s.nrows  
            for col in range(colm_counts):
                for row in range(rows_counts):
                    cell_value= s.cell_value(row,col)
                    cell=cell_value
                    if (type(cell)==type(1.0)):
                        cell=int(cell)
                    self.grp2_table.setItem(row,col,QTableWidgetItem(str(cell)))
        except FileNotFoundError:
            print('file not selected')

##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = teaching_page4()
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()

