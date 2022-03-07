import global_var
from global_files import*
import teaching_2
from  Sql_db import *
import global_test_var as GV


class teaching_page2(QtGui.QMainWindow,teaching_2.Ui_MainWindow):   # class of select part/tech page1
    def __init__(self):
        super(teaching_page2,self).__init__()
        self.setupUi(self)

        self.label_5.hide()            
        self.label_13.hide()
        self.label_25.hide()
        self.label_29.hide()
        self.label_32.hide()
        # self.label_58.hide()
        self.label_55.hide()
        self.label_49.hide()
        self.stackedWidget.setCurrentIndex(0)


        self.actuations.mousePressEvent = self.actuation_page
        self.facilities.mousePressEvent = self.facility_page
        self.facilities_2.mousePressEvent = self.Assetcode_page
    
        self.pushButton_4.clicked.connect(self.save_setting)
        self.pushButton_5.clicked.connect(self.Set_data)
        self.pushButton_6.clicked.connect(self.save_setting)
        self.label_4.mousePressEvent = self.buzzer_on_off
        self.label_15.mousePressEvent = self.cutter_on_off
        self.label_48.mousePressEvent = self.Component_test
        self.label_54.mousePressEvent = self.Auto_Mode
        

        self.label_26.mousePressEvent = self.lbl_on_off
        self.label_47.mousePressEvent = self.total_lbls
        self.label_38.mousePressEvent = self.barcode_match_y_n

        # self.label_57.mousePressEvent = self.All_Error
        # self.label_60.mousePressEvent = self.All_Circuits_mode


        self.label_20.mousePressEvent = self.bar_no_1
        self.label_44.mousePressEvent = self.bar_no_1
        self.label_14.mousePressEvent = self.bar_no_1
        self.label_23.mousePressEvent = self.bar_no_2        
        self.label_21.mousePressEvent = self.bar_no_2
        self.label_45.mousePressEvent = self.bar_no_2
        self.label_22.mousePressEvent = self.bar_no_3
        self.label_46.mousePressEvent = self.bar_no_3
        self.label_24.mousePressEvent = self.bar_no_3

        self.checkBox.stateChanged.connect(self.use_gbl_settings)
##        self.pushButton_3.clicked.connect(self.close_window)
        self.lineEdit_11.setValidator(QIntValidator(1, 999))
        self.lineEdit_10.setValidator(QIntValidator(1, 20))
        self.lineEdit_61.setValidator(QIntValidator(1, 9))
        self.lineEdit_58.setValidator(QIntValidator(1, 9))
        self.lineEdit_59.setValidator(QIntValidator(1, 9))
        self.lineEdit_60.setValidator(QIntValidator(1, 9))
        self.lineEdit_6.setValidator(QIntValidator(1, 15))
        self.lineEdit_11.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_10.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_61.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_58.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_59.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_60.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_6.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))

        self.lineEdit_3.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_4.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_5.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_15.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_16.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_17.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
        self.lineEdit_18.setValidator(QRegExpValidator(QRegExp("[0-9_]+")))
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
    def close_window(self):
        global_var.state_machine = 1
        global_var.state_machine_flag = 1
        print('log', global_var.state_machine_flag, global_var.state_machine)
                
    def actuation_page(self,event):
        self.checkBox.setHidden(False)
        self.stackedWidget.setCurrentIndex(0)
        self.actuations.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_select.png);color: rgb(255, 255, 255);font: 14pt "Roboto [GOOG]";""")
        self.facilities.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);color: rgb(0, 0, 0);font: 14pt "Roboto [GOOG]";""")
        self.facilities_2.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);color: rgb(0, 0, 0);font: 14pt "Roboto [GOOG]";""")
        
    def facility_page(self,event):
        self.checkBox.setHidden(False)
        self.stackedWidget.setCurrentIndex(1)
        self.actuations.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);color: rgb(0, 0, 0);font: 14pt "Roboto [GOOG]";""")
        self.facilities.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_select.png);color: rgb(255, 255, 255);font: 14pt "Roboto [GOOG]";""")
        self.facilities_2.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);color:rgb(0, 0, 0) ;font: 14pt "Roboto [GOOG]";""")
        
    def Assetcode_page(self,event):
        self.checkBox.setHidden(True)
        self.stackedWidget.setCurrentIndex(2)
        self.actuations.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);color: rgb(0, 0, 0);font: 14pt "Roboto [GOOG]";""")
        self.facilities.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_unselect.png);color: rgb(0, 0, 0);font: 14pt "Roboto [GOOG]";""")
        self.facilities_2.setStyleSheet("""border-image: url(:/images/final_assets/Page_Toggle/page_select.png);color: rgb(255, 255, 255);font: 14pt "Roboto [GOOG]";""")


        
    
    def acuation_db_read(self):
        self.lineEdit.setText(str(GV.Location_No))
        self.lineEdit_2.setText(str(GV.Part_Name))
        self.lineEdit_3.setText(str(GV.Release_Time))
        self.lineEdit_4.setText(str(GV.Q_Mark_Time))
        self.lineEdit_5.setText(str(GV.Fail_Time))
        self.lineEdit_15.setText(str(GV.Open_point_Timeout))
        self.lineEdit_16.setText(str(GV.Short_point_Timeout))
        self.lineEdit_17.setText(str(GV.Interchange_point_Timeout))
        self.lineEdit_18.setText(str(GV.Extra_point_Timeout))
        
        if(GV.Buzzer_Status==0):
            global_var.buzz_on_off=0
            self.buzzer_on_off(1)
        else:
            global_var.buzz_on_off=1
            self.buzzer_on_off(1)           
        if(GV.Cutter_status==0):
            global_var.cut_on_off=0
            self.cutter_on_off(1)
        else:
            global_var.cut_on_off=1
            self.cutter_on_off(1)
            
