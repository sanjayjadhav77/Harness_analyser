import global_test_var as GV
from CAN_Bus import *
from HDM import *
from printer import *
from Actuation import *
from Test_Engine import *
from Peripheral_Processes import*
from Component_test import*
from global_files import*
import time
from datetime import datetime
#----------------------------------Thread-------------------------------------------------------------------------------------------#
def tester_message_generation():
    
    while True:
        # print("GV.module_no",GV.module_no)
        Module_list(GV.module_no)
        time.sleep(0.01)
        GV.test_count+=1
        

    
'''-------------------------------------UI Engine----------------------------'''
def Module_list(module_no):
    ops = {
        0: boardtest_Screen,
        1: checkboard_status,
        2: HA_checkboard_status,
        3: Harness_Availability,
        4: Learn_Harness,
        5: Switch_Detection,
        6: HA_Switch_Detection,
        7: HA_Harness_Availability,
        8: Test_Flow
    }
    chosen_operation_function = ops.get(module_no, invalid_Ecode)
    return chosen_operation_function(module_no)
def boardtest_Screen(x):
    pass
##    print("Default_Screen")
def Test_Flow(x):
    Engine_states(GV.Estate)
def invalid_Ecode(x):
    raise Exception("Invalid operation")


'''-------------------------Board test menu------------------------------------------------'''
def GUI_Display(data_Available,self):
##    print("data_Available...",data_Available)
    Custom_Message(data_Available)
    
    ops = {
        0: UI_boardtest,
        1: UI_Check_board,
        2: UI_Show_points,
        3: UI_Self_test,
        4: UI_Learn_Hrn,
        5: UI_Switch_Detection,
        6: UI_Group_Data_Diagno,
        7: UI_Global_Group_Data,
        8: UI_Comp_Testing,
        9: UI_HA_checkbord,
        10: UI_HA_Switch_Detection,
        11: UI_HA_Show_points,
        12: UI_HA_Group_Data_Diagno,
        13: UI_HA_Self_test
        
    }
    chosen_operation_function = ops.get(data_Available, invalid_Ecode)
    return chosen_operation_function(data_Available,self)
    
def UI_HA_checkbord(x,self):
    a=str(GV.short_pin)
    a=a.strip('[')
    a=a.strip(']')
    a=a.split(",")
    self.p4.p1.tableWidget.clear()
    for i in range (len(a)):
        self.p4.p1.tableWidget.setItem(0,i, QTableWidgetItem(str(a[i])))
def UI_Comp_Testing(x,self):
    print("GV.comp_display",GV.comp_display)
    for i in range(len(GV.comp_display)):
        grp2_data=GV.comp_display[i]
        for j in range(len(grp2_data)):
            grp_pts=grp2_data[j]
            self.p18.tableWidget_2.setItem(i,j, QTableWidgetItem(str(grp_pts)))
        
    
def UI_boardtest(x,self):
    pass
def UI_Global_Group_Data(x,self):
    for i in range(len(GV.Global_Group_data_display)):
        grp2_data=GV.Global_Group_data_display[i]
        for j in range(len(grp2_data)):
            grp_pts=grp2_data[j]
            self.p19.grp2_table.setItem(i,j, QTableWidgetItem(str(grp_pts)))

def UI_Group_Data_Diagno(x,self):

    for i in range(len(GV.Local_Group_data_display)):
        self.p21.tableWidget.setItem(i,0, QTableWidgetItem(str(GV.LocalGrpNo[i])))
        shw_grp=GV.Local_Group_data_display[i]
        for j in range(len(shw_grp)):
            display_points=shw_grp[j]
            self.p21.tableWidget.setItem(i,j+1, QTableWidgetItem(str(display_points)))
def UI_HA_Group_Data_Diagno(x,self):

    for i in range(len(GV.Local_Group_data_display)):
        self.p4.p1.tableWidget.setItem(i,0, QTableWidgetItem(str(GV.LocalGrpNo[i])))
        shw_grp=GV.Local_Group_data_display[i]
        for j in range(len(shw_grp)):
            display_points=shw_grp[j]
            self.p4.p1.tableWidget.setItem(i,j+1, QTableWidgetItem(str(display_points)))

def UI_HA_Switch_Detection(x,self):
    try:
        for i in range (len(GV.Switch_display)):
            read=(GV.Switch_display[i])
            for j in range (len(read)):
                display_points=read[j]
                self.p4.p1.tableWidget.setItem(i,j, QTableWidgetItem(str(display_points)))
        
    except  (IOError,ValueError,TypeError):
        print("error in reading  connector status please repeat procedure...")
        self.p21.tableWidget.setItem(0,0, QTableWidgetItem('Error...'))
def UI_Switch_Detection(x,self): 
    try:
        for i in range (len(GV.Switch_display)):
            read=(GV.Switch_display[i])
            for j in range (len(read)):
                display_points=read[j]
                self.p21.tableWidget.setItem(i,j, QTableWidgetItem(str(display_points)))
        
    except  (IOError,ValueError,TypeError):
        print("error in reading  connector status please repeat procedure...")
        self.p21.tableWidget.setItem(0,0, QTableWidgetItem('Error...'))
