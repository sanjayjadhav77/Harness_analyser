import sys
sys.path.insert(1, '/home/pi/Desktop/HA_Analyzer/code/tester_files')
import os
from PyQt4 import QtCore, QtGui
import cutting_chart2
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from  Sql_db import *
import global_test_var as GV
import global_var 
from global_files import*

class cutting_chart_window(QtGui.QMainWindow,cutting_chart2.Ui_MainWindow):               # class of admin page

    def __init__(self):
        super(cutting_chart_window,self).__init__()
        self.setupUi(self)
        self.read_val_frm_db()
    def loaddata(self):
        
        for i in range(len(GV.cutting_chartData)):
            read=GV.cutting_chartData[i]
            for j in range(len(read)):
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(read[j])))

    def read_val_frm_db(self):
        GV.cutting_chartData=DownloadCutting_ChartData(GV.Location_No)
        self.loaddata()
        
##class cutting_chart_window(QtGui.QFrame, cutting_chart2.Ui_Form):
##    def __init__(self):
##        super(self.__class__,self).__init__()
##        self.setupUi(self)
##        print("GV.cutting_chartData",GV.cutting_chartData)
####        self.loaddata()
##    def loaddata(self):
##        
##        for i in range(len(GV.cutting_chartData)):
##            read=GV.cutting_chartData[i]
##            for j in range(len(read)):
##                self.tableWidget.setItem(i,j, QTableWidgetItem(str(read[j])))
##        for i in range (len(GV.From_Temp)):
##            x.tableWidget.setItem(i,0, QTableWidgetItem('Continuity'))
##            x.tableWidget.setItem(i,1, QTableWidgetItem(str(GV.Name_Temp[i])))
##            x.tableWidget.setItem(i,2, QTableWidgetItem(str(GV.From_Temp[i])))
##            x.tableWidget.setItem(i,3, QTableWidgetItem(str(GV.To_Temp[i])))
##            x.tableWidget.setItem(i,4, QTableWidgetItem(str(GV.Color_Temp[i])))
##            
            
##
##def main():
##    app = QtGui.QApplication(sys.argv)
##    app.setApplicationName('phonon Player')
##    f = cutting_chart_window()
##    f.show()
##    app.exec_()
##    sys.exit(app.exec_())
##
##if __name__ == '__main__':
##    main()