#----------------------------------------Actuation fun-------------------------------------------------------------------------------------------------------------#            
        
    def buzzer_on_off(self,event):
        if(global_var.buzz_on_off==0):
            global_var.buzz_on_off=1
            GV.Buzzer_Status=0
            self.label_11.show()
            self.label_5.hide()
            self.label_4.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_4.setText('Fail')
            self.label_4.setAlignment(Qt.AlignRight)
            self.label_4.setAlignment(Qt.AlignVCenter)
            self.label_4.setIndent(11)
        elif(global_var.buzz_on_off==1):
            global_var.buzz_on_off=0
            GV.Buzzer_Status=1
            self.label_11.hide()
            self.label_5.show()
            self.label_4.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_4.setText('Pass')
            self.label_4.setAlignment(Qt.AlignLeft)
            self.label_4.setAlignment(Qt.AlignVCenter)
            self.label_4.setIndent(25)
            
    def cutter_on_off(self,event):
        if(global_var.cut_on_off==0):
            global_var.cut_on_off=1
            GV.Cutter_status=0
            self.label_16.show()
            self.label_13.hide()
            self.label_15.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_15.setText('No')
            self.label_15.setAlignment(Qt.AlignRight)
            self.label_15.setAlignment(Qt.AlignVCenter)
            self.label_15.setIndent(11)
        elif(global_var.cut_on_off==1):
            global_var.cut_on_off=0
            GV.Cutter_status=1
            self.label_16.hide()
            self.label_13.show()
            self.label_15.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_15.setText('Yes')
            self.label_15.setAlignment(Qt.AlignLeft)
            self.label_15.setAlignment(Qt.AlignVCenter)
            self.label_15.setIndent(25)

    def extra_pt_on_off(self,event):
        if(global_var.ext_pt_on_off==0):
            global_var.ext_pt_on_off=1
            GV.Extra_Point_Test=0
            self.label_19.show()
            self.label_17.hide()
            self.label_18.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_18.setText('No')
            self.label_18.setAlignment(Qt.AlignRight)
            self.label_18.setAlignment(Qt.AlignVCenter)
            self.label_18.setIndent(11)
        elif(global_var.ext_pt_on_off==1):
            global_var.ext_pt_on_off=0
            GV.Extra_Point_Test=1
            self.label_19.hide()
            self.label_17.show()
            self.label_18.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_18.setText('Yes')
            self.label_18.setAlignment(Qt.AlignLeft)
            self.label_18.setAlignment(Qt.AlignVCenter)
            self.label_18.setIndent(25)