def UI_Check_board(x,self):
    a=str(GV.short_pin)
    a=a.strip('[')
    a=a.strip(']')
    a=a.split(",")
    self.p21.tableWidget.clear()
    for i in range (len(a)):
        self.p21.tableWidget.setItem(0,i, QTableWidgetItem(str(a[i])))
    
def UI_HA_Show_points(x,self):
    for i in range(len(GV.ckt_net)):
        read=(GV.ckt_net[i])
        for j in range(len(read)):
            display_points=read[j]
            self.p4.p1.tableWidget.setItem(i,j, QTableWidgetItem(str(display_points)))

def UI_Show_points(x,self):
    for i in range(len(GV.ckt_net)):
        read=(GV.ckt_net[i])
        for j in range(len(read)):
            display_points=read[j]
            self.p21.tableWidget.setItem(i,j, QTableWidgetItem(str(display_points)))

def UI_Self_test(x,self):
    if(len(GV.selftest_pin)>0):
        for i in range (len(GV.selftest_pin)):
            self.p21.tableWidget.setItem(0,i, QTableWidgetItem(str(GV.selftest_pin[i])))
    else:
        self.p21.tableWidget.setItem(0,0, QTableWidgetItem("Board ok"))
        
def UI_HA_Self_test(x,self):
    if(len(GV.selftest_pin)>0):
        for i in range (len(GV.selftest_pin)):
            self.p4.p1.tableWidget.setItem(0,i, QTableWidgetItem(str(GV.selftest_pin[i])))
    else:
        self.p4.p1.tableWidget.setItem(0,0, QTableWidgetItem("Board ok"))

def UI_Learn_Hrn(x,self):
    print("GV.ckt_net....",GV.ckt_net)
    # self.p17.comboBox_2.addItem(str(GV.stage))
    # self.p17.comboBox_2.setItemText(str(GV.stage))
    if(len(GV.ckt_net)>0):
        no_of_points=map(len,GV.ckt_net)
        total_point=sum(no_of_points)
        total_point=str(total_point)
        self.p17.hrn_table.setItem(0,0, QTableWidgetItem(total_point))
                
        for i in range(len(GV.ckt_net)):
            read=(GV.ckt_net[i])
                #print(read)
            for j in range(len(read)):
                display_points=read[j]
                self.p17.hrn_table.setItem(i+1,j, QTableWidgetItem(str(display_points)))
        # self.p17.comboBox_2.addItem(str(GV.stage))
                        
    else:
        self.p17.hrn_table.setItem(0,0, QTableWidgetItem('Fail'))
    
    

def Custom_Message(data_Available):
##    print("cheack....data_Available...",data_Available)
    ops = {
        0: CM_boardtest,
        1: CM_Check_board,
        2: CM_Show_points,
        3: CM_Self_test,
        4: CM_Learn_Hrn,
        5: CM_Switch_Detection,
        6: CM_Group_Data_Diagno,
        7: CM_Global_Group_Data,
        8: CM_Comp_Testing,
        9: CM_HA_ccheckboard,
        10: CM_HA_Switch_Detection,
        11: CM_HA_Show_points,
        12: CM_HA_Group_Data_Diagno,
        13: CM_HA_Self_test
    }
    chosen_operation_function = ops.get(data_Available, invalid_Ecode)
    return chosen_operation_function(data_Available)
def CM_Comp_Testing(x):
    GV.comp_display=[]
##    print("GV.component_test.......",GV.component_test)
    for i in range(len(GV.component_test)):
        r=list(GV.component_test[i])
        if (r[3] in GV.Actual_pins):
            r[3]=GV.virtual_pins[r[3]-1]
        if (r[4] in GV.Actual_pins):
            r[4]=GV.virtual_pins[r[4]-1]
        GV.comp_display.append(r)
    
def CM_Global_Group_Data(x):
    GV.Global_Group_data_display=[]
   
    for i in range(len(GV.Local_Group_data)):
        read=(GV.Local_Group_data[i])
        ckt=[]
        for j in range(len(read)):
            if (read[j] in GV.Actual_pins):
                ind=GV.Actual_pins.index(read[j])
                ckt.append(GV.virtual_pins[ind])
            
        GV.Global_Group_data_display.append(ckt)    
    print("GV.Global_Group_data_display",GV.Global_Group_data_display)
    
def CM_Group_Data_Diagno(x):

    GV.Local_Group_data_display=[]
   
    for i in range(len(GV.Local_Group_data)):
        read=(GV.Local_Group_data[i])
        ckt=[]
        for j in range(len(read)):
            if (read[j] in GV.Actual_pins):
                ind=GV.Actual_pins.index(read[j])
                ckt.append(GV.virtual_pins[ind])
            
        GV.Local_Group_data_display.append(ckt)    
    print("GV.Local_Group_data_display",GV.Local_Group_data_display)
