import sys
sys.path.insert(1, '/home/pi/Desktop/AWHT/code/tester_files')
from PyQt4 import QtGui, QtCore

import numpy as np
import cv2
import global_var
from global_files import*
import grplib 
from  Sql_db import *
import global_test_var as GV
class Groupcreation(QtGui.QMainWindow, grplib.Ui_MainWindow):
    def __init__(self):
        super(Groupcreation, self).__init__()
        self.setupUi(self)
        
        '''  LineEdit to get connector name  '''
#        self.e1 = self.lineEdit_5
        
        '''  LineEdit to get total count of pins on connector  '''
#        self.e2 = self.lineEdit_2
        # self.spinBox.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_4.setText('continuity')
        self.r_data = []
        self.c_data = []
        self.nCavity = 0
        self.ConnList = []
        self.pushButton_2.clicked.connect(self.Save_Data)
    
     
##        self.pushButton_3.clicked.connect(self.close_main_window)
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

    def close_main_window(self):
        global_var.state_machine = 23
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)

        '''  PushButton to call openf()  '''
    def setComboTxt(self,c,text):
        index = c.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
             c.setCurrentIndex(index)
    def add(self):
        get_lastCTpin()
        self.comboBox_8.clear()
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.comboBox_8.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
##        self.lineEdit_7.clear()
        self.lineEdit_6.clear()
        self.spinBox.setValue(0)
        self.spinBox_3.setValue(0)
        self.spinBox_2.setValue(0) 
        self.ConnList=[]
        for i in get_allConLib():
            self.ConnList.append(i[0])

        print(self.ConnList)
        for i in self.ConnList:
            self.comboBox_8.addItem(i)
        self.comboBox_8.currentIndexChanged.connect(self.selectConn)
        self.selectConn(0)
    def edit(self):
        get_lastCTpin()
        try:
            self.comboBox_8.clear()
##            print("GV.grp_id",GV.grp_id)
            self.lineEdit_3.setText(str(GV.grp_id))
            self.read_gloabl1_db()
            self.ConnList=[]
            for i in range(len(GV.leakage_gbl)):
                if(GV.grp_id == GV.leakage_gbl[i][0] ):
                    print(GV.leakage_gbl[i][0])
                    self.spinBox.setValue(GV.leakage_gbl[i][1])
                    self.spinBox_3.setValue(GV.switch_gbl[i][1])
                    self.spinBox_2.setValue(GV.led_gbl[i][1]) 
                          
            for i in get_allConLib():
                self.ConnList.append(i[0])
            
            print(self.ConnList)
            for i in self.ConnList:
                self.comboBox_8.addItem(i)
            self.comboBox_8.currentIndexChanged.connect(self.selectConn)
            self.selectConn(0)
            self.setComboTxt(self.comboBox_7,self.data[6])
            self.setComboTxt(self.comboBox_2,self.data[7])
            self.setComboTxt(self.comboBox_4,self.data[8])
            self.setComboTxt(self.comboBox_5,self.data[9])
            self.setComboTxt(self.comboBox,self.data[10])
            self.setComboTxt(self.comboBox_6,self.data[11])
            
            self.comboBox_9.setCurrentIndex(int(self.data[1]))    
            self.lineEdit_6.setText(self.data[2])

            self.lineEdit_4.setText(self.data[4])
            self.lineEdit_5.setText(self.data[3])
            output=get_LibMap1(self.data[3])

            self.setComboTxt(self.comboBox_8,str(output[0][1]))
            self.WriteTable(self.tableWidget)
        except(IndexError):
            pass
            
    def ReadTable(self,table):
        number_of_rows = table.rowCount()
        data = []
        for i in range(number_of_rows):

            if (not(table.item(i,1)==None)):
                if (len((table.item(i,1)).text())>0):
                    data.append(tuple([int(self.lineEdit_3.text()),int((table.item(i,0)).text()),int((table.item(i,1)).text())]))
        return (data)
    def WriteTable(self,table):
        data=[]
        self.tableWidget.setRowCount(0)
##        data=self.r_data[GV.grp_id-1]
        for i in range (len(self.r_data)):
            if(self.r_data[i][0]==GV.grp_id and self.r_data[i][4]=='CT'):
                data.append(self.r_data[i])
                