#----------------------------------------Facilities fun-------------------------------------------------------------------------------------------------------------#           
    def facilities_db_read(self):
        print("GV.Num_Stages",GV.Num_Stages,type(GV.Num_Stages))
        self.lineEdit_6.setText(str(GV.Num_Stages))
        self.lineEdit_6.setReadOnly(True)
        self.comboBox.setCurrentIndex(GV.All_Error)
        if(GV.LabelPrint==0):
            global_var.lbl_y_n=0
            self.lbl_on_off(1)            
        else:
            global_var.lbl_y_n=1
            self.lbl_on_off(1)
            
        if(GV.LabelNos==0):
            global_var.no_of_lbl=1
            self.total_lbls(1)
        else:
            global_var.no_of_lbl=0
            self.total_lbls(1)    

        if(GV.Barcode_Match==0):
            global_var.bar_y_n=0
            self.barcode_match_y_n(1)        
        else:

            global_var.bar_y_n=1
            self.barcode_match_y_n(1)

        if(GV.Component_status==0):
            global_var.onpass_on_off=0
            self.Component_test(1)
        else:
            global_var.onpass_on_off=1
            self.Component_test(1)

        # if(GV.All_Error==0):
        #     global_var.All_Error_yn=0
        #     self.All_Error(1)
        # else:
        #     global_var.All_Error_yn=1
        #     self.All_Error(1)
        # if(GV.All_circuits_Mode==0):
        #     global_var.All_circuits_yn=0
        #     self.All_Circuits_mode(1)
        # else:
        #     global_var.All_circuits_yn=1
        #     self.All_Circuits_mode(1)
            
##        if(GV.External_Interface==0):
##            global_var.External_Interface_yn=0
##            self.External_Interface(1)
##        else:
##            global_var.External_Interface_yn=1
##            self.External_Interface(1)

        if(GV.Auto_Mode==0):
            global_var.Auto_Mode_yn=0
            self.Auto_Mode(1)
        else:
            global_var.Auto_Mode_yn=1
            self.Auto_Mode(1)
            
        if(GV.No_Of_Barcodes==1):
            global_var.no_1=1
            self.bar_no_1(1)

        elif(GV.No_Of_Barcodes==2):
            global_var.no_2=1
            self.bar_no_2(1)

        else:
            global_var.no_3=1
            self.bar_no_3(1)

    def lbl_on_off(self,event):
