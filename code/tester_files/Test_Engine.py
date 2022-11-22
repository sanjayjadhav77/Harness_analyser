import global_test_var as GV
from CAN_Bus import *
from HDM import *
from printer import *
from Actuation import *
from Peripheral_Processes import*
from Component_test import*
from global_files import*
import time
from datetime import datetime
from SSLT import *


'''-----------------------------Test Engine----------------------------------''' 

def Engine_states(Estate):
    print("Estate",Estate)
    ops = {
        0: Default_State,
        1: Asset_Scanning,
        2: Sample_Production,
        3: Leak_Test,
        4: HarnessAvailability,
        5: FirstStage_Test,
        6: MultiStage_Test,
        7: Component_Test,
        8: Label_Printing,
        9: Barcode1_Matching,
        10: Barcode2_Matching,
        11: Report_Generation_state,
        12: Actuations,
        13: RemoveHarness,
        14: hold_time,
        15: Blank_State,
        16: clear_scan,
        17: Supervisor_state

             
    }
    chosen_operation_function = ops.get(Estate, invalid_key)
    return chosen_operation_function(Estate)
    print("sub Option selection")
def Supervisor_state(Estate):
    GV.data_delivered=17
def clear_scan(Estate):
    GV.data_delivered=16
def Blank_State(Estate):
    #self.p4.barcode_scan_line.clear()

    GV.data_delivered=5
def invalid_key(Estate):
    raise Exception("Invalid operation")
def Default_State(Estate):
    GV.data_delivered=0
    print("Default_State")
def hold_time(Estate):
    # print("GV.data_delivered",GV.data_delivered)
    #self.p4.barcode_scan_line.clear()
    GV.data_delivered=15
    
  
def Asset_Scanning(Estate):
    if(GV.AssetCodeScan=='1'):
        if(GV.Sample==1):
            GV.data_delivered=1
        else:
            GV.Estate=2
    else:
        GV.Estate=3
    
def Sample_Production(Estate):

    if(GV.Sample==1):
        GV.data_delivered=2
    else:
        GV.Estate=3
        
def Leak_Test(Estate):    
    if(GV.LeakageChannel=='1'):
        Leakage_Test()
    else:
        x=len(GV.switch)
        GV.Stop_Leakage=0
        while(x!=GV.Stop_Leakage and GV.Abort_flag==0):
            Connector_Availability()
            if(GV.switch_status[GV.Stop_Leakage][1]==1):
                print("Connector " +str(GV.switch_status[GV.Stop_Leakage][0])+ " present")
                GV.Display_Message=("Connector "+ str(GV.switch_status[GV.Stop_Leakage][0])+" present")
                # GV.Display_Message=("Leakage Test " +str(GV.switch_status[GV.Stop_Leakage][0])+ " Start")
                GV.data_delivered=13
                GV.Stop_Leakage+=1
            else:
               GV.Display_Message=("Connector "+ str(GV.switch_status[GV.Stop_Leakage][0])+" Absent")
               print("Connector "+ str(GV.switch_status[GV.Stop_Leakage][0])+" Absent")
               GV.data_delivered=13    
            
        GV.Estate=4

    
def Component_Test(Estate):
    if(GV.Sample==0):
        GV.data_delivered=7
        print("Component_Test ")
    else:
        GV.Estate=12
def Label_Printing(Estate):
    if(GV.LabelPrint==1):
        lbl_printing(GV.Local_Label_Data)
        GV.Estate=9
    else:
        GV.Estate=9
def Barcode1_Matching(Estate):
    if(GV.Barcode_Match==1):

        GV.data_delivered=9
        
    else:
        print("barcode1 not present")
        GV.Estate=10
def Barcode2_Matching(Estate):
    if(GV.Barcode_Match==1):
        if(GV.No_Of_Barcodes==2):
            GV.data_delivered=14
        
        else:
            print("barcode2 not present")
            GV.Estate=11
    else:
        GV.Estate=11
def Report_Generation_state(Estate):
    if(GV.Report=='1'):
        GV.data_delivered=10
    else:
        GV.Estate=12
