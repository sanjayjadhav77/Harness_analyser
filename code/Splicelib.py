import global_var
from global_files import*
import Add_splice
import sys
##sys.path.insert(1, '/home/pi/Desktop/AWHT/code/tester_files')
from PyQt4 import QtGui, QtCore
import numpy as np
import cv2
from  Sql_db import *
import global_test_var as GV

class splice_library(QtGui.QMainWindow,Add_splice.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(splice_library,self).__init__()
        self.setupUi(self)
        self.e1 = self.lineEdit_6
        self.e2 = self.lineEdit_7
        self.s_data = []
##        self.pushButton_4.clicked.connect(self.close_window)
        self.pushButton_2.clicked.connect(self.openf)
        self.pushButton_6.clicked.connect(self.save_db)
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.offset = 11
        
        self.verticalSlider.setValue(11)
        self.verticalSlider.valueChanged.connect(self.sl_val)
        self.radioButton.toggled.connect(self.sl_val)
        self.lineEdit_7.setValidator(QIntValidator(1,9999))
        self.comboBox_7.currentIndexChanged.connect(self.clear_data)
    def clear_data(self):
        self.lineEdit_7.clear()
        self.lineEdit_6.clear()
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
    def save_db(self):
        print(self.s_data,len(self.e2.text()),len(self.e1.text()))
        try:
            img_encode = cv2.imencode('.png', self.img)[1]
            data_encode = np.array(img_encode)
            self.binimg = data_encode.tostring()
            if(self.comboBox_7.currentText()=='Net Number' or (len(self.e2.text())<=0) or (len(self.s_data))<=0):
                self.quit_msg="Check All Fields"
                self.popupmeassage()
                
            else:    
                UploadSplice1(tuple([GV.Location_No,GV.stage,self.comboBox_7.currentText(),self.e1.text(),self.binimg]),self.s_data)
                
                self.quit_msg="Saved Successfully"
                self.popupmeassage()
            
        except(AttributeError,IndexError):
            self.quit_msg="Filled Data First"
            self.popupmeassage()

        """       function to read image file     """
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
    def sl_val(self):
        ''' offset for square width which will be drawn on image  '''
        self.offset = self.verticalSlider.value()
        try:
            if(self.radioButton.isChecked()):
                start_pt = (self.x-self.offset,self.y-self.offset)
                end_pt = (self.x+self.offset,self.y+self.offset)
                self.clone = self.img.copy()
                cv2.rectangle(self.clone, start_pt,end_pt, (0, 255, 0), 2)
            else:
                self.clone = self.img.copy()
                center=(self.x,self.y)
                cv2.ellipse(self.clone, center, ((self.offset)+1,(self.offset)+1), 0, 0, 360, (0,255,0),2)
            self.e3.hide()
            ''' convert cv2 image to qt image  ''' 
            cvt2qt = QtGui.QImage(self.clone.data, self.clone.shape[1], self.clone.shape[0], QtGui.QImage.Format_RGB888)
           
            ''' convert qt image to qt pixmap  ''' 
            pixmap = QtGui.QPixmap.fromImage(cvt2qt);
            
            ''' set pixmap on label  ''' 
            self.label.setPixmap(pixmap);
        except:
            print('please open image first and click on a terminal')
        
        """     function to get pin number from LineEdit which is on image   """
    def read_file(self,filename):
        self.img = cv2.imread(filename)
        img_encode = cv2.imencode('.png', self.img)[1]
        data_encode = np.array(img_encode)
        self.binimg = data_encode.tostring()
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        cvt2qt = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(cvt2qt);
        self.label.setPixmap(pixmap);
        self.label.mousePressEvent = self.getPos
    def getPos(self , event):
        
        '''  extract (x,x) co-ordinate from event  '''
        self.x = event.pos().x()
        self.y = event.pos().y()
        
        '''  hide previously drawn LineEdit   '''
        try:
          self.e3.hide()
        except:
          print("An exception occurred") 

        if(self.radioButton.isChecked()):
            '''  Draw Rectangle on image  '''
            start_pt = (self.x-self.offset,self.y-self.offset)
            end_pt = (self.x+self.offset,self.y+self.offset)
            self.clone = self.img.copy()
            cv2.rectangle(self.clone, start_pt,end_pt, (0, 255, 0), 2)
        else:
            self.clone = self.img.copy()
            center=(self.x,self.y)
            cv2.ellipse(self.clone, center, ((self.offset)+1,(self.offset)+1), 0, 0, 360, (0,255,0),2)
            
        
        ''' convert cv2 image to qt image  ''' 
        cvt2qt = QtGui.QImage(self.clone.data, self.clone.shape[1], self.clone.shape[0], QtGui.QImage.Format_RGB888)
       
        ''' convert qt image to qt pixmap  ''' 
        pixmap = QtGui.QPixmap.fromImage(cvt2qt);
        
        ''' set pixmap on label  ''' 
        self.label.setPixmap(pixmap);
        
        '''  insert LineEdit on image  ''' 
        self.e3 = QtGui.QLineEdit(self.label)
        self.e3.setStyleSheet("color: rgb(0, 170, 255);"
                        "background-color: (253,253,253);"
                        "selection-color: yellow;"
                        "selection-background-color: blue;");
        self.e3.move(self.x+self.offset,self.y-self.offset)
        self.e3.resize(50,25)
        self.e3.show()
        self.e3.setFocus()
        
        ''' add callback to self.get_data(), it will be
            called when Enter key is pressed  ''' 
        self.e3.returnPressed.connect(self.get_data)
#        print(self.x,self.y)
    def get_data(self):
        if(not(self.e3.text() in self.entries)):
            if(len(self.entries)<int(self.e2.text())):
                if(len(self.e3.text())>0):
                    self.entries.insert(len(self.entries),(self.e3.text()))
                    if(self.radioButton.isChecked()):
                        sh=1
                    else:
                        sh=0
                    self.img = cv2.putText(self.img, self.e3.text(), (self.x - 5,self.y - 5), cv2.FONT_HERSHEY_PLAIN,
                                        1, (0, 255, 0), 1, cv2.LINE_AA)
                    self.s_data.append(tuple([self.e1.text(),self.e3.text(),
                                              self.x,self.y]))
#                        print(self.e3.text())
            else:
                self.mess = "Entries are more than total number of pins"
                self.clickMethod()
        else:
            self.mess = "Pin number repeated"
            self.clickMethod()
##        else:
##            self.mess = "Pin number can not be greater that number of cavity"
##            self.clickMethod()
        self.e3.hide()
    def clickMethod(self):
        QtGui.QMessageBox.about(self, "WARNING", self.mess)
    def openf(self):
        print(self.e1.text())
        SpliceList = get_SpliceLib(self.e1.text())
        print(SpliceList)
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home/pi/Desktop/.HA_Editor/code/tester_files/Splice Images',"Image files (*.jpg *.png)")
        print("fileName",fileName)
        spname=(fileName.split('/')[-1]).split('.')[0]
        self.e1.setText(str(spname))
      
        if(self.e1.text() in str(SpliceList)):
            
            self.mess = "connector name already exists"
            self.clickMethod()
            print("connector name already exists")
        else:
            self.entries = []
            self.s_data = []
                #        options = QtGui.QFileDialog.Options()
    #        options |= QtGui.QFileDialog.DontUseNativeDialog
    #        fileName, _ = QtGui.QFileDialog.getOpenFileName(
    #                        None,
    #                        "QFileDialog.getOpenFileName()",
    #                        "",
    #                        "Image Files (*.png)",
    #                        options=options)
            self.read_file(fileName)           
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = splice_library()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
