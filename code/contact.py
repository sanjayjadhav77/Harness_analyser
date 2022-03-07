
import global_var
from global_files import*
import contact_screen

class contactUs_page(QtGui.QMainWindow,contact_screen.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(contactUs_page,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("About Us")
        self.centerOnScreen()
    def centerOnScreen (self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        x=(resolution.width() / 2) - (self.frameSize().width() / 2)
        y=(resolution.height() / 2) - (self.frameSize().height() / 2)
        self.move(x,y) 
        
                
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = contactUs_page()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
