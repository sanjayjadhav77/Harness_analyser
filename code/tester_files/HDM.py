import sys
sys.path.insert(1, '/home/pi/Desktop/.HA_Editor/code')
import can
from SSLT import *
import global_var
import global_test_var as GV
import time
import os
from Sql_db import*
import numpy as np
from Actuation import *
# GV.Visual_Engine_Start=3
 
from CAN_Bus import *
from  Sql_db import *
def ConnectorActualpin_Display(x,y):
    if(GV.ConectorVisual=='0'):
        if (x in GV.Actual_pins and  y in GV.Actual_pins):
            xind=GV.Actual_pins.index(x)
            yind=GV.Actual_pins.index(y)
            z=GV.virtual_pins[xind]
            w=GV.virtual_pins[yind]
    else:
        if(GV.IO_error_code==6):
            if (GV.ClickOn_Next==0):
                Cavity_Details(GV.x,GV.intpoint1)
                z=GV.connector1_name+'-'+ str(GV.cavity1)
                w=GV.connector2_name+'-'+str(GV.cavity2)
            else:
                Cavity_Details(GV.y,GV.intpoint2)
                z=GV.connector1_name+'-'+ str(GV.cavity1)
                w=GV.connector2_name+'-'+str(GV.cavity2)
        else:
            
            Cavity_Details(GV.x,GV.y)
            z=GV.connector1_name+'-'+ str(GV.cavity1)
            w=GV.connector2_name+'-'+str(GV.cavity2)
    return(z,w)
#------------------------------------Connector Visuals-----------------------------
def Cavity_Details(a,b):
    cavity1=0
    connector1=0
    connector1_name=0
    wtype1=0
    wcolor1a=' '
    wcolor1b=' '
    wgauge1=0
    
    cavity2=0
    connector2=0
    connector2_name=0
    wtype2=0
    wcolor2a=' ' 
    wcolor2b=' '
    wgauge2=0
    GV.Visual_Engine_Start=0
    if(GV.ConectorVisual=='1'):
        for j in range(len(GV.Local_Group2_File)):
            if a in GV.Local_Group2_File[j]:
                connector1=j
                connector_cavity=GV.Local_Group3_File[j]
                cavity1=int(connector_cavity[GV.Local_Group2_File[j].index(a)])
                break
            else:
                connector1 = None
        for j in range(len(GV.Local_Group2_File)):
            if b in GV.Local_Group2_File[j]:
                connector2=j
                connector_cavity=GV.Local_Group3_File[j]
                cavity2=int(connector_cavity[GV.Local_Group2_File[j].index(b)])
                break
            else:
                connector2 = None
##            print("GV.Local_Group2_File.........",GV.Local_Group2_File)
##            print("connector1................",connector1,connector2)
        if (connector1 != None and connector2 != None ):
            for j in range(len(GV.circuits)):
                if a in GV.circuits[j]:
                    wtype1=GV.Wire_Type[j]
                    wcolor1a=GV.Wire_color1[j]
                    wcolor1b=GV.Wire_color2[j]
                    wgauge1=GV.Wire_Gauge[j]
            for j in range(len(GV.circuits)):
                if b in GV.circuits[j]:
                    wtype2=GV.Wire_Type[j]
                    wcolor2a=GV.Wire_color1[j]
                    wcolor2b=GV.Wire_color2[j]
                    wgauge2=GV.Wire_Gauge[j]
##                print("GV.Connector_Part_Name",GV.Connector_Part_Name)
            
            connector1_name=str(GV.Connector_Part_Name[int(connector1)])
            connector2_name=str(GV.Connector_Part_Name[int(connector2)])
        
            GV.cavity1=cavity1
            GV.connector1=connector1
            GV.connector1_name=connector1_name
            GV.wtype1=wtype1
            if (len(wcolor1a)>0):
                if ('/') in wcolor1a:
                    x=wcolor1a.split("/")
                    GV.wcolor1a=x[0]
                    GV.wcolor1b=x[1]

                else:    
                    GV.wcolor1a=wcolor1a
                    GV.wcolor1b=wcolor1b
            GV.wgauge1=wgauge1

            GV.cavity2=cavity2
            GV.connector2=connector2
            GV.connector2_name=connector2_name
            GV.wtype2=wtype2
            if (len(wcolor2a)>0):
                if ('/') in wcolor2a:
                    x=wcolor2a.split("/")
                    GV.wcolor2a=x[0]
                    GV.wcolor2b=x[1]

                else:    
                    GV.wcolor2a=wcolor2a
                    GV.wcolor2b=wcolor2b
            

##            print("color",GV.wcolor2a,GV.wcolor2b,GV.wcolor1a,GV.wcolor1b)
            GV.wgauge2=wgauge2
            GV.Visual_Engine_Start=1
        else:
            GV.connector1_name='None'
            GV.connector2_name='None'
            GV.cavity1=a
            GV.cavity2=b
            GV.wtype1=' '
            GV.wtype2=' '
            GV.Visual_Engine_Start=5
    
            
    else:
        GV.connector1_name='P'
        GV.cavity1=a
        GV.connector2_name='P'
        GV.cavity2=b
        GV.wtype1=' '
        GV.wtype2=' '

