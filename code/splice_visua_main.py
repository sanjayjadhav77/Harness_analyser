from global_files import*
import splice_visualization
from  Sql_db import *
from PyQt4 import QtGui, QtCore
import numpy as np
import cv2
import global_test_var as GV
class Splice_visual(QtGui.QMainWindow,splice_visualization.Ui_MainWindow):      # class of abt_tester page

    def __init__(self):
        super(Splice_visual,self).__init__()
        self.setupUi(self)
##        self.pushButton_2.clicked.connect(self.close_window)
        self.pushButton.clicked.connect(self.show_image)
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
        
    def show_image(self):
        Netnumber=self.lineEdit.text()
        if(len(Netnumber)>0):
            x=DownloadSplice1(GV.Location_No,Netnumber)
            try:
                nparr = np.fromstring(x[0][0], np.uint8)
                

                self.img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                cvt2qt = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], QtGui.QImage.Format_RGB888)
                ''' convert qt image to qt pixmap  '''
                pixmap = QtGui.QPixmap.fromImage(cvt2qt);
                ''' set pixmap on label  '''
                self.label.setPixmap(pixmap)
            except(IndexError):
                self.mess="Data Not Present at Location"
                self.clickMethod()
        else:
            self.mess="Enter Net Number"
            self.clickMethod()
    def clickMethod(self):
        QtGui.QMessageBox.about(self, "Message", self.mess)   
##
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = Splice_visual()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
