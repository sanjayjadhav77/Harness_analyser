from global_files import*
from PyQt4 import QtGui, QtCore, uic
from PyQt4 import QtCore, QtGui
import fo
import sys
import global_test_var as GV

class Ui_Dialog(QtGui.QDialog,fo.Ui_Dialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setText(str(GV.FoQty))
        self.lineEdit.setEnabled(False)
        self.pushButton.clicked.connect(self.enter_fo_qty)
        GV.Set_fo_flag=0
    def enter_fo_qty(self):
        
        self.close()
        GV.module_no=8
        GV.Estate=2
        
        print('set')

    
        
        
# def main():
#    app = QtGui.QApplication(sys.argv)
#    GUI = Ui_Dialog()
#    GUI.setGeometry(120,76,1101,332)
#    GUI.show()
#    app.exec_()

# if __name__ == '__main__':
#    main()