#--------------------------------------card initialization--------------------------------------------------#
def card_init():
    for i in range (1,GV.Card_counter+1):
        GV.msg= can.Message(arbitration_id =  0x7D0 | i , data=[0x05,0x00,0x00,0x00],extended_id=False)
        data=send_msg()
        if(data==0):
            try:
                GV.message = GV.bus.recv(0.1)
##                print("test",GV.message)
            except(AttributeError, IOError, ValueError, TypeError):
                CAN_stop()
                time.sleep(1)
                CAN_start()
                print("Error while reciving Data")
##                print(" dummy-----------------------",dummy)
        else:
            print("IO error occured")
#---------------------------------------Card status function---------------------------------------------------#        
def card_status():
    count_card=0
    
    for i in range (1,17):
        GV.msg = can.Message(arbitration_id= 0x7D0 | i , data=[0x04,0x00,0x00,0x00],extended_id=False)
        GV.bus.send(GV.msg)
##        print(msg)
        try:
            GV.message = GV.bus.recv(0.01) 
            card_detect = (GV.message.data[3])
            if (card_detect == i):
                print("card" + " " + str(i) + " " + "present")
                count_card += 1
               
            else:
                
                # pass
                print("card" + " " + str(i) + " " + "absent")
                
        except(AttributeError, IOError, ValueError, TypeError):
            # pass
            print("card" + " " + str(i) + " " + "absent")
            
    #print("total_card", count_card)
    return(count_card)
#---------------------------------------------- led navigation----------------------------------------------------------------------------------
def Led_test():
    for x in range(len(GV.led)):
        single_write(GV.led[x][1],1)
        time.sleep(0.5)
    time.sleep(1)
    for x in range(len(GV.led)):
        single_write(GV.led[x][1],0)
        time.sleep(0.5)
    time.sleep(1)    

def Leakpin_test():
    for x in range(len(GV.leakage)):
        single_write(GV.leakage[x][1],1)
        time.sleep(0.5)
    time.sleep(1)
    for x in range(len(GV.leakage)):
        single_write(GV.leakage[x][1],0)
        time.sleep(0.5)
    time.sleep(1) 

def Led_self_test():
    led=[1,3,5,6,8,9,16,32,64]
    for x in range(len(led)):
        single_write(led[x],1)
        time.sleep(0.01)
    time.sleep(2)
    for x in range(len(led)):
        single_write(led[x],0)
        time.sleep(0.01)

def connector_led_on():
    led=[1,3,5,6,8,9,16,32,64]
    for x in range(len(led)):
        single_write(led[x],1)
        time.sleep(0.1)
        
def connector_led_off():
    led=[1,3,5,6,8,9,16,32,64]
    for x in range(len(led)):
        single_write(led[x],0)
        time.sleep(0.1)

def Error_indication(x,y):

    led_pin=[]
    for i in range(len(GV.Group_data)):
        if x in GV.Group_data[i]:
            grpNo1=(GV.Group_data.index(GV.Group_data[i])+1)
        if y in GV.Group_data[i]:
            grpNo2=(GV.Group_data.index(GV.Group_data[i])+1)
    for i in range (len(GV.led)):
        if (grpNo1 == GV.led[i][0]):
            led_pin.append(GV.led[i][1])
        if (grpNo2 == GV.led[i][0]):
            led_pin.append(GV.led[i][1])
##    print("led_pin",led_pin)
    # Clear_led_all(led_pin)
    
    if (GV.lastled1==0 and GV.lastled2==0):
        pass
    else:
        single_write(GV.lastled1,0)
        single_write(GV.lastled2,0)
        time.sleep(0.05)
    try:
        GV.lastled1=led_pin[0]
        
        GV.lastled2=led_pin[1]
    except(IndexError):
        print("Led Pin Not Present")
    for x in range(len(led_pin)):
        
        single_write(led_pin[x],1)
##        time.sleep(0.1)
        
def Clear_led_all():
    for x in range(len(GV.led)):
        single_write(GV.led[x][1],0)
        time.sleep(0.01)
        
#-----------------------------------------------------------switch detection---------------------------------------------------------------------
def Switch_Detection(x):
##    GV.switch=[[1, 3], [2, 9], [3, 16], [4, 23]]
    GV.Switch_status=[]
    for i in range(len(GV.switch)):
##        print(GV.switch[i][1])
        status=single_read(GV.switch[i][1])
        x=[GV.switch[i][0],status]
        GV.Switch_status.append(x)
    
    print("Switch_status",GV.Switch_status)
    GV.data_Available=5
    GV.module_no=0
def HA_Switch_Detection(x):
##    GV.switch=[[1, 3], [2, 9], [3, 16], [4, 23]]
    GV.Switch_status=[]
    for i in range(len(GV.switch)):
##        print(GV.switch[i][1])
        status=single_read(GV.switch[i][1])
        x=[GV.switch[i][0],status]
        GV.Switch_status.append(x)
    
    print("Switch_status",GV.Switch_status)
    GV.data_Available=10
    GV.module_no=0
#--------------------------------------------------------Check board array generation-----------------------------------------------#
def checkboard_status(x):
    global checkboard_point
##    io_error_flag=0
    GV.checkboard_list=[]
   # card_init()
    error=multiple_read()
##    checkboard_point=0
    if(error==0):
        for position in range(GV.Card_counter*64):
            if(array[position]==1):
                if( (position+1) not in GV.special_pins):
                    GV.checkboard_list.append(position+1)
    else:
       print("error")
       GV.checkboard_list=[]
    GV.chekb_data = GV.checkboard_list
    GV.data_Available=1
