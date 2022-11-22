import sys
sys.path.insert(1, '/home/pi/Desktop/.HA_Editor/code/tester_files')
import os
import new_Mdi
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import QMovie
from global_files import *
from  Sql_db import *
from Peripheral_Processes import*
import partload_main
import global_test_var as GV 
import random
import cv2
import global_var
import cutting_chart2
import grid_main
import cuttingChart_main
import HA_Diagno_main
import numpy as np
import threading
import warnings
import time
from HDM import *
global btnstate_flag



class mdiArea_window(QtGui.QMainWindow, new_Mdi.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        global btnstate_flag
        btnstate_flag=0
        
        self.p2= cuttingChart_main.cutting_chart_window()
        self.p3= grid_main.grid_window()
        self.p1= HA_Diagno_main.HA_dignostics_window()
        self.cutting()
        
        self.grid()
        self.Diagnostics()
        self.sp4.hide()
        self.sp3.hide()
        self.btnstate()
        self.mdiArea.tileSubWindows()
        self.pushButton.clicked.connect(self.btnstate)
        self.Enter_btn.clicked.connect(self.start_process)
        self.pushButton_2.clicked.connect(self.Previous)
        self.pushButton_3.clicked.connect(self.Next)
        self.label_21.mousePressEvent=self.production_sample
        self.barcode_scan_line.editingFinished.connect(self.barscancheck)
        self.pushButton_5.clicked.connect(self.abort_fun)
        self.pushButton_2.clicked.connect(self.Previous)
        self.pushButton_3.clicked.connect(self.Next)
         
    
    
    def Previous(self):
        GV.ClickOn_Next=0

    def Next(self):
        GV.ClickOn_Next=1
    def barscancheck(self):
        GV.scan_data=str(self.barcode_scan_line.text())
        
        print("GV.scan_data",GV.scan_data)
        if(len(GV.scan_data)>0):
            if(GV.Estate==0):
                Autopartload(self)
                        
                
    def abort_fun(self,event):        
        self.msg_line.setText("Harness Fail...")
        self.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: blue""")
        time.sleep(0.6)

        UploadProdLog_Data(GV.Location_No,GV.Part_Name,' Stop','Process Stop')
        UploadProdLog_Data(GV.Location_No,GV.Part_Name,' Stop',str(GV.Display_Message))
        
##        GV.Stop_Leakage=len(GV.switch)
        print('abort',global_var.p_s)
        card_init()
        if(GV.AssetCodeScan=='1'):
            if(global_var.p_s==0):
                global_var.p_s=1
                self.production_sample()
                GV.Fo_test_Flag=0
            else:
                global_var.p_s=0
                self.production_sample()
                GV.Fo_test_Flag=1       ###fo flag 
        GV.Abort_flag=1
        GV.Estate=0
        GV.PrvEstate=0
        
        GV.Intruption_flag=0
        time.sleep(0.6)
        GV.tested_circuits=[] 
        GV.x=1
        GV.y=1
        GV.Display_Message=''
        GV.module_no=0
        GV.Visual_Engine_Start=3
        
        GV.data_delivered=0
        
        self.msg_line.clear()
        GV.Multi_stage=1
        GV.time_gap=0
        GV.privious_x=0
        GV.privious_y=0
        GV.Privious_intpoint1=0
        GV.Privious_intpoint2=0
        GV.IO_error_code=1
        card_init()
        self.msg_line.setText("Put Cable")
        self.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: blue""")
        
        
        if(GV.Fail_Count>=999999):
            GV.Fail_Count=0
            GV.Fail_Count=GV.Fail_Count+1
        else:
            GV.Fail_Count=GV.Fail_Count+1
            UploadProdLog_Data(GV.Location_No,GV.Part_Name,' Abort Fail',str(GV.Fail_Count))
            
        self.fail_cnt_line.setText(str(GV.Fail_Count))
        x=[(GV.Pass_Count,GV.Fail_Count,GV.Stage1_status,GV.Stage1_Points_No,GV.Stage2_status,GV.Stage2_Points_No)]
        UploadCable_Info(GV.Location_No,x)
        global_var.state_machine_flag=1
        global_var.state_machine=4
        
      

    def production_sample(self,event):
        if(global_var.p_s==0):
            GV.Sample=0
            global_var.p_s=1
