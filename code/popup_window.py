from global_files import*
from PyQt4 import QtGui, QtCore, uic
from PyQt4 import QtCore, QtGui
import popup
import sys

class Ui_Dialog(QtGui.QDialog,popup.Ui_Dialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)
        self.setFocus()
        self.pushButton.clicked.connect(self.process_cmplt_popup)
        print('okkkkkkk')
    def process_cmplt_popup(self):
        self.close()
##        global_var.state_machine=8
##        global_var.state_machine_flag=1
        
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = Ui_Dialog()
##    GUI.setGeometry(120,76,1101,332)
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