##    print("checkboard_list.........",GV.chekb_data) #short point
##    if(len(checkboard_list)>0):
##        short_pin=checkboard_list[0]
def HA_checkboard_status(x):
    global checkboard_point
##    io_error_flag=0
    GV.checkboard_list=[]
    
   # card_init()
    # if(GV.Check_bypass==1):
    error=multiple_read()
##    checkboard_point=0
    if(error==0):
        for position in range(GV.Card_counter*64):
            if(array[position]==1):
                if( (position+1) not in GV.special_pins):
                    GV.checkboard_list.append(position+1)
    else:
        print("Error")
        GV.checkboard_list=[]
    GV.chekb_data = GV.checkboard_list
##    print("checkboard_list.........",GV.chekb_data) #short point
    GV.data_Available=9
   
#----------------------------------------------------------------------------------------------------------------------------------#   
def Learn_Harness(x):
##    t1=time.time()
    if(GV.stage==1):
        DeleteHarnessData(GV.Location_No)
    print("execute sucefull...........",GV.stage)
    global learn_error
    global circuits
    learn_error=0
    learn_array=[]
    flag1=0
    Learn_Harness_list=[[] for i in range(GV.total_point+1)]
    GV.circuits_temp=[]
        
   
    for k in range(1,(GV.total_point+1)):
        if(k not in GV.special_pins):       ##spl line to skip learn from spl pins  
            #print(k)
            for j in range(GV.total_point+1):
                #print(k,j)
                if(k in Learn_Harness_list[j]):
                    flag1=1
                    break
                else:
                    flag1=0
                       
            if(flag1==0):
                learn_result = IOclear_and_IOread(k)
                if(learn_result==0):
                    for position in range(k-1,GV.total_point):
                        if(array[position]==1):
                            if((position+1) not in GV.special_pins):
                                if(k not in Learn_Harness_list[k-1]):
                                    Learn_Harness_list[k-1].append(k)      
                                Learn_Harness_list[k-1].append(position+1)                   

                elif(learn_result==1):
                    print("Error in IOclear and IOread")
                
#    print(Learn_Harness_list)

    for i in range(len(Learn_Harness_list)):
        temp = []
        learn_pnt = Learn_Harness_list[i]
        for j in range(len(learn_pnt)):
            if(learn_pnt[j] != 0):
                temp.append(learn_pnt[j])
        learn_array.append(temp)

    for k in range(len(learn_array)):
        if(len(learn_array[k])>1):
            GV.circuits_temp.append(learn_array[k])
            
##    print("circuits",GV.circuits)
    
    if (len(GV.circuits_temp)>(GV.total_point/2)):
        GV.circuits_temp=[]
    for a in range(len(GV.circuits_temp)):
        #print("GV.circuits[a]",len( GV.circuits[a]))
        if (len(GV.circuits_temp[a])>128):
            GV.circuits_temp=[]
    
    GV.circuits=GV.circuits_temp
    print("circuits",(GV.circuits))
    Stage1_Points_No=0
    for i in range (len(GV.circuits)):
        for j in range (len(GV.circuits[i])):
            Stage1_Points_No+=1

    GV.data_Available=4
    GV.module_no=0
##    t2=time.time()
##    print("time..",t2-t1)
#--------------------------------------------------------------------------------------------------------------------------------
def Harness_Availability(x):  ##Self_Test() harness available harness_remove()
    print("execute sucefull...........")
    global short_flag
    short_flag=0
    learn_error=0
    GV.short_array=[]
    flag1=0
    Learn_Harness_list=[[] for i in range(GV.total_point+1)]

    for k in range(1,(GV.total_point+1)):
        if(k not in GV.special_pins):       ##spl line to skip learn from spl pins 
            if(short_flag==1):
                break
            for j in range(GV.total_point+1):
                if(k in Learn_Harness_list[j]):
                    flag1=1
                    break
                else:
                    flag1=0
                       
            if(flag1==0):
                learn_result = IOclear_and_IOread(k)
                if(learn_result==0):
                    for position in range(GV.total_point):
                        if(array[position]==1):
                            if((position+1) not in GV.special_pins):
                                if(k not in Learn_Harness_list[k-1]):
                                            Learn_Harness_list[k-1].append(k) 
                                Learn_Harness_list[k-1].append(position+1)
                                if(len(Learn_Harness_list[k-1])>1):
                                    GV.short_array=Learn_Harness_list[k-1]
                                    short_flag=1
                                    break

                elif(learn_result==1):
                    print("Error in IOclear and IOread")
    print("GV.short_array",GV.short_array)
    GV.data_Available=3
    GV.module_no=0
    return(short_flag)