##        UploadLog_Data(GV.Location_No,GV.Part_Name,'Label ','Clicked')
        if(global_var.lbl_y_n==0):
            global_var.lbl_y_n=1
            GV.LabelPrint=0
            self.label_27.show()
            self.label_25.hide()
            self.label_26.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_26.setText('No')
            self.label_26.setAlignment(Qt.AlignRight)
            self.label_26.setAlignment(Qt.AlignVCenter)
            self.label_26.setIndent(11)
        elif(global_var.lbl_y_n==1):
            global_var.lbl_y_n=0
            GV.LabelPrint=1
            self.label_27.hide()
            self.label_25.show()
            self.label_26.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_26.setText('Yes')
            self.label_26.setAlignment(Qt.AlignLeft)
            self.label_26.setAlignment(Qt.AlignVCenter)
            self.label_26.setIndent(25)
      
    def total_lbls(self,event):
        if(global_var.no_of_lbl==0):
            global_var.no_of_lbl=1
            GV.LabelNos=1
            self.label_31.show()
            self.label_32.hide()
            self.label_47.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_47.setText('01')
            self.label_47.setAlignment(Qt.AlignRight)
            self.label_47.setAlignment(Qt.AlignVCenter)
            self.label_47.setIndent(30)
            
        elif(global_var.no_of_labels==1):    
            global_var.no_of_lbl=0
            GV.LabelNos=2
            self.label_31.hide()
            self.label_32.show()
            self.label_47.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_47.setText('02')
            self.label_47.setAlignment(Qt.AlignLeft)
            self.label_47.setAlignment(Qt.AlignVCenter)
            self.label_47.setIndent(15)

    def Component_test(self,event):
        if(global_var.onpass_on_off==0):
            global_var.onpass_on_off=1
            GV.Component_status=0
            self.label_50.show()
            self.label_49.hide()
            self.label_48.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_48.setText('No')
            self.label_48.setAlignment(Qt.AlignRight)
            self.label_48.setAlignment(Qt.AlignVCenter)
            self.label_48.setIndent(11)
        elif(global_var.onpass_on_off==1):
            global_var.onpass_on_off=0
            GV.Component_status=1
            self.label_50.hide()
            self.label_49.show()
            self.label_48.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_48.setText('Yes')
            self.label_48.setAlignment(Qt.AlignLeft)
            self.label_48.setAlignment(Qt.AlignVCenter)
            self.label_48.setIndent(25)

    def Leak_test(self,event):
        if(global_var.Leak_on_off==0):
            global_var.Leak_on_off=1
            GV.Leak_test_yn=0
            self.label_63.show()
            self.label_61.hide()
            self.label_60.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_60.setText('Fail')
            self.label_60.setAlignment(Qt.AlignRight)
            self.label_60.setAlignment(Qt.AlignVCenter)
            self.label_60.setIndent(11)
        elif(global_var.Leak_on_off==1):
            global_var.Leak_on_off=0
            GV.Leak_test_yn=1
            self.label_63.hide()
            self.label_61.show()
            self.label_60.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_60.setText('Pass')
            self.label_60.setAlignment(Qt.AlignLeft)
            self.label_60.setAlignment(Qt.AlignVCenter)
            self.label_60.setIndent(25)
    def barcode_match_y_n(self,event):
        if(global_var.bar_y_n==0):
            global_var.bar_y_n=1
            GV.Barcode_Match=0
            self.label_30.show()
            self.label_29.hide()
            self.label_38.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_38.setText('No')
            self.label_38.setAlignment(Qt.AlignRight)
            self.label_38.setAlignment(Qt.AlignVCenter)
            self.label_38.setIndent(11)
            
        elif(global_var.bar_y_n==1):    
            global_var.bar_y_n=0
            GV.Barcode_Match=1
            self.label_30.hide()
            self.label_29.show()
            self.label_38.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_38.setText('Yes')
            self.label_38.setAlignment(Qt.AlignLeft)
            self.label_38.setAlignment(Qt.AlignVCenter)
            self.label_38.setIndent(25)
            
    def External_Interface(self,event):
        if(global_var.External_Interface_yn==0):
            global_var.External_Interface_yn=1
            GV.External_Interface=0
            self.label_53.show()
            self.label_52.hide()
            self.label_51.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_51.setText('No')
            self.label_51.setAlignment(Qt.AlignRight)
            self.label_51.setAlignment(Qt.AlignVCenter)
            self.label_51.setIndent(11)
            
        elif(global_var.External_Interface_yn==1):    
            global_var.External_Interface_yn=0
            GV.External_Interface=1
            self.label_53.hide()
            self.label_52.show()
            self.label_51.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_51.setText('Yes')
            self.label_51.setAlignment(Qt.AlignLeft)
            self.label_51.setAlignment(Qt.AlignVCenter)
            self.label_51.setIndent(25)       

    def Auto_Mode(self,event):
        if(global_var.Auto_Mode_yn==0):
            global_var.Auto_Mode_yn=1
            GV.Auto_Mode=0
            self.label_56.show()
            self.label_55.hide()
            self.label_54.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_54.setText('No')
            self.label_54.setAlignment(Qt.AlignRight)
            self.label_54.setAlignment(Qt.AlignVCenter)
            self.label_54.setIndent(11)
            
        elif(global_var.Auto_Mode_yn==1):    
            global_var.Auto_Mode_yn=0
            GV.Auto_Mode=1
            self.label_56.hide()
            self.label_55.show()
            self.label_54.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_54.setText('Yes')
            self.label_54.setAlignment(Qt.AlignLeft)
            self.label_54.setAlignment(Qt.AlignVCenter)
            self.label_54.setIndent(25)          
    # def All_Error(self,event):
    #     if(global_var.All_Error_yn==0):
    #         global_var.All_Error_yn=1
    #         GV.All_Error=0
    #         self.label_59.show()
    #         self.label_58.hide()
    #         self.label_57.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
    #         self.label_57.setText('No')
    #         self.label_57.setAlignment(Qt.AlignRight)
    #         self.label_57.setAlignment(Qt.AlignVCenter)
    #         self.label_57.setIndent(11)
            
    #     elif(global_var.All_Error_yn==1):    
    #         global_var.All_Error_yn=0
    #         GV.All_Error=1
    #         self.label_59.hide()
    #         self.label_58.show()
    #         self.label_57.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
    #         self.label_57.setText('Yes')
    #         self.label_57.setAlignment(Qt.AlignLeft)
    #         self.label_57.setAlignment(Qt.AlignVCenter)
    #         self.label_57.setIndent(25)

    # def All_Circuits_mode(self,event):
    #     if(global_var.All_circuits_yn==0):
    #         global_var.All_circuits_yn=1
    #         GV.All_circuits_Mode=0
    #         self.label_63.show()
    #         self.label_61.hide()
    #         self.label_60.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
    #         self.label_60.setText('No')
    #         self.label_60.setAlignment(Qt.AlignRight)
    #         self.label_60.setAlignment(Qt.AlignVCenter)
    #         self.label_60.setIndent(11)
            
    #     elif(global_var.All_circuits_yn==1):    
    #         global_var.All_circuits_yn=0
    #         GV.All_circuits_Mode=1
    #         self.label_63.hide()
    #         self.label_61.show()
    #         self.label_60.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
    #         self.label_60.setText('Yes')
    #         self.label_60.setAlignment(Qt.AlignLeft)
    #         self.label_60.setAlignment(Qt.AlignVCenter)
    #         self.label_60.setIndent(25)       

    def two_stage_on_off(self,event):
        
