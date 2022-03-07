import sys
import os
from PyQt4 import QtCore, QtGui, uic
import grid_view2
from  Sql_db import *
import global_test_var as GV

class grid_window(QtGui.QFrame, grid_view2.Ui_Form):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        for i in range (len(GV.Fixture_Position)):
            row=int(GV.Fixture_Position[i][1])-1
            col_name=GV.Fixture_Position[i][0]
            if(col_name=='A'):
                col=0
            elif(col_name=='B'):
                col=1
            elif(col_name=='C'):
                col=2
            elif(col_name=='D'):
                col=3
            elif(col_name=='E'):
                col=4
            elif(col_name=='F'):
                col=5    
            elif(col_name=='G'):
                col=6
            elif(col_name=='H'):
                col=7
            elif(col_name=='I'):
                col=8
            elif(col_name=='J'):
                col=9
            elif(col_name=='K'):
                col=10

            # self.tableWidget.setItem(row, col, QtGui.QTableWidgetItem())
            self.tableWidget.setItem(row, col,QtGui.QTableWidgetItem(str(GV.Fixture_Position[i])))
            self.tableWidget.item(row, col).setBackground(QtGui.QColor(51,255,51))


                
            # print(i)

# def main():
#    app = QtGui.QApplication(sys.argv)
#    app.setApplicationName('phonon Player')
#    f = grid_window()
#    f.show()
#    app.exec_()
#    sys.exit(app.exec_())

# if __name__ == '__main__':
#    main()