def HA_Harness_Availability(x):  ##Self_Test() harness available harness_remove()
    print("execute sucefull...........")
    global short_flag
    short_flag=0
    learn_error=0
    GV.short_array=[]
    flag1=0
    Learn_Harness_list=[[] for i in range(GV.total_point+1)]

    for k in range(1,(GV.total_point+1)):
        if(k not in GV.special_pins):       ##spl line to skip learn from spl pins 
            if(short_flag==1):
                break
            for j in range(GV.total_point+1):
                if(k in Learn_Harness_list[j]):
                    flag1=1
                    break
                else:
                    flag1=0
                       
            if(flag1==0):
                learn_result = IOclear_and_IOread(k)
                if(learn_result==0):
                    for position in range(GV.total_point):
                        if(array[position]==1):
                            if((position+1) not in GV.special_pins):
                                if(k not in Learn_Harness_list[k-1]):
                                            Learn_Harness_list[k-1].append(k) 
                                Learn_Harness_list[k-1].append(position+1)
                                if(len(Learn_Harness_list[k-1])>1):
                                    GV.short_array=Learn_Harness_list[k-1]
                                    short_flag=1
                                    break

                elif(learn_result==1):
                    print("Error in IOclear and IOread")
##    print("GV.short_array",GV.short_array)
    if (GV.HA==0):
        GV.data_Available=13
        GV.module_no=0
    else:
        GV.HA=0
        
    return(short_flag)
def test_Harness_Availability(x):  ##Self_Test() harness available harness_remove()
    print("execute sucefull...........")
    global short_flag
    short_flag=0
    learn_error=0
    GV.short_array=[]
    flag1=0
    Learn_Harness_list=[[] for i in range(GV.total_point+1)]

    for k in range(1,(GV.total_point+1)):
        if(k not in GV.special_pins):       ##spl line to skip learn from spl pins 
            if(short_flag==1):
                break
            for j in range(GV.total_point+1):
                if(k in Learn_Harness_list[j]):
                    flag1=1
                    break
                else:
                    flag1=0
                       
            if(flag1==0):
                learn_result = IOclear_and_IOread(k)
                if(learn_result==0):
                    for position in range(GV.total_point):
                        if(array[position]==1):
                            if((position+1) not in GV.special_pins):
                                if(k not in Learn_Harness_list[k-1]):
                                            Learn_Harness_list[k-1].append(k) 
                                Learn_Harness_list[k-1].append(position+1)
                                if(len(Learn_Harness_list[k-1])>1):
                                    GV.short_array=Learn_Harness_list[k-1]
                                    short_flag=1
                                    break

                elif(learn_result==1):
                    print("Error in IOclear and IOread")

        
    return(short_flag)
#--------------------------------------------Test Engine-----------------------------------------------------------------------------------
def Test_engine(point1,point2):
    #print("point1,point2",point1,point2)
    
    if(GV.update==1 or (point1==1  and point2==2)):
        GV.update=0
        IO_error=IOclear_and_IOread(GV.x)
        if(IO_error==1):
            return 9
        #print("GV.x...................",GV.x)
    
    Csr=1 if(array[GV.y-1]==1) else 0
    status=Csr
    if(status==0):
        if(proper_circuit(point1,point2)==0):
            GV.intpoint1=0
            GV.intpoint2=0
            #print("no issue",GV.x,GV.y)
            return 1
        else:
            
            inc=interchange_test(point1,point2)
            if(inc==1):
##                print("interchange",point2,GV.intpoint1,point1,GV.intpoint2)
                return 6
            else:
                #print("open",GV.x,GV.y)
                GV.intpoint1=0
                GV.intpoint2=0
                return 3
            
    else:
        #print("connection_status done")
        if(proper_circuit(point1,point2)==1):
            #print("valid net",GV.x,GV.y)
            GV.intpoint1=0
            GV.intpoint2=0
            GV.tested_circuits.append(GV.x)
            GV.tested_circuits.append(GV.y)
            return 2
        
        else:
            flag1=0
            flag2=0
            for i in range(len(GV.circuits_temp)):
                if(point1 in GV.circuits_temp[i]):
##                    print(point1)
                    flag1=1
                    short1=i
                if(point2 in GV.circuits_temp[i]):
##                    print(point2)
                    flag2=1
                    short2=i
                
            if((flag1==0)&(flag2==0)):
              #print("extra points",point1,point2)
              GV.intpoint1=0
              GV.intpoint2=0
              if(GV.Multi_stage==1):
                  return(7)
              else:
                  return(1)
                  
            
            if(((flag1==1)&(flag2==0))or((flag1==0)&(flag2==1))):
              #print("short point",point1,point2)
              GV.intpoint1=0
              GV.intpoint2=0
              return(4)

            if((flag1==1)&(flag2==1)):
                #print(" group short check",point1,point2,GV.x,GV.y)
              #print("GV.circuits[i]",GV.circuits[short1],GV.circuits[short2])
              if(point1==GV.circuits_temp[short1][0] and point2==GV.circuits_temp[short2][0]):
                  GV.intpoint1=0
                  GV.intpoint2=0
                  return(4)
                  
              else:
                  Max_array=[]
                  for k in range(len(GV.circuits_temp[short1])):
                      if (GV.circuits_temp[short1][k]) > point2:
                          Max_array.append(GV.circuits_temp[short1][k])
               
                  for k in range(len(Max_array)):
                      if(k not in GV.special_pins):
                          if(array[Max_array[k]-1]==0):
                              insertion=Max_array[k]
                              GV.intpoint2=insertion
                              GV.intpoint1=GV.circuits_temp[short2][0]
                              if(GV.intpoint1==point2):
                                  GV.intpoint1=GV.circuits_temp[short2][1]
                              #print("interchange ",point1,point2,GV.intpoint1,GV.intpoint2)
                              return(6)
              #print("short point",point1,point2)
              GV.intpoint1=0
              GV.intpoint2=0
              return(4)   
             


