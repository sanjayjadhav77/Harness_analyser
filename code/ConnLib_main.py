import sys
##sys.path.insert(1, '/home/pi/Desktop/AWHT/code/tester_files')
from PyQt4 import QtGui, QtCore
import numpy as np
import cv2
from  Sql_db import *
import global_test_var as GV
import global_var
from global_files import*
import ConnLibCreation

class Connlibrary(QtGui.QMainWindow, ConnLibCreation.Ui_MainWindow):
    def __init__(self):
        super(Connlibrary, self).__init__()
##        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
        self.setupUi(self)
        '''  LineEdit to get connector name  '''
        self.e1 = self.lineEdit_5
        
        '''  LineEdit to get total count of pins on connector  '''
        self.e2 = self.lineEdit_2
        self.m_data = []
        self.c_data = []
        
        '''  PushButton to call openf()  '''
        self.pushButton_3.clicked.connect(self.openf)
        self.pushButton_2.clicked.connect(self.close_win)
##        self.pushButton_4.clicked.connect(self.close_main_window)
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
#        ''' offset for square width which will be drawn on image  '''
        self.offset = 11
        self.verticalSlider.setValue(11)
        self.verticalSlider.valueChanged.connect(self.sl_val)
        self.radioButton.toggled.connect(self.sl_val)
        self.lineEdit_2.setValidator(QIntValidator(1, 999))
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
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
    def close_win(self):
        print(self.m_data)
        try:
            UploadConnectorImages(tuple([self.e1.text(),self.binimg]))
            if(len(self.m_data)>0):
                UploadCavityMap(self.m_data)
                print("after",self.m_data)
                self.quit_msg="Saved Successfully"
                self.popupmeassage()
            else:
                self.quit_msg="Complete Tranning !!!"
                self.popupmeassage()
        except(AttributeError,IndexError):
            self.quit_msg="Filled Data First"
            self.popupmeassage()
        """       function to read image file     """
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
    def sl_val(self):
        ''' offset for square width which will be drawn on image  '''
        self.offset = self.verticalSlider.value()
        try:
            if(self.radioButton.isChecked()):
                start_pt = (self.x-self.offset,self.y-self.offset)
                end_pt = (self.x+self.offset,self.y+self.offset)
                self.clone = self.img.copy()
                cv2.rectangle(self.clone, start_pt,end_pt, (0, 255, 0), 1)
            else:
                self.clone = self.img.copy()
                center=(self.x,self.y)
                cv2.ellipse(self.clone, center, ((self.offset)+1,(self.offset)+1), 0, 0, 360, (0,255,0),1)
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
    def get_data(self):
        try:
    ##    if(int(self.e3.text())<=int(self.e2.text())):
            if(not(self.e3.text() in self.entries)):
##                print("self.entries",self.entries,self.e2.text())
                if(len(self.entries)<int(self.e2.text())):
                    if(len(self.e3.text())>0):
                        self.entries.insert(len(self.entries),(self.e3.text()))
                        if(self.radioButton.isChecked()):
                            sh=1
                        else:
                            sh=0
                        self.m_data.append(tuple([self.e1.text(),self.e3.text(),
                                                  self.x,self.y,sh,
                                                  self.verticalSlider.value()]))
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
        except(ValueError):
            self.mess = "Enter cavities"
            self.clickMethod()

    def clickMethod(self):
        QtGui.QMessageBox.about(self, "WARNING", self.mess)
#        msg.setIcon(QtWidgets.QMessageBox.Warning)
        
    """     function to get (x,y) cordinate from image and
            draw square on the image 
            and insert LineEdit on image    """
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
            cv2.rectangle(self.clone, start_pt,end_pt, (0, 255, 0), 1)
        else:
            self.clone = self.img.copy()
            center=(self.x,self.y)
            cv2.ellipse(self.clone, center, ((self.offset)+1,(self.offset)+1), 0, 0, 360, (0,255,0),1)
            
        
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
        
    def openf(self):
        print(self.e1.text())
        ConnList = get_ConLib(self.e1.text())
        print(ConnList)
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home/pi/Desktop/.HA_Editor/code/tester_files/Connector_Images',"Image files (*.jpg *.png)")
        print("fileName",fileName)
        cname=(fileName.split('/')[-1]).split('.')[0]
        self.e1.setText(str(cname))
      
        if(self.e1.text() in str(ConnList)):
            
            self.mess = "connector name already exists"
            self.clickMethod()
            print("connector name already exists")
        else:
            self.entries = []
            self.m_data = []

            self.read_file(fileName)



##if __name__ == "__main__":
##    app = QtGui.QApplication(sys.argv)
##    w = Connlibrary()
##    w.show()
##    sys.exit(app.exec_())