##        global_var.two_stage_y_n=1
        if(global_var.two_stage_y_n==0):
            global_var.two_stage_y_n=1
            GV.Stage_on=0
            GV.flagx=0
            print("global_var.two_stage_y_n1",global_var.two_stage_y_n)
            print("GV.flagx1",GV.flagx)
            self.label_40.show()
            self.label_39.hide()
            self.label_41.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/no.png);color: rgb(255, 255, 255);")
            self.label_41.setText('No')
            self.label_41.setAlignment(Qt.AlignRight)
            self.label_41.setAlignment(Qt.AlignVCenter)
            self.label_41.setIndent(11)
            
        elif(global_var.two_stage_y_n==1):    
            global_var.two_stage_y_n=0
            GV.Stage_on=1
            GV.flagx=1
            print("global_var.two_stage_y_n1",global_var.two_stage_y_n)
            print("GV.flagx2",GV.flagx)
            self.label_40.hide()
            self.label_39.show()
            self.label_41.setStyleSheet("background-image: url(:/images/final_assets/Toggle_yes_no/yes.png);color: rgb(255, 255, 255);")
            self.label_41.setText('Yes')
            self.label_41.setAlignment(Qt.AlignLeft)
            self.label_41.setAlignment(Qt.AlignVCenter)
            self.label_41.setIndent(25)

    def bar_no_1(self,event):
        if (global_var.no_1==1):
            global_var.no_1=0
            GV.No_Of_Barcodes=1
            self.label_23.clear()
            self.label_24.clear()
            self.label_21.setEnabled(False)
            self.label_23.setEnabled(False)
            self.label_45.setEnabled(False)
            
            self.label_22.setEnabled(False)
            self.label_24.setEnabled(False)
            self.label_46.setEnabled(False)
            self.pixmap = QPixmap(':/images/final_assets/Checkbox/check.png')
            self.label_14.setPixmap(self.pixmap)
            
        elif (global_var.no_1==0):
            global_var.no_1=1
            self.label_14.clear()
            self.label_21.setEnabled(True)
            self.label_23.setEnabled(True)
            self.label_45.setEnabled(True)
            
            self.label_22.setEnabled(True)
            self.label_24.setEnabled(True)
            self.label_46.setEnabled(True)

    def bar_no_2(self,event):
        if (global_var.no_2==1):
            global_var.no_2=0
            GV.No_Of_Barcodes=2
            self.label_14.clear()
            self.label_24.clear()

            self.label_20.setEnabled(False)
            self.label_14.setEnabled(False)
            self.label_44.setEnabled(False)
            
            self.label_22.setEnabled(False)
            self.label_46.setEnabled(False)    
            self.label_24.setEnabled(False)

            self.pixmap = QPixmap(':/images/final_assets/Checkbox/check.png')
            self.label_23.setPixmap(self.pixmap)
            
        elif (global_var.no_2==0):
            global_var.no_2=1
            self.label_23.clear()
            self.label_20.setEnabled(True)
            self.label_14.setEnabled(True)
            self.label_44.setEnabled(True)
            
            self.label_22.setEnabled(True)
            self.label_46.setEnabled(True)    
            self.label_24.setEnabled(True)

    def bar_no_3(self,event):
        UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Bar No 3','Clicked')
        if (global_var.no_3==1):
            global_var.no_3=0
            GV.No_Of_Barcodes=3
            self.label_14.clear()
            self.label_23.clear()

            self.label_20.setEnabled(False)
            self.label_14.setEnabled(False)
            self.label_44.setEnabled(False)
            
            self.label_21.setEnabled(False)
            self.label_23.setEnabled(False)
            self.label_45.setEnabled(False)
            
            self.pixmap = QPixmap(':/images/final_assets/Checkbox/check.png')
            self.label_24.setPixmap(self.pixmap)
            
        elif (global_var.no_3==0):
            global_var.no_3=1
            self.label_24.clear()
            self.label_20.setEnabled(True)
            self.label_14.setEnabled(True)
            self.label_44.setEnabled(True)
            
            self.label_21.setEnabled(True)
            self.label_23.setEnabled(True)
            self.label_45.setEnabled(True)
            
    def use_gbl_settings(self,event):
        if self.checkBox.isChecked():
            global_var.Global_Settings_File = DownloadGLobal_Cable_Settings()
            print("Global_Settings_File",global_var.Global_Settings_File)
            self.gbl_acuation_db_read()
            self.gbl_facilities_db_read()
        else:
            print("unchecked")
            
       
    def gbl_acuation_db_read(self):
        automanual=global_var.Global_Settings_File[0][0]
        Release_Time_2=global_var.Global_Settings_File[0][1]
        Q_Mark_Time_2=global_var.Global_Settings_File[0][2]
        failtime=global_var.Global_Settings_File[0][3]
        Buzzer_Status_2=global_var.Global_Settings_File[0][4]
        Extra_Point_Test_2=global_var.Global_Settings_File[0][5]
        Cutter_status_2=global_var.Global_Settings_File[0][6]
        Open_point_Timeout_2=global_var.Global_Settings_File[0][7]
        Short_point_Timeout_2=global_var.Global_Settings_File[0][8]
        Interchange_point_Timeout_2=global_var.Global_Settings_File[0][9]
        Extra_point_Timeout_2=global_var.Global_Settings_File[0][10]
        noofstages=global_var.Global_Settings_File[0][17]
                 
        self.lineEdit.setText(str(GV.Location_No))
        self.lineEdit_2.setText(str(GV.Part_Name))
        self.lineEdit_3.setText(str(Release_Time_2))
        self.lineEdit_4.setText(str(Q_Mark_Time_2))
        self.lineEdit_5.setText(str(failtime))
        self.lineEdit_15.setText(str(Open_point_Timeout_2))
        self.lineEdit_16.setText(str(Short_point_Timeout_2))
        self.lineEdit_17.setText(str(Interchange_point_Timeout_2))
        self.lineEdit_18.setText(str(Extra_point_Timeout_2))
        self.lineEdit_6.setText(str(noofstages))