def Actuations(Estate):
    print("Actuations")    
    
    GV.Visual_Engine_Start=6
    GV.Display_Message="Release on"
    GV.data_delivered=13
    if(GV.Q_Mark_Time!=0):
        Qmarkset()
        time.sleep(GV.Q_Mark_Time)
        Qmark_reset()
    if(GV.Release_Time!=0):
        Release_on()
        passled_on()
        time.sleep(GV.Release_Time)
        passled_off()
        Release_off()
    
    GV.Estate=13
def HarnessAvailability(Estate):
    print("check harness available if auto mode")
    GV.HA=1
    if(GV.Auto_Mode==1):
        HA_result=test_Harness_Availability(Estate)
        print("HA_result",HA_result)
        if(HA_result==1):
            GV.Estate=5
        else:
            
            GV.Display_Message="Harness not Available"
            GV.data_delivered=13
            GV.message_color=2
            GV.Estate=4
            
    else:
        GV.Estate=5
        
        
    
def FirstStage_Test(Estate):
    GV.Multi_stage=1
    GV.Estate=6
    GV.checkboard_to_engine=0
    GV.Display_Message=("Processing...............")
    GV.message_color=1
       
    
def MultiStage_Test(Estate):
    print("Actual Engine run1....")
    now=time.time()
    GV.circuits=[]
    DownloadHarnessData(GV.Location_No,GV.Multi_stage)
    GV.circuits_temp=GV.circuits
    if(GV.checkboard_to_engine==0):
        GV.x=1
        GV.y=2
        GV.IO_error_code=1
        GV.Intruption_flag=1
        GV.time_gap=0
        GV.privious_x=0
        GV.privious_y=0
        GV.Privious_intpoint1=0
        GV.Privious_intpoint2=0
        GV.Previous_Time=time.time()
        GV.Current_Time=time.time()
        now=time.time()
        while(GV.Intruption_flag):
            Engine_start()
        current=time.time()
        print("GV.X=",GV.x,"GV.y=",GV.y)
        print("time",current-now)
    else:    
        now=time.time()
        while(GV.Intruption_flag):
            Engine_start()
        current=time.time()
        print("GV.X=",GV.x,"GV.y=",GV.y)
        print("time",current-now)

    if(GV.Check_bypass==0):
        if(GV.Abort_flag==0):
            if(GV.Cutter_Action==0):
                if(GV.Num_Stages==GV.Multi_stage):
                    GV.Multi_stage=1
                    GV.Estate=7
                    GV.Intruption_flag=1
                else:
                    GV.Multi_stage+=1
                    GV.Intruption_flag=1
                    GV.Estate=6
            else:
                if(GV.Sample_Production==0):
                    GV.Cutter_Action=0
                    GV.Estate=15
                else:
                    if(GV.IO_error_code==8):
                        GV.Cutter_Action=0
                        GV.Estate=2
                        GV.Visual_Engine_Start=2
                        # GV.data_delivered=2
                    else:
                        GV.data_delivered=2
                        GV.module_no=0
        else:
            if(GV.Sample==0):
                cutter_set()
                failled_on()
                time.sleep(GV.Fail_Time)
                failled_off()
                cutter_reset()
            GV.Abort_flag=0
            GV.Estate=0
    else:
        GV.Check_bypass=0
def RemoveHarness(Estate):
    #print("check harness remove if auto mode")
    GV.data_delivered=12

def UIEngine_Display(data_delivered,self):
##    print("data_delivered",data_delivered)
    ops = {
        0: UI_Default_State,
        1: UI_Asset_Scanning,
        2: UI_Sample_Production,
        3: UI_Leak_Test,
        4: UI_HarnessAvailability,
        5: UI_FirstStage_Test,
        6: UI_SecondStage_Test,
        7: UI_Component_Test,
        8: UI_Label_Printing,
        9: UI_Barcode_Matching,
        10: UI_Report_Generation,
        11: UI_Actuations,
        12: UI_RemoveHarness,
        13: UI_Operational_messages,
        14: UI_barcode2_matching,
        15: UI_MsgHold,
        16: UI_Clearscan,
        17: UI_Supervisor_state
   
        
           
    }
    chosen_operation_function = ops.get(data_delivered, invalid_key)
    return chosen_operation_function(data_delivered,self)
    print("sub Option selection")



