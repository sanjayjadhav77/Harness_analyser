
import global_var
from global_files import*
import message_library

class message_library_page(QtGui.QMainWindow,message_library.Ui_MainWindow):   # class of contactus page

    def __init__(self):
        super(message_library_page,self).__init__()
        self.setupUi(self)
##        self.pushButton_3.clicked.connect(self.close_window)
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
                
##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = message_library_page()  
##    GUI.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
