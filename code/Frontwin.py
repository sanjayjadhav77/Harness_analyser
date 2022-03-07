
##import global_var
from global_files import*
import Front_window

class Front_win(QtGui.QMainWindow,Front_window.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(Front_win,self).__init__()
        self.setupUi(self)
        pixmap = QPixmap('/home/pi/Desktop/.HA_Editor/UI_files/final_assets/kalp_logo_Font.jpg')
        self.label.setPixmap(pixmap)
##        self.label.setScaledContents(True)
                
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = Front_win()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