def proper_circuit(po1,po2):
  flag=0
  for i in range(len(GV.circuits_temp)):
    if((po1 in GV.circuits_temp[i])&(po2 in GV.circuits_temp[i])):
      flag=1
  return(flag)

def interchange_test(pt1,pt2):
    global circuits_single_list
    import numpy
    flag=0
    for i in range(pt2, GV.total_point):
        if(i not in GV.special_pins):
            if(array[i]==1):
                flag=1
                break
        
    if(flag==1):
        z = i+1
       
        for i in range(len(GV.circuits_temp)):
            abc = GV.circuits_temp[i]
            if(z in abc):
                GV.intpoint1 = abc[0]
                GV.intpoint2 = abc[1]
                #print("checkup",pt1,pt1,GV.intpoint1,GV.intpoint2)
                if(pt1!=pt2 and pt1!=GV.intpoint1 and pt1!=GV.intpoint2):
                    print("interchange ",pt1,pt2,GV.intpoint1,GV.intpoint2)
                    return 1
                else:
                    return 0
                    
    return 0
#-----------------------------------------------------Engine spl case-------------------------------------------------------------
def Spl_case_Handle():
    #IO_error_code 1= no issue,2=valid point,3=openpoint,4=short point,5=group short,6=interchange,7=extra
    #tester points GV.x & GV.y
    x=1
    #y increament
    while(x==1):
        GV.y+=1
        
        #both point are same increment second point
        if(GV.x==GV.y):
            GV.y=GV.y+1
        
        # y is equal to greater than total points
        if(GV.y>GV.total_point):
            GV.x+=1
            # y is less than x then xincrement by one and assign to y                      
            while(GV.x in GV.tested_circuits):
                GV.x+=1
            GV.y=GV.x+1  
            GV.update=1
            
        if(GV.x >=(GV.total_point)):#complete test process exit from test engine

            GV.tested_circuits=[] 
            GV.x=1
            GV.y=2
            GV.IO_error_code=8
            GV.Intruption_flag=0
            GV.Visual_Engine_Start=4
            # print(" Multi Stage harness pass")
            UploadProdLog_Data(GV.Location_No,GV.Part_Name,'Engine Start','Multi Stage pass')
            GV.Display_Message= str(GV.Multi_stage)+" Stage harness pass"
            GV.data_delivered=13
        # time.sleep(0.2) 
          
        if((GV.x  in GV.special_pins) or (GV.y  in GV.special_pins)):
            x=1
            # print("Skip avoiding testing of spl pins",GV.x,GV.x)
        else:
            x=0

          


#-----------------------------------------------------Engine start----------------------------------------------------------------
def Engine_start():

    
    if((GV.IO_error_code==1) or (GV.IO_error_code==2) ):
        Spl_case_Handle()
        #print("test1..................................")
    else:
         GV.update=1
         if(GV.All_Error== 1 and GV.Allcircuit_error==1):
            #  if((GV.Privious_x!=GV.x) and (GV.Privious_y!=GV.y) and (GV.Privious_intpoint1!=GV.intpoint1) and (GV.Privious_intpoint2!=GV.intpoint2)):
            GV.Allcircuit_error=0
            GV.tested_circuits=[]
            GV.x=1
            GV.y=2


         #print("test2..................................")
    if(GV.Intruption_flag==1):
        GV.IO_error_code=Test_engine(GV.x,GV.y)

    if(GV.IO_error_code==1):
        if(GV.All_Error!= 1 ):

            if(GV.x in GV.Actual_pins):
                steps=GV.total_point/8
                if(((GV.x % steps)==0) and( GV.y==GV.total_point)):# this is used for testing speed.  show processing message at the time of GV.x change
                    GV.Visual_Engine_Start=2
                    ind=GV.Actual_pins.index(GV.x)
                    z=GV.virtual_pins[ind]
                    GV.Display_Message=("Processing...............NET- "+str(z))
                    GV.message_color=1
##        print("E1.no issue",GV.x,GV.y)
    if(GV.IO_error_code==2):
        Clear_led_all()