##        if (noofstages=='0'):
##            self.comboBox.setCurrentIndex(0)
##        elif(noofstages=='1'):
##            self.comboBox.setCurrentIndex(1)
##        else:
##            self.comboBox.setCurrentIndex(2)
        if(automanual==0):
            global_var.Auto_Mode_yn=0
            self.Auto_Mode(1)
        else:
            global_var.Auto_Mode_yn=1
            self.Auto_Mode(1)
        if(Buzzer_Status_2==0):
            global_var.buzz_on_off=0
            self.buzzer_on_off(1)
        else:
            global_var.buzz_on_off=1
            self.buzzer_on_off(1)           
        if(Cutter_status_2==0):
            global_var.cut_on_off=0
            self.cutter_on_off(1)
        else:
            global_var.cut_on_off=1
            self.cutter_on_off(1)
##        if(Extra_Point_Test_2==0):
##            global_var.ext_pt_on_off=0
##            self.extra_pt_on_off(1)
##        else:
##            global_var.ext_pt_on_off=1
##            self.extra_pt_on_off(1)      

    def gbl_facilities_db_read(self):
        LabelPrint_2=global_var.Global_Settings_File[0][11]
        LabelNos_2=global_var.Global_Settings_File[0][12]
        Barcode_Match_2=global_var.Global_Settings_File[0][13]
        No_Of_Barcodes_2=global_var.Global_Settings_File[0][14]
        allerror=global_var.Global_Settings_File[0][15]
        comptest=global_var.Global_Settings_File[0][16]

        print('LabelPrint_2',LabelPrint_2)
        print('LabelNos_2',LabelNos_2)
        print('Barcode_Match_2',Barcode_Match_2)
        print('Barcode_Match_2',Barcode_Match_2)

        if(GV.Component_status==0):
            global_var.onpass_on_off=0
            self.Component_test(1)
        else:
            global_var.onpass_on_off=1
            self.Component_test(1)

        self.comboBox.setCurrentIndex(allerror)
        # if(allerror==0):
        #     global_var.All_Error_yn=0
        #     self.All_Error(1)
        # else:
        #     global_var.All_Error_yn=1
        #     self.All_Error(1)
        if(LabelPrint_2==0):
            global_var.lbl_y_n=0
            self.lbl_on_off(1)            
        else:
            global_var.lbl_y_n=1
            self.lbl_on_off(1)
            
        if(LabelNos_2==0):
            global_var.no_of_lbl=1
            self.total_lbls(1)
        else:
            global_var.no_of_lbl=0
            self.total_lbls(1)    
     
        if(Barcode_Match_2==0):
            global_var.bar_y_n=0
            self.barcode_match_y_n(1)        
        else:
            global_var.bar_y_n=1
            self.barcode_match_y_n(1)        

        if(No_Of_Barcodes_2==1):
            global_var.no_1=1
            self.bar_no_1(1)

        elif(No_Of_Barcodes_2==2):
            global_var.no_2=1
            self.bar_no_2(1)

        else:
            global_var.no_3=1
            self.bar_no_3(1)
