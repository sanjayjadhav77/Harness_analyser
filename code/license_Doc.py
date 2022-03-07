
import global_var
from global_files import*
import licensce

class license_page(QtGui.QMainWindow,licensce.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(license_page,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("licence and legality ")
        self.textEdit.setReadOnly(True)
        self.centerOnScreen()
    def centerOnScreen (self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        x=(resolution.width() / 2) - (self.frameSize().width() / 2)
        y=(resolution.height() / 2) - (self.frameSize().height() / 2)
        self.move(x,y) 
       
                
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = license_page()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