def CM_HA_Group_Data_Diagno(x):
    GV.Local_Group_data_display=[]

    for i in range(len(GV.Local_Group_data)):
        read=(GV.Local_Group_data[i])
        ckt=[]
        for j in range(len(read)):
            if (read[j] in GV.Actual_pins):
                ind=GV.Actual_pins.index(read[j])
                ckt.append(GV.virtual_pins[ind])
            
        GV.Local_Group_data_display.append(ckt)    
    print("GV.Local_Group_data_display",GV.Local_Group_data_display)
def CM_HA_Switch_Detection(x):
    GV.Switch_display=[]
    for i in range (len(GV.Switch_status)):
        if(GV.Switch_status[i][1]== 1):
            result = ['Group'+ ' '+str(GV.Switch_status[i][0]),'Press']
        else:
            result = ['Group'+ ' '+str(GV.Switch_status[i][0]),'Release']
        
        GV.Switch_display.append(result)
def CM_Switch_Detection(x):
    GV.Switch_display=[]
    for i in range (len(GV.Switch_status)):
        if(GV.Switch_status[i][1]== 1):
            result = ['Group'+ ' '+str(GV.Switch_status[i][0]),'Press']
        else:
            result = ['Group'+ ' '+str(GV.Switch_status[i][0]),'Release']
        
        GV.Switch_display.append(result)

        

def CM_HA_ccheckboard(x):
    GV.short_pin=[]

    for i in range (len(GV.chekb_data)):
        if (GV.chekb_data[i] in GV.Actual_pins):
            ind=GV.Actual_pins.index(GV.chekb_data[i])
            GV.short_pin.append(GV.virtual_pins[ind])
    print("checkboard_list.....",GV.short_pin)
def CM_Check_board(x):
    GV.short_pin=[]

    for i in range (len(GV.chekb_data)):
        if (GV.chekb_data[i] in GV.Actual_pins):
            ind=GV.Actual_pins.index(GV.chekb_data[i])
            GV.short_pin.append(GV.virtual_pins[ind])
            
           
     
    print("checkboard_list.....",GV.short_pin)
            
def CM_Learn_Hrn(x):

    GV.ckt_net=[]
    
    circuits=GV.circuits
    print("circuits....",circuits)
        
 
    try:
        for i in range(len(circuits)):
            read=(circuits[i])
            ckt=[]
            
            for j in range(len(read)):
                if (read[j] in GV.Actual_pins):
                    ind=GV.Actual_pins.index(read[j])
                    ckt.append(GV.virtual_pins[ind])
                    # ckt.append(GV.virtual_pins[read[j]-1])
                
            GV.ckt_net.append(ckt)
        print("check....",GV.ckt_net)
    except(IndexError):
        print("No data  in circuit")
def CM_HA_Show_points(x):
    GV.ckt_net=[]
    circuits=GV.circuits
    # print("GV.Actual_pins",GV.Actual_pins)
    # print("GV.virtual_pins",GV.virtual_pins)
    for i in range(len(circuits)):
        read=(circuits[i])
        ckt=[]
        for j in range(len(read)):
            if (read[j] in GV.Actual_pins):
                ind=GV.Actual_pins.index(read[j])
                ckt.append(GV.virtual_pins[ind])
            
        GV.ckt_net.append(ckt)    
    print("GV.ckt_net",GV.ckt_net)

def CM_Show_points(x):
    
    GV.ckt_net=[]
    
    circuits=GV.circuits
   
    for i in range(len(circuits)):
        read=(circuits[i])
        ckt=[]
        for j in range(len(read)):
            if (read[j] in GV.Actual_pins):
                ckt.append(GV.virtual_pins[read[j]-1])
            
        GV.ckt_net.append(ckt)    
    print("GV.ckt_net",GV.ckt_net)
def CM_Self_test(x):
    GV.selftest_pin=[]
    for i in range (len(GV.short_array)):
        if (GV.short_array[i] in GV.Actual_pins):
            GV.selftest_pin.append(GV.virtual_pins[GV.short_array[i]-1])
    
def CM_HA_Self_test(x):
    GV.selftest_pin=[]
    for i in range (len(GV.short_array)):
        if (GV.short_array[i] in GV.Actual_pins):
            GV.selftest_pin.append(GV.virtual_pins[GV.short_array[i]-1])
def CM_boardtest(x):
    pass
##    print("boardtest_Screen")

def CM_Operational_Message(x):
    print("CM_Operational_Message")



# if __name__ == '__main__':
#     print("special_pins")
##    CAN_configuration()
##    GV.Card_counter=card_status()
##    print("total_card", GV.Card_counter)
##    GV.total_point=GV.Card_counter*64
##    GV.module_no=1
##    while 1:
##        Module_list(GV.module_no)
##        time.sleep(0.1)
        
    