##=================================================================FOQty============================================================================================
    def Set_data(self):
        self.send_data()
        GV.flow =  self.comboBox_22.currentIndex()
        x=self.lineEdit_11.text()
        y=self.lineEdit_59.text()
        z=self.lineEdit_58.text()
        w=len(z)
        print("xy",x,y,type(z),type(w),z,w)
        if((len((self.lineEdit_10.text()).strip(' ')))>0):
            GV.Noofbar=self.lineEdit_10.text()
            
        else:
            GV.Noofbar='0'
            
        if((len(self.lineEdit_11.text()))>0):
            GV.FoQty=self.lineEdit_11.text()
            
        else:
            GV.FoQty='0'

        if((len(self.lineEdit_61.text()))>0):
            GV.Opcount=self.lineEdit_61.text()
            
        else:
            GV.Opcount='0'
        if((len(self.lineEdit_58.text()))>0):
            GV.Shcount=self.lineEdit_58.text()
            
        else:
            GV.Shcount='0'
        if((len(self.lineEdit_59.text()))>0):
            GV.Intercount=self.lineEdit_59.text()
            
        else:
            GV.Intercount='0'
        if((len(self.lineEdit_60.text()))>0):
            GV.Extracount=self.lineEdit_60.text()
            
        else:
            GV.Extracount='0'
        
        GV.sample_counter=0
        if (self.checkBox_30.isChecked()):
            GV.OpenPoint = '1'
        else:
            GV.OpenPoint = '0'
        if (self.checkBox_29.isChecked()):
            GV.ShortPoint = '1'
        else:
            GV.ShortPoint = '0'
        if (self.checkBox_28.isChecked()):
            GV.Interchange = '1'
        else:
            GV.Interchange = '0'
        if (self.checkBox_27.isChecked()):
            GV.ExtraPoint = '1'
        else:
           GV.ExtraPoint = '0'
    
        print("GV.OpenPoint",GV.OpenPoint)
        print("GV.OpenPoint",GV.ShortPoint)
        print("GV.OpenPoint",GV.Interchange)
        print("GV.OpenPoint",GV.ExtraPoint)
        

        Tp = [GV.FoQty,GV.flow,GV.Noofbar,GV.OpenPoint,GV.Opcount,GV.ShortPoint,GV.Shcount,GV.Interchange,GV.Intercount,GV.ExtraPoint,GV.Extracount]
        print("Tp",Tp)
        UploadAssetcode1(GV.Location_No,Tp)
        self.quit_msg = "Set Complete"
        self.popupmeassage()  
            
    def send_data(self):