##        print("data....",data)
        for j in range (len(data)):
            self.tableWidget.insertRow(j)
            self.tableWidget.setItem(j, 0,QtGui.QTableWidgetItem(str(data[j][1])))
            self.tableWidget.setItem(j, 1,QtGui.QTableWidgetItem(str(data[j][2])))

    def read_gloabl1_db(self):
        Grp_1=DownloadGlobal_Grp1()
        for i in Grp_1:
            if (i[0]==GV.grp_id):

                self.data=i
                self.r_data=DownloadGlobal_Grp2()
   
    def selectConn(self,i):

        try:
            binimg = get_conn_Image(self.comboBox_8.currentText())[0][0]
            nparr = np.fromstring(binimg, np.uint8)
            

            self.img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.Cavities = get_conn_Cavity(self.comboBox_8.currentText())
    ##        print(self.Cavities)
            self.nCavity = len(self.Cavities)
            self.tableWidget.setRowCount(0)
    #        k=0
    #        k=self.tableWidget.rowCount()
    #        print(k)
            Cavity=[]
            xs = []
            ys = []
            fontscale=1/3
            clone = self.img.copy()
            for k in self.Cavities:
                clone = cv2.putText(clone, str(k[2]), (int(k[3])-4,int(k[4])-4), cv2.FONT_HERSHEY_SIMPLEX,  
                                    fontscale, (255, 0, 0), 1, cv2.LINE_AA)
                Cavity.append(k[2])
                xs.append(k[3])
                ys.append(k[4])
            #self.lineEdit_5.setText(self.comboBox_8.currentText())
            self.lineEdit_2.setText(str(self.nCavity))
            ''' convert cv2 image to qt image  '''
            cvt2qt = QtGui.QImage(clone.data, clone.shape[1], clone.shape[0], QtGui.QImage.Format_RGB888)
            ''' convert qt image to qt pixmap  '''
            pixmap = QtGui.QPixmap.fromImage(cvt2qt);
            ''' set pixmap on label  '''
            self.label.setPixmap(pixmap);
            for j in range(self.nCavity):
                self.tableWidget.insertRow(j)
                self.tableWidget.setItem(j, 0,QtGui.QTableWidgetItem(str(Cavity[j])))
        except:
            print("Connector not selected")
            


    def Save_Data(self):
        try:
            GV.r_data=[]

    #==================================globalfr2save==========================
    ##        print("GV.r_data...........",GV.r_data)
            
            print("GV.LstHWP........",GV.LstHWP,GV.lstCTP)
            FPos = self.lineEdit_6.text()
            GrpNo = int(self.lineEdit_3.text())
            FixTyp = self.lineEdit_4.text()
            ConnName = self.lineEdit_5.text()
            print("ConnName",GrpNo,ConnName,len(ConnName),FixTyp,FPos)
            leakcheck = self.comboBox_9.currentText()
            NaviStat = self.comboBox_7.currentText()
            ConnPres = self.comboBox_2.currentText()
            SecLock = self.comboBox_4.currentText()
            SensIn = self.comboBox_5.currentText()
            EjeStat = self.comboBox.currentText()
            FixAct = self.comboBox_6.currentText()
            
            
            nCavity = int(self.lineEdit_2.text())
            libname = str(self.comboBox_8.currentText())
            if(leakcheck=='Yes'):
                LeakStat=1
            else:
                LeakStat=0
                
            if(LeakStat==1):
                # GV.LstHWP=GV.LstHWP+1
                GV.Leakage=self.spinBox.value()
                x=(GrpNo,0,GV.Leakage,0,'LT')
                # print("GV.Leakage",GV.Leakage)
                GV.r_data.append(x)

            if(NaviStat=='Yes'):
                # GV.LstHWP=GV.LstHWP+1
                GV.navigation=self.spinBox_2.value()
                x=(GrpNo,0,GV.navigation,0,'NV')
                print("GV.navigation",GV.navigation)
                GV.r_data.append(x)

            if(ConnPres=='Yes'):
                # GV.LstHWP=GV.LstHWP+1
                GV.connpresence = self.spinBox_3.value()
                x=(GrpNo,0,GV.connpresence,0,'SW')
                print("GV.connpresence",GV.connpresence)
                GV.r_data.append(x)

            if(SecLock=='Yes'):
                # GV.LstHWP=GV.LstHWP+1
                GV.seclock = self.spinBox_4.value()
                x=(GrpNo,0,GV.seclock,0,'SL')
                GV.r_data.append(x)

            if(SensIn=='Yes'):
                # GV.LstHWP=GV.LstHWP+1
                GV.sensor_input=self.spinBox_5.value()
                x=(GrpNo,0,GV.sensor_input,0,'SI')
                GV.r_data.append(x)

            if(EjeStat=='Yes'):
                # GV.LstHWP=GV.LstHWP+1
                GV.ejectorstatus=self.spinBox_6.value()
                x=(GrpNo,0,GV.ejectorstatus,0,'ES')
                GV.r_data.append(x)

            if(FixAct=='Yes'):
                # GV.LstHWP=GV.LstHWP+1
                GV.fix_actuation = self.spinBox_7.value()
                print("fic actuation",GV.fix_actuation)
                x=(GrpNo,0,GV.fix_actuation,0,'FA')
                GV.r_data.append(x)

            
            tabledata = self.ReadTable(self.tableWidget)
            for i in range(len(tabledata)):
                GrpNo=tabledata[i][0]
                cavityno=tabledata[i][1]
                GV.LstHWP=tabledata[i][2]
                GV.lstCTP=GV.lstCTP+1
                x=(GrpNo,cavityno,GV.LstHWP,GV.lstCTP,'CT')
                GV.r_data.append(x)
            
            c_data = [tuple([GrpNo,LeakStat,FPos,ConnName,FixTyp,nCavity,NaviStat,
                            ConnPres,SecLock,SensIn,EjeStat,FixAct])]
            print("GV.r_data",GV.r_data)
            print("c_data",c_data)
            UploadGlobal_Grp2(GV.r_data)
            UploadGlobal_Grp1(c_data)
            UploadLocal_Grp1(c_data,GV.Location_No)
            UploadLibMap(tuple([GrpNo,ConnName,libname]))
            self.quit_msg = " Data Saved Succesfully "
            self.popupmeassage()
        except(ValueError):
            self.quit_msg = " Mandatory fields not Filled "
            self.popupmeassage()
       
        

#        sys.exit(app.exec_())

##if __name__ == "__main__":
##    app = QtGui.QApplication(sys.argv)
##    w = Groupcreation()
##    w.show()
##    sys.exit(app.exec_())