##        print("E2.Valid ",GV.x,GV.y)
    if(GV.IO_error_code==3):
        Error_indication(GV.x,GV.y)
        GV.message_color=2
        if(str(GV.Cutter_status)=='1'):
            z,w=ConnectorActualpin_Display(GV.x,GV.y)
            Smsg="S"+str(GV.Multi_stage)
            GV.Display_Message=(Smsg+"-Open Point:  "+str(z)+' '+str(w)+"    Timeout-"+str(round(GV.Open_point_Timeout-GV.time_gap)))
            print(Smsg+"-Open Point:  "+str(z)+'-'+str(w)+"    Timeout-"+str(round(GV.Open_point_Timeout-GV.time_gap)))
            cutter_timeout(GV.Open_point_Timeout)
            GV.Allcircuit_error=1
                  
        else:
            z,w=ConnectorActualpin_Display(GV.x,GV.y)
            Smsg="S"+str(GV.Multi_stage)
            GV.Display_Message=(Smsg+"-Open Point:  "+str(z)+'   '+str(w))
            print(Smsg+"-Open Point:  "+str(z)+' '+str(w))
            GV.Allcircuit_error=1
            GV.Privious_x=GV.x
            GV.Privious_y=GV.y
            GV.Privious_intpoint1=GV.intpoint1
            GV.Privious_intpoint2=GV.intpoint2
            
            
    elif(GV.IO_error_code==4):
        Error_indication(GV.x,GV.y)
        GV.message_color=2
        if(GV.Cutter_status==1):
            z,w=ConnectorActualpin_Display(GV.x,GV.y)
            Smsg="S"+str(GV.Multi_stage)
            GV.Display_Message=(Smsg+"-short point "+str(z)+' '+str(w)+"    Timeout-"+str(round(GV.Short_point_Timeout-GV.time_gap)))
            print(Smsg+"-short point "+str(z)+' '+str(w)+"    Timeout-"+str(round(GV.Short_point_Timeout-GV.time_gap)))
            cutter_timeout(GV.Short_point_Timeout)
            GV.Allcircuit_error=1
        else:
            z,w=ConnectorActualpin_Display(GV.x,GV.y)
            Smsg="S"+str(GV.Multi_stage)
            GV.Display_Message=(Smsg+"-short point "+str(z)+'   '+str(w))
            print(Smsg+"-short point "+str(z)+' '+str(w))
            GV.Allcircuit_error=1
            GV.Privious_x=GV.x
            GV.Privious_y=GV.y
            GV.Privious_intpoint1=GV.intpoint1
            GV.Privious_intpoint2=GV.intpoint2
            
    elif(GV.IO_error_code==6):
        Error_indication(GV.x,GV.y)
        GV.message_color=2
        if(GV.Cutter_status==1):
            if (GV.intpoint1 in GV.Actual_pins and GV.intpoint2 in GV.Actual_pins):
                z,w=ConnectorActualpin_Display(GV.x,GV.y)
                Smsg="S"+str(GV.Multi_stage)
                a=GV.virtual_pins[(GV.intpoint1)-1]
                b=GV.virtual_pins[(GV.intpoint2)-1]
                GV.Display_Message=(Smsg+"-Int Point:"+str(z)+'-'+str(a)+' '+str(w)+'-'+str(b)+"   Timeout-"+str(round(GV.Interchange_point_Timeout-GV.time_gap)))
                print(Smsg+"-Interchange Point:"+str(z)+'-'+str(a)+' '+str(w)+'-'+str(b)+" Timeout-"+str(round(GV.Interchange_point_Timeout-GV.time_gap)))
                cutter_timeout(GV.Interchange_point_Timeout)
                GV.Allcircuit_error=1
        else:
            if (GV.intpoint1 in GV.Actual_pins and GV.intpoint2 in GV.Actual_pins):
                z,w=ConnectorActualpin_Display(GV.x,GV.y)
                Smsg="S"+str(GV.Multi_stage)  
                a=GV.virtual_pins[(GV.intpoint1)-1]
                b=GV.virtual_pins[(GV.intpoint2)-1]
                GV.Display_Message=(Smsg+"-Int Point:"+str(z)+'-'+str(a)+' '+str(w)+'-'+str(b))
                print(Smsg+"-Interchange Point:"+str(z)+'-'+str(a)+' '+str(w)+'-'+str(b))
                GV.Allcircuit_error=1
                GV.Privious_x=GV.x
                GV.Privious_y=GV.y
                GV.Privious_intpoint1=GV.intpoint1
                GV.Privious_intpoint2=GV.intpoint2
                
    elif(GV.IO_error_code==7):
        Error_indication(GV.x,GV.y)
        GV.message_color=2
        if(GV.Cutter_status==1):
            z,w=ConnectorActualpin_Display(GV.x,GV.y)
            Smsg="S"+str(GV.Multi_stage)
            GV.Display_Message=(Smsg+"-Extra "+str(z)+' '+str(w)+"    Timeout-"+str(round(GV.Extra_point_Timeout-GV.time_gap)))
            print(Smsg+"-Extra "+str(z)+'-'+str(w)+"    Timeout-"+str(round(GV.Extra_point_Timeout-GV.time_gap)))
            cutter_timeout(GV.Extra_point_Timeout)
            GV.Allcircuit_error=1
        else:
            z,w=ConnectorActualpin_Display(GV.x,GV.y)
            Smsg="S"+str(GV.Multi_stage)
            GV.Display_Message=(Smsg+"-Extra "+str(z)+'   '+str(w))
            print(Smsg+"-Extra "+str(z)+'-'+str(w))
            GV.Allcircuit_error=1
            GV.Privious_x=GV.x
            GV.Privious_y=GV.y
            GV.Privious_intpoint1=GV.intpoint1
            GV.Privious_intpoint2=GV.intpoint2
    
    elif(GV.IO_error_code==8):
        if(GV.Sample_Production==1):
            GV.Cutter_Action=1
            Sample_mode()  
        else:
            print("harness pass")
        
    elif(GV.IO_error_code==9):
        print("Communication error-----------------------------")

    GV.data_delivered=13

    # if((GV.IO_error_code==3) or (GV.IO_error_code==4)or (GV.IO_error_code==5) or(GV.IO_error_code==6) or (GV.IO_error_code==7)) :
    #     HA_result=1
    #     HA_result=test_Harness_Availability(1)
    #     if(HA_result==0):
    #         print("harness remove")
    #         GV.Abort_Event_flag=1
    #         GV.Abort_flag=1
            #GV.Intruption_flag=0
            #GV.Abort_flag=1
   
        
    