##        try:
        row=self.tableWidget.rowCount()
        col=self.tableWidget.columnCount()
        grp2_list= [[] for i in range(row)]
        print("check..............................................",row,col)
        for i in range(row):
            for j in range(col):
                try:
##                    print("i,j",i,j)
                    item = self.tableWidget.item(i, j).text()
##                    print("item",item)
                    try:
                        grp2_list[i].append(item)
                        row+=1
                    except ValueError:
                        print('grp2_table valueerror')
                except AttributeError:
                    row+= 1
    
        tp=[x for x in grp2_list if x]
        print(tp,"tp")
        UploadAssetcode2(GV.Location_No,tp)
            
           
    def display_data(self):
        self.tableWidget.clear()
        item=QtGui.QTableWidgetItem("Serial No")
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(180, 180, 180))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item=QtGui.QTableWidgetItem("Asset Code")
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(180, 180, 180))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item=QtGui.QTableWidgetItem("Custom Message")
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(180, 180, 180))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        print("print here......",GV.prod_Setting,GV.prod_data)
        for i in range (len(GV.prod_data)):
            read = GV.prod_data[i]
            for j in range (len(read)):
                display_points=read[j]
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(display_points)))
        if (GV.flow=='0'):
            self.comboBox_22.setCurrentIndex(0)
        else:
            self.comboBox_22.setCurrentIndex(1)

        self.lineEdit_10.setText(str(GV.Noofbar))
        self.lineEdit_11.setText(str(GV.FoQty))
        self.lineEdit_61.setText(str(GV.Opcount))
        self.lineEdit_58.setText(str(GV.Shcount))
        self.lineEdit_59.setText(str(GV.Intercount))
        self.lineEdit_60.setText(str(GV.Extracount))
        

        if (GV.OpenPoint=='1'):
            self.checkBox_30.setChecked(True)
        else:
            self.checkBox_30.setChecked(False)

        if (GV.ShortPoint=='1'):
            self.checkBox_29.setChecked(True)
        else:
            self.checkBox_29.setChecked(False)

        if (GV.Interchange=='1'):
            self.checkBox_28.setChecked(True)
        else:
            self.checkBox_28.setChecked(False)

        if (GV.ExtraPoint=='1'):
            self.checkBox_27.setChecked(True)
        else:
            self.checkBox_27.setChecked(False)
        
##==================================================================End FO=========================================================================================
        
        
    def save_setting(self):
        # GV.NoofStages=self.lineEdit_6.text()
    
        self.pushButton_4.setStyleSheet("background-image: url(:/images/final_assets/Main_Btn/btn_press.png);color: rgb(255, 255, 255);")
        GV.Location_No=self.lineEdit.text()
        GV.Part_Name=self.lineEdit_2.text()
        GV.Release_Time=self.lineEdit_3.text()
        GV.Fail_Time=self.lineEdit_5.text()
        GV.Q_Mark_Time=self.lineEdit_4.text()
        GV.Open_point_Timeout=self.lineEdit_15.text()
        GV.Short_point_Timeout=self.lineEdit_16.text()
        GV.Interchange_point_Timeout=self.lineEdit_17.text()
        GV.Extra_point_Timeout=self.lineEdit_18.text()
        GV.All_Error= self.comboBox.currentIndex()
##        print(GV.Release_Time,GV.Fail_Time,type(GV.Fail_Time),type(GV.Release_Time))
        if(len(GV.Release_Time)>0 and len(GV.Fail_Time)>0 and len(GV.Q_Mark_Time)>0 and len(GV.Open_point_Timeout)>0 and len(GV.Short_point_Timeout)>0 and len(GV.Interchange_point_Timeout)>0 and len(GV.Extra_point_Timeout)>0):
            UpLoadCableId(GV.Location_No,GV.Part_Name)
            UploadCable_Settings(GV.Location_No)
            UploadSysLog_Data(GV.Location_No,GV.Part_Name,'Save','Saved Settings')
            print('hs done')
            self.quit_msg = "Settings Saved"
            self.popupmeassage()
        else:
            self.quit_msg = "Fill All Fields"
            self.popupmeassage()


##def main():
##    app = QtGui.QApplication(sys.argv)
##    GUI = teaching_page2()
##    GUI.show()
##    app.exec_()
##Akash
##if __name__ == '__main__':
##    main()

        