##                GV.abort_pass_fail=1
            self.label_21.setStyleSheet("""border-image: url(:/images/final_assets/Toggle_fun/pro_icon.png);color: rgb(255, 255, 255);font:12pt "Roboto [GOOG]";""")
            self.label_21.setText('Production')
            self.label_21.setAlignment(Qt.AlignLeft)
            self.label_21.setAlignment(Qt.AlignVCenter)
            self.label_21.setIndent(45)
        elif(global_var.p_s==1):
            global_var.p_s=0
            GV.Sample=1
            self.label_21.setStyleSheet("""border-image: url(:/images/final_assets/Toggle_fun/sample_icon.png);color: rgb(255, 255, 255);font:12pt "Roboto [GOOG]";""")
            self.label_21.setText('Sample')
            self.label_21.setAlignment(Qt.AlignRight)
            self.label_21.setAlignment(Qt.AlignVCenter)
            self.label_21.setIndent(30)

    def clickMethod(self):
        QtGui.QMessageBox.about(self, "Message", self.mess)
          
        
    def press_button(self,event):
        print("Button pressed")
        if (global_var.state_machine==4):
            self.start_process(event)
            self.Enter_btn.setStyleSheet("""background-image: url(:/images/final_assets/Secondary_btn/pressed.png);color: rgb(0, 170, 255);font: 16pt "Roboto [GOOG]";""")
        else:
            pass
    def tst(self):
        
        self.sp2 = QMdiSubWindow()
        self.sp2.setWidget(self.p11)
        self.sp2.setWindowTitle("testing")
        self.mdiArea.addSubWindow(self.sp2)
##        self.subwindow.setFixedSize(400,600)
        self.sp2.setWindowFlags(Qt.FramelessWindowHint)
##        self.sp4.resize(self.p4.size())
        self.mdiArea.tileSubWindows()
        self.sp2.show()
    def cutting(self):
        
        self.sp4 = QMdiSubWindow()
        self.sp4.setWidget(self.p2)
        self.sp4.setWindowTitle("Cutting chart")
        self.mdiArea.addSubWindow(self.sp4)
##        self.subwindow.setFixedSize(400,600)
        self.sp4.setWindowFlags(Qt.FramelessWindowHint)
##        self.sp4.resize(self.p4.size())
        self.mdiArea.tileSubWindows()
        self.sp4.show()
        
    def grid(self):
        
        self.sp3 = QMdiSubWindow()
        self.sp3.setWidget(self.p3)
        self.sp3.setWindowTitle("grid veiw")
        self.mdiArea.addSubWindow(self.sp3)
        
        self.sp3.show()
        self.sp3.setWindowFlags(Qt.FramelessWindowHint)

    def Diagnostics(self):

        self.sp1 = QMdiSubWindow()
        self.sp1.setWidget(self.p1)
        self.sp1.setWindowTitle("daignostics")
        self.mdiArea.addSubWindow(self.sp1)
        self.sp1.show()
        self.sp1.setWindowFlags(Qt.FramelessWindowHint)

        
    def btnstate(self):
        global btnstate_flag
        if (btnstate_flag==0):
            self.sp3.hide()
            self.sp4.hide()
            self.sp1.show()
            self.pushButton.setText("Board Layout" )
            btnstate_flag=1
            self.mdiArea.tileSubWindows()
        elif (btnstate_flag==1):
            self.sp1.hide()
            self.sp3.show()
            self.sp4.show()
            self.pushButton.setText("Diagnostics")
            self.mdiArea.tileSubWindows()
            btnstate_flag=0
        
           
    def activeMdiChild(self):
        activeSubWindow = self.mdiArea.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()
        return None
    def mousePressEvent(self,event):
        self.mdiArea.tileSubWindows()
    def closeIt(self):
        sub=self.activeMdiChild()
        sub.showMinimized()
        self.mdiArea.tileSubWindows()
##=====================================================================================================================================


    def start_process(self,event):
        UploadProdLog_Data(GV.Location_No,GV.Part_Name,'Engine Start','Testing Started')