#--------------------------------------------------------------------------------------------------------------------------------
def cutter_timeout(t1):
    global timeout
    timeout=t1
    
    if((GV.Privious_x==GV.x) and (GV.Privious_y==GV.y) and (GV.Privious_intpoint1==GV.intpoint1) and (GV.Privious_intpoint2==GV.intpoint2)):
        GV.Current_Time=time.time()
        GV.time_gap=0
    else:
        GV.Privious_x=GV.x
        GV.Privious_y=GV.y
        GV.Privious_intpoint1=GV.intpoint1
        GV.Privious_intpoint2=GV.intpoint2
        GV.Previous_Time=time.time()
        GV.Current_Time=time.time()
        
    GV.time_gap=GV.Current_Time-GV.Previous_Time
##    print("timeout-",timeout)
##    print("GV.time_gap",GV.time_gap)
    if(GV.time_gap > float(timeout)):
        if(GV.Sample_Production==1):
            GV.Sample_result=Sample_mode()  
        GV.Previous_Time=time.time()
        GV.Current_Time=time.time()
        GV.privious_x=0
        GV.privious_y=0
        GV.Privious_intpoint1=0
        GV.Privious_intpoint2=0
        
        GV.time_gap=0
        GV.tested_circuits=[]
        GV.x=1
        GV.y=1
        GV.Intruption_flag=0
        # GV.Display_Message=''
        GV.Cutter_Action=1
        if(GV.Sample_Production==1):
            GV.data_delivered=2
        else:
            cutter_set()
            # failled_on()
            time.sleep(GV.Fail_Time)
            cutter_reset()
            # failled_off() 
            
        print("timeout occured...",GV.Sample_result)
        
#--------------------------------------------------------------------------------
def sample_init(self):
    print("samle mode initialization",GV.sample_counter)

    if(GV.sample_counter !=0):
##        print("GV.temp_openflag",GV.temp_openflag,GV.temp_shortflag)
        if(GV.temp_openflag=='1'):
            GV.msgpriority=3
            self.p4.msg_line.setText("Insert Open Point Sample")
            GV.Sample_Production=1
            GV.Fo_test_Flag=1
            print("OpenPoint")
        elif(GV.temp_shortflag=='1'):
            GV.msgpriority=4
            self.p4.msg_line.setText("Insert Short Point Sample")
            GV.Sample_Production=1
            GV.Fo_test_Flag=1

            print("ShortPoint")    
        elif(GV.temp_extraflag=='1'):
            GV.msgpriority=7
            self.p4.msg_line.setText("Insert Extra Point Sample")
            GV.Sample_Production=1
            GV.Fo_test_Flag=1
            print("ExtraPoint")
        elif(GV.temp_interchangeflag=='1'):
            GV.msgpriority=6
            self.p4.msg_line.setText("Insert Interchange Point Sample")
    
            GV.Sample_Production=1
            GV.Fo_test_Flag=1
            print("Interchange")
    else:
        self.p4.msg_line.setText("Setup Mode Completed...")
        GV.Cutter_Action=0
        GV.Sample_Production=0
        global_var.p_s=0
        self.p4.production_sample()
        GV.OpenPoint_count_temp=0
        
        print("Setup Mode Completed...")
        print("GV.Estate",GV.Estate)
        time.sleep(0.6)
        GV.Estate=0
        GV.Visual_Engine_Start=3
        self.p4.msg_line.setText("Put Cable")
        
        GV.data_delivered=0
               
#--------------------------------------------------------------------------------        
def Sample_mode():
    if(GV.msgpriority == GV.IO_error_code):
        print("test",GV.Open_points)
        GV.sample_counter=GV.sample_counter-1
        if(GV.msgpriority==3):
            print("GV.x....",GV.x,GV.y)
            print("GV.Open_points",GV.Open_points)
            if((GV.x and GV.y ) not  in GV.Open_points):
                GV.Open_points.append(GV.x)
                GV.Open_points.append(GV.y)
                GV.OpenPoint_count_temp +=1
                print("GV.OpenPoint_count_temp",GV.OpenPoint_count_temp)
                print("GV.Opcount",GV.Opcount)
                if(GV.OpenPoint_count_temp==int(GV.Opcount)):
                    GV.temp_openflag='0'
                    print("open sample tested....")
                return 0
            else:
                print("Wrong sample tested....")
                GV.Display_Message="Wrong sample "
                print("Wrong sample")
                GV.sample_counter=GV.sample_counter+1
                time.sleep(0.6)
                return 2
        if(GV.msgpriority==4):
            GV.temp_shortflag='0'
            print("short sample tested....")
            return 0
        if(GV.msgpriority==7):
            GV.temp_extraflag='0'
            print("extra sample tested....")
            return 0
        if(GV.msgpriority==6):
            GV.temp_interchangeflag='0'
            print("interchange sample tested....")
            return 0

        
    else:
        GV.Display_Message="Wrong sample "
        time.sleep(0.6)
        print("Wrong sample")
        return 2
#--------------------------------card sequential--------------------------------------------
def Card_sequential():
    Card_seq_flag=0
    for i in range(GV.Card_counter):
       GV.msg = can.Message(arbitration_id= 0x7D0 | i+1 , data=[0x04,0x00,0x00,0x00],extended_id=False)
       GV.bus.send(GV.msg)