def UI_Operational_messages(x,self):
    self.p4.msg_line.setText(GV.Display_Message)
    self.p4.label_21.setEnabled(True)
    if(GV.message_color==2):
        self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: red""")
    elif(GV.message_color==3):
        self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: green""")
    else:
        self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: blue""")
    
def UI_Default_State(x,self):
    GV.Visual_Engine_Start=3
    GV.Abort_flag=0
    if(GV.AssetCodeScan=='1'):
        if(GV.FoQty=='0'):
            self.msg_line.setText("Set FO Quantity...")
            self.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: red""")
    else:        
        self.p4.msg_line.setText("Put Cable Points-"+(str(GV.point_count)))
        self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: blue""")


def UI_Asset_Scanning(x,self):
    self.p4.barcode_scan_line.setFocus()
    Fixtures_scaning(self)
    
        
        
def UI_Sample_Production(x,self):
    sample_init(self)   ### HDM.PY
##    if(GV.Abort_flag==0):
##        GV.Estate=13
##    else:
##        
##        GV.Estate=0
def UI_Leak_Test(x,self):
    print("leak test")
    GV.Estate=4
def UI_HarnessAvailability(x,self):
    time.sleep(0.6)
def UI_FirstStage_Test(x,self):
    GV.Cutter_Action=0
    self.p4.label_21.setEnabled(True)
    print("GV.Fail_Coun",GV.Fail_Count)
    GV.Visual_Engine_Start=3
    self.p4.msg_line.setText("Harness Fail...")
    self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: red""")
    time.sleep(0.6)
    GV.Intruption_flag=0
    if(GV.AssetCodeScan=='1'):
        if(global_var.p_s==0):
            global_var.p_s=1
            self.p4.production_sample()
            GV.Fo_test_Flag=0
        else:
            global_var.p_s=0
            self.p4.production_sample()
            GV.Fo_test_Flag=1       ###fo flag 
    GV.tested_circuits=[] 
    GV.x=1
    GV.y=1
    
    GV.module_no=0
    GV.Visual_Engine_Start=3
    GV.data_delivered=0
    self.p4.msg_line.clear()
    GV.Multi_stage=1
    GV.time_gap=0
    GV.privious_x=0
    GV.privious_y=0
    GV.Privious_intpoint1=0
    GV.Privious_intpoint2=0
    GV.IO_error_code=1
    
    if(GV.Fail_Count>=999999):
        GV.Fail_Count=0
        GV.Fail_Count=GV.Fail_Count+1
        GV.Display_Message=''
    else:
        GV.Fail_Count=GV.Fail_Count+1
        UploadProdLog_Data(GV.Location_No,GV.Part_Name,'Timeout',str(GV.Display_Message))
        UploadProdLog_Data(GV.Location_No,GV.Part_Name,' Abort Fail',str(GV.Fail_Count))
        GV.Display_Message=''
        
    self.p4.fail_cnt_line.setText(str(GV.Fail_Count))
    self.p4.msg_line.setText("Put Cable")
    self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: blue""")
    x=[(GV.Pass_Count,GV.Fail_Count,GV.Stage1_status,GV.Stage1_Points_No,GV.Stage2_status,GV.Stage2_Points_No)]
    UploadCable_Info(GV.Location_No,x)
    
    GV.data_delivered=0
    GV.Estate=0

def UI_SecondStage_Test(x,self):
    pass
def UI_Component_Test(x,self):
    # print("GV.Pass_Count",type(GV.Pass_Count))
    if(GV.AssetCodeScan=='1'):
        GV.FoQty=int(GV.FoQty)-1
        UploadFO_QTY(GV.Location_No,GV.FoQty)
    if(GV.Pass_Count>=999999):
        GV.Pass_Count=0
    else:
        GV.Pass_Count=GV.Pass_Count+1
    # print("GV.Pass_Count",GV.Pass_Count)
    
    x=[(GV.Pass_Count,GV.Fail_Count,GV.Stage1_status,GV.Stage1_Points_No,GV.Stage2_status,GV.Stage2_Points_No)]
    UploadCable_Info(GV.Location_No,x)
    UploadProdLog_Data(GV.Location_No,GV.Part_Name,'Harness Pass',GV.Pass_Count)
    self.p4.pass_cnt_line.setText(str(GV.Pass_Count))
    self.p4.fail_cnt_line.setText(str(GV.Fail_Count))
    self.p4.fo_qty.setText(str(GV.FoQty))
    time.sleep(1)
    GV.Estate=8
    GV.data_delivered=4
def UI_Label_Printing(x,self):
    pass
def UI_Barcode_Matching(x,self):
    self.p4.pushButton_5.setEnabled(False)
    self.p4.p1.comboBox.setEnabled(False)
    self.p4.p1.frame_4.setEnabled(False)
    self.p4.p1.label_19.setEnabled(False)
    self.p4.p1.frame.setEnabled(False)
    self.p4.p1.label_4.setEnabled(False)
    self.p4.p1.label_5.setEnabled(False)
    self.p4.p1.frame_5.setEnabled(False)
    self.p4.p1.label_20.setEnabled(False)
    self.p4.p1.label_24.setEnabled(False)
    self.p4.p1.frame_6.setEnabled(False)
    self.p4.p1.label_21.setEnabled(False)
    self.p4.p1.label_25.setEnabled(False)    
    self.p4.p1.label_50.setEnabled(False)
    self.p4.barcode_scan_line.setEnabled(True)
    self.p4.barcode_scan_line.setFocus()
    self.p4.msg_line.setText("Scan barcode 1")
    self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: blue""")
    barcode1_scaning(self)
 