##        self.Enter_btn.setEnabled(False)
        self.label_21.setEnabled(False)
        self.Enter_btn.setStyleSheet("""border-image: url(:/images/final_assets/Secondary_btn/pressed.png);color: rgb(0, 170, 255);font: 16pt "Roboto [GOOG]";""")
        GV.module_no=8
        GV.Estate=0
        print("check--------------",GV.scan_complete,GV.Fo_test_Flag)
        if (GV.Fo_test_Flag==0):##sample to production set
            # print("GV.FoQty",GV.FoQty,type(GV.FoQty))
            if((int(GV.FoQty) <=0) and (GV.AssetCodeScan=='1')):
                self.Enter_btn.setEnabled(False)
                self.pushButton_5.setEnabled(False)
                self.msg_line.setText("Set FO Quantity...")
                self.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: red""")
                

            else:    
                if(GV.AutoPartLoad=='0' and GV.AssetCodeScan=='0'):
                    
                    GV.Estate=3

                else:
                    if(GV.AutoPartLoad=='1'):
                        self.barcode_scan_line.setFocus()
                        if(GV.scan_complete==1):
                            GV.scan_complete=0
                            print("Test Engine Start...")
                            GV.Estate=2
                                
                        else:
                            
                            self.new_window =partload_main.Ui_Dialog()
                            self.new_window.show()
                            self.barcode_scan_line.setFocus()
                            self.barcode_scan_line.setEnabled(True)
                            
                        
                    else:            
                        self.barcode_scan_line.setEnabled(True)
                        self.barcode_scan_line.setFocus()
                        GV.Estate=1
        else:
            GV.Fo_test_Flag=0
            GV.Estate=5
        self.Enter_btn.setStyleSheet("""border-image: url(:/images/final_assets/Secondary_btn/pressed.png);color: rgb(0, 170, 255);font: 16pt "Roboto [GOOG]";""")        

        

##=========================================================================================================================================
    def Previous(self):
        GV.ClickOn_Next=0

    def Next(self):
        GV.ClickOn_Next=1

    def read_val_frm_db(self):
        print("GV.Pass_Count",GV.Pass_Count,GV.Fail_Count,GV.Part_Name,GV.Location_No)
        try:
            self.pass_cnt_line.setText(str(GV.Pass_Count))
            self.fail_cnt_line.setText(str(GV.Fail_Count))
            self.fo_qty.setText(str(GV.FoQty))
            self.label_19.setText(str(GV.Part_Name))
            self.label_20.setText(str(GV.Location_No))
            

        except TypeError:
            GV.Pass_Count=0
            GV.Fail_Count=0

    
"""   draw line on image and return it as pixmap   """
def draw_line(img,x1,y1,x2,y2,colo1,colo2,err,radius,sc):
    '''  read images  '''
#    img1 = cv2.imread(image1_path)
#    img2 = cv2.imread(image2_path)
#        print(img1.shape,img2.shape)
    '''  attach two images side-by-side  '''
#    img = np.concatenate((img1, img2), axis=1)
#        print(img.shape)
    ''' calculate line points on image  '''
    if(img.shape[1]==600):
        x2 = x2+300
    
    offset1 = radius[0]
    offset2 = radius[1]
    clone = img.copy()
    colo = colo1
    if sc[0] ==0:
        axes1 = (radius[0],radius[0])
        axes2 = (radius[1],radius[1])
        if not(colo[0] == colo[1]):
            angle=0;
            startAngle=0;
            endAngle=180;
            center=(x1,y1)
            
            cv2.ellipse(clone, center, axes1, angle, startAngle, endAngle, colo[0],-1)
            cv2.ellipse(clone, center, axes1, angle, startAngle+180, endAngle+180, colo[1],-1)
        else:
            angle=0;
            startAngle=0;
            endAngle=360;
            center=(x1,y1)
##            print("elipse", center, axes1, angle, startAngle, endAngle, colo[0],-1)
            cv2.ellipse(clone, center, axes1, angle, startAngle, endAngle, colo[0],-1)
    else:
        if not(colo[0] == colo[1]):
            start_pt = (x1-offset1,y1-offset1)
            end_pt = (x1+offset1,y1)
            cv2.rectangle(clone, start_pt,end_pt, colo[0], -1)
            
            start_pt = (x1-offset1,y1)
            end_pt = (x1+offset1,y1+offset1)
            cv2.rectangle(clone, start_pt,end_pt, colo[1], -1)
            
        else:
            start_pt = (x1-offset1,y1-offset1)
            end_pt = (x1+offset1,y1+offset1)
            cv2.rectangle(clone, start_pt,end_pt, colo[0], -1)

    
    colo = colo2
    if sc[1] ==0:
        axes1 = (radius[0],radius[0])
        axes2 = (radius[1],radius[1])
        if not(colo[0] == colo[1]):
            angle=0;
            startAngle=0;
            endAngle=180;
            center=(x2,y2)
            cv2.ellipse(clone, center, axes2, angle, startAngle, endAngle, colo[0],-1)
            cv2.ellipse(clone, center, axes2, angle, startAngle+180, endAngle+180, colo[1],-1)
        else:
            angle=0;
            startAngle=0;
            endAngle=360;
            center=(x2,y2)
            cv2.ellipse(clone, center, axes2, angle, startAngle, endAngle, colo[0],-1)
    else:
        if not(colo[0] == colo[1]):
            start_pt = (x2-offset2,y2-offset2)
            end_pt = (x2+offset2,y2)
            cv2.rectangle(clone, start_pt,end_pt, colo[0], -1)
            
            start_pt = (x2-offset2,y2)
            end_pt = (x2+offset2,y2+offset2)
            cv2.rectangle(clone, start_pt,end_pt, colo[1], -1)
        else:
            start_pt = (x2-offset2,y2-offset2)
            end_pt = (x2+offset2,y2+offset2)
            cv2.rectangle(clone, start_pt,end_pt, colo[0], -1)
    
    axes1 = (radius[0]+6,radius[0]+6)
    axes2 = (radius[1]+6,radius[1]+6)
    if err==1:
        center=(x1,y1)
        cv2.ellipse(clone, center, axes1, 0, 0, 360, (0,0,255),4)
        center=(x2,y2)
        cv2.ellipse(clone, center, axes2, 0, 0, 360, (0,0,255),4)
    else:
        center=(x1,y1)
        cv2.ellipse(clone, center, axes1, 0, 0, 360, (0,255,0),4)
        center=(x2,y2)
        cv2.ellipse(clone, center, axes2, 0, 0, 360, (0,255,0),4)
    img = cv2.cvtColor(clone, cv2.COLOR_BGR2RGB)
#        cv2.imwrite("text.png",img)
    '''  convert cv2 image to qt image  '''

    cvt2qt = QtGui.QImage(img, img.shape[1],img.shape[0], img.shape[1] * 3,
                          QtGui.QImage.Format_RGB888)


    '''  convert qt image to qt pixmap  '''
    pixmap = QPixmap.fromImage(cvt2qt);
    return (pixmap)

    """   generate random test data   """
def strtuple_inttuple(a):
    b=a.strip('(')
    b=b.strip(')')
    b=b.split(',')
    c=[]
    for i in b:
        c.append(int(i))
    return(tuple(c))
##    @pyqtSlot()

def rand_data(p4):
    ConnName1 = GV.connector1_name
    ConnName2 = GV.connector2_name
    pt1 = GV.cavity1-1
    pt2 = GV.cavity2-1
    try:
        for i in range (len(GV.library_mapping)):
            if ConnName1 in GV.library_mapping[i]:
                LibName1=GV.library_mapping[i][1]
                GrNo1=GV.library_mapping[i][0]
            if ConnName2 in GV.library_mapping[i]:
                LibName2=GV.library_mapping[i][1]
                GrNo2=GV.library_mapping[i][0]
    except:
        self.mess="Connector Name is Not Present in Library"
        self.clickMethod()

    try:
        data = get_Cavity_Map(LibName1)
        data2 = get_Cavity_Map(LibName2)
    except:
        self.mess="Library Not Present"
        self.clickMethod()
    x1 = data[pt1][1]
    y1 = data[pt1][2]
    radius1 = data[pt1][4]
    sc1 = data[pt1][3]
    
##    print("cavity data",data2,pt2)
    x2 = data2[pt2][1]
    y2 = data2[pt2][2]
    radius2 = data2[pt2][4]
    sc2 = data2[pt2][3]
##    print(sc2)
    binimg = get_conn_Image(LibName1)[0][0]
    nparr = np.frombuffer(binimg, np.uint8)
    img1 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if(GV.wcolor1a==' '):
        GV.wcolor1a = 'WHT'
    if(GV.wcolor1b==' '):
        GV.wcolor1b = 'WHT'
    if(GV.wcolor2a==' '):
        GV.wcolor2a = 'WHT'
    if(GV.wcolor2b==' '):
        GV.wcolor2b = 'WHT'

    try:
        colo1 = [strtuple_inttuple(Downloadwirecolor1(GV.wcolor1a)[0][0]),
                 strtuple_inttuple(Downloadwirecolor1(GV.wcolor1b)[0][0])]
        colo2 = [strtuple_inttuple(Downloadwirecolor1(GV.wcolor2a)[0][0]),
                 strtuple_inttuple(Downloadwirecolor1(GV.wcolor2b)[0][0])]
    
       
        colo1[0]=tuple([colo1[0][2],colo1[0][1],colo1[0][0]])
        colo1[1]=tuple([colo1[1][2],colo1[1][1],colo1[1][0]])
        colo2[0]=tuple([colo2[0][2],colo2[0][1],colo2[0][0]])
        colo2[1]=tuple([colo2[1][2],colo2[1][1],colo2[1][0]])
    ##    print("colo1",colo1,"   colo2",colo2)
    
        if(ConnName1 ==ConnName2 ):
            img = img1
            pixmap=draw_line(img,x1,y1,x2,y2,colo1,colo2,1,[radius1,radius2],[sc1,sc2])
            p4.label.setPixmap(pixmap);
            p4.label.show()
        else:
            binimg = get_conn_Image(LibName2)[0][0]
            nparr = np.frombuffer(binimg, np.uint8)
            img2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            img = np.concatenate((img1, img2), axis=1)
            pixmap=draw_line(img,x1,y1,x2,y2,colo1,colo2,1,[radius1,radius2],[sc1,sc2])
            p4.label.setPixmap(pixmap);
            p4.label.setScaledContents(True)
            p4.label.show()
    except:
        print("Color Not Present In library")
def clear_image(p4):

    pixmap = QPixmap('/home/pi/Desktop/.HA_Editor/UI_files/final_assets/mdi_images/roc.png')
    p4.label.setPixmap(pixmap)
    p4.label.setScaledContents(True)
    p4.label.show()
def put_image(p4):

    pixmap = QPixmap('/home/pi/Desktop/.HA_Editor/UI_files/final_assets/mdi_images/put_cable.png')
    p4.label.setPixmap(pixmap)
    p4.label.setScaledContents(True)
    p4.label.show()
##    p4.label.hide()

def pass_image(p4):

    pixmap = QPixmap('/home/pi/Desktop/.HA_Editor/UI_files/final_assets/mdi_images/pass_cable.png')
    p4.label.setPixmap(pixmap)
    p4.label.setScaledContents(True)
    p4.label.show()
    
def wrong_image(p4):
    pixmap = QPixmap('/home/pi/Desktop/.HA_Editor/UI_files/final_assets/mdi_images/wrong_insertion.png')
    p4.label.setPixmap(pixmap)
    p4.label.setScaledContents(True)
    p4.label.show()
def release_image(p4):
    pixmap = QPixmap('/home/pi/Desktop/.HA_Editor/UI_files/final_assets/mdi_images/Release.jpeg')
    p4.label.setPixmap(pixmap)
    p4.label.setScaledContents(True)
    p4.label.show()

def barcode_image(p4):
##    # set qmovie as label
##    p4.movie = QMovie("/home/pi/Desktop/HA_Editor/UI_files/final_assets/mdi_images/barcode.gif")
##    p4.label.setMovie(p4.movie)
##    p4.movie.start()
    pixmap = QPixmap('/home/pi/Desktop/.HA_Editor/UI_files/final_assets/mdi_images/barcodeScan.png')
    p4.label.setPixmap(pixmap)
    p4.label.setScaledContents(True)
    p4.label.show()

##============================================================================================================================================
           
##def main():
##    app = QtGui.QApplication(sys.argv)
##    app.setApplicationName('mdiArea')
##    f = mdiArea_window()
##    timer = QTimer()
##    f.connect(timer,SIGNAL("timeout()"),f,SLOT("rand_data()"))
##    timer.start(400)
##    
##    f.show()
##    app.exec_()
##    sys.exit(app.exec_())
##
##if __name__ == '__main__':
##    main()