##        print(msg)
       try:
           GV.message = GV.bus.recv(0.01) 
           card_detect = (GV.message.data[3])
           if (card_detect == i+1):
               print("Your card is sequential")
               Card_seq_flag=0
           else:
               Card_seq_flag=1
               print("Your card is not sequential")
                
       except(AttributeError, IOError, ValueError, TypeError):
           Card_seq_flag=1
           print("Error")
           print("Your card is not sequential")
           break
    return(Card_seq_flag)       
###------------------------------fo--------------------------------------------------------------------------------------------------
# if __name__=='__main__':
#    CAN_configuration()
#    GV.Card_counter=card_status()
#    print("total_card", GV.Card_counter)
   
#    while(1):
#        GV.Card_counter=card_status()
#        x=Card_sequential()
#        if(x==1):
#            print("error found")
#        time.sleep(5)
##    
##    Frl_on()
####    Frl_off()
##    single_write(56,1)
##    x=0
##    while 1:
##        x=Leak_pin_test()
##        time.sleep(1)
##        if(x==1):
##            Frl_off()
##            single_write(56,0)
##            x=0
##            
####        print("testing")
##    print("Done")    


#        print(i+1)
#    GV.total_point=GV.Card_counter*64
##
##    GV.circuits=[[1, 8], [2, 14], [4, 13], [9, 10, 11, 12]]
##    GV.circuits1=[[1,2,8,9,10]] 
##    GV.x=1
##    GV.y=2
##    GV.IO_error_code=1
##    now=time.time()
##    GV.circuits_temp=GV.circuits
##    GV.Multi_stage=1
##    GV.time_gap=0
##    GV.OpenPoint_count=1
##    GV.Sample_Production=1
##    GV.sample_counter=3
##    GV.msgpriority=3
##    print("circuits point count-",GV.circuits)
##    print("test open point sample...1")
##    val1 =input()
##    while(GV.Intruption_flag):
##        Engine_start()
##    print("test open point sample...2")
##    GV.Intruption_flag=1
##    val1 =input()
##    GV.x=1
##    GV.y=2
##    while(GV.Intruption_flag):
##        Engine_start()
##
##    GV.msgpriority=4
##
##    print("test short point sample...")
##    GV.Intruption_flag=1
##    val1 =input()
##    while(GV.Intruption_flag):
##        Engine_start()
##    
##    current=time.time()
##    print("time",current-now)
##        
###--------------------------------------------------------------------------------------------------------------------------------  
##if __name__=='__main__':
##    count=0
##    CAN_configuration()
##    #    Sqdb_to_Ram(1)
##    GV.Card_counter=card_status()
##    print("total_card", GV.Card_counter)
##    GV.total_point=GV.Card_counter*64
##    card_init()
##    while 1:
##        checkboard_status(1)
#     #    count+=1
#     #    print(count)

###--------------------------------------------------------------------------------------------------------------------------------  
##if __name__=='__main__':
##    CAN_configuration()
##
##    GV.Card_counter=card_status()
##    print("total_card", GV.Card_counter)
##    GV.total_point=GV.Card_counter*64
##    GV.circuits=[[1, 8], [2, 14], [4, 13], [9, 10, 11, 12]]
##    GV.circuits1=[[1,2,8, 14], [4, 13], [9, 10, 11, 12]]
##    GV.x=1
##    GV.y=1
##    GV.IO_error_code=1
##    now=time.time()
##    GV.circuits_temp=GV.circuits
##    GV.Multi_stage=2
##    GV.time_gap=0
##    GV.OpenPoint_count=1
##    GV.Sample_Production=0
##    GV.sample_counter=3
##    GV.msgpriority=3
##    print("circuits point count-",GV.circuits)
##    now=time.time()
##    while(GV.Intruption_flag):
##        Engine_start()
##    current=time.time()
##    print("time",current-now)
   
#####--------------------------------------------------------------------------------------------------------------------------------  
##if __name__=='__main__':
##    CAN_configuration()
##    GV.Card_counter=card_status()
##    print("total_card", GV.Card_counter)
##    GV.total_point=GV.Card_counter*64
##    card_init()
##    #Sqdb_to_Ram(1)
##    now=time.time()
##    Learn_Harness(1)
##    current=time.time()
##    print("time",current-now)
##    
###-------------------------------------------------------------------------------------------
##if __name__=='__main__':
##    CAN_configuration()
##    GV.Card_counter=card_status()
##    print("total_card", GV.Card_counter)
##    GV.total_point=GV.Card_counter*64
##    card_init()
##    GV.update=1
##    print("start")
##    GV.circuits_temp=[[1,3],[4,6],[7,9]]
##    error_code=Test_engine(1,3)
##    print("error_code",error_code)
##if __name__=='__main__':
##    CAN_configuration()
##
##    GV.Card_counter=card_status()
##    print("total_card", GV.Card_counter)
##    GV.total_point=GV.Card_counter*64
##    Harness_status=Harness_Availability()
##    print("Harness_status",Harness_status)
###-------------------------------------------------------------------------------------------
# if __name__=='__main__':
#    CAN_configuration()
#    GV.Card_counter=card_status()
#    print("total_card", GV.Card_counter)
#    GV.total_point=GV.Card_counter*64
#    single_write(44,0)
##    Switch_Detection()