def UI_barcode2_matching(x,self):
    self.p4.pushButton_5.setEnabled(False)
  
    self.p4.barcode_scan_line.setFocus()
    self.p4.msg_line.setText("Scan barcode 2")
    self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: blue""")
    barcode2_scaning(self)
     
def UI_Report_Generation(x,self):
    
    Report_Generation(self)
        
def UI_Actuations(x,self):
    pass
def UI_RemoveHarness(x,self):
    self.p4.label_21.setEnabled(True)
    self.p4.pushButton_5.setEnabled(True)
    self.p4.p1.comboBox.setEnabled(True)
    self.p4.p1.frame_4.setEnabled(True)
    self.p4.p1.label_19.setEnabled(True)
    self.p4.p1.frame.setEnabled(True)
    self.p4.p1.label_4.setEnabled(True)
    self.p4.p1.label_5.setEnabled(True)
    self.p4.p1.frame_5.setEnabled(True)
    self.p4.p1.label_20.setEnabled(True)
    self.p4.p1.label_24.setEnabled(True)
    self.p4.p1.frame_6.setEnabled(True)
    self.p4.p1.label_21.setEnabled(True)
    self.p4.p1.label_25.setEnabled(True)    
    self.p4.p1.label_50.setEnabled(True)
    if(GV.Auto_Mode==1):
        HA_result=test_Harness_Availability(GV.Estate)
##        print("HA_result",HA_result)
        if(HA_result==1):
            print("Remove harness")
            self.p4.msg_line.setText("Remove Harness")
            self.p4.Enter_btn.setEnabled(True)
            
            if(GV.Abort_flag==0):
                GV.Estate=13
            else:
                GV.Abort_Event_flag=1
                GV.Estate=0
                
        else:
            print("HAreness release")
            GV.Visual_Engine_Start=3
            self.p4.msg_line.setText("Put Cable")
            self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: blue""")
            GV.data_delivered=13
            GV.Estate=4
            #GV.Option=0
            
    else:
        GV.Visual_Engine_Start=3
        self.p4.msg_line.setText("Put Cable")
        self.p4.msg_line.setStyleSheet("""border-radius: 1px;font: 20pt "Roboto [GOOG]";color: blue""")

        GV.Estate=0

def UI_MsgHold(x,self):
    print("Hold time start")
    GV.Hold+=1
    if(GV.Hold==5):
        print("Hold time end")
        GV.Hold=0
        GV.Estate=GV.Holdstate
        # GV.data_delivered=9
def UI_Clearscan(x,self):
    print("In clear scan")

def UI_Supervisor_state(x,self):
    self.p8.key.setFocus()
    GV.Estate=16

##if __name__ == '__main__':
##    Engine_states(5)
    
