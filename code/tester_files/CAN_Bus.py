import can
import time
import os
import numpy as np
import global_test_var as GV

array1 = np.zeros((64), dtype=int)
array = np.ones((256), dtype=int)
##print(array)
def CAN_start():
    os.system("sudo /sbin/ip link set can0 down ")
    os.system("sudo ip link set can0 type can restart-ms 100")
    time.sleep(0.01)
    os.system("sudo ifconfig can0 txqueuelen 1000")
    os.system("sudo /sbin/ip link set can0 up type can bitrate 1000000 ")
    

def CAN_stop():
    os.system("sudo /sbin/ip link set can0 down ")
    time.sleep(0.01)
    
CAN_start()
time.sleep(0.1)

#------------------------------------------Can configuration---------------------------------------------------#    
def CAN_configuration():
    try:
        GV.bus = can.interface.Bus(channel='can0', bustype='socketcan_native', bitrate=1000000)
    except OSError:
        print('Cannot find PiCAN board.')
        exit()
#-------------------------------------------------------------------------------------------------------------#
#----------------------------------------CAN message send-----------------------------------------------------#        
def send_msg():
    try:
        GV.bus.send(GV.msg,1)
        error_flag=0
    except can.CanError:
        error_flag=1
        print("Message NOT sent")
    return(error_flag)
#-------------------------------------------------------------------------------------------------------------#
#---------------------------------------single pin read function---------------------------------------------------#
def single_read(pin_number):
    if(pin_number<=64):
        #print("in between 1-64")
        card_id = 0x7D1
       
    elif(pin_number > 64 and pin_number<129):
         #print("in between 64-128")
         card_id = 0x7D2
         pin_number=pin_number-64

    elif(pin_number > 128 and pin_number<193):
         #print("in between 128-192")
         card_id = 0x7D3
         pin_number=pin_number-128

    elif(pin_number > 192 and pin_number<257):
         #print("in between 192-256")
         card_id = 0x7D4
         pin_number=pin_number-192     

    elif(pin_number > 256 and pin_number<321):
         #print("in between 256-320")
         card_id = 0x7D5
         pin_number=pin_number-256

    elif(pin_number > 320 and pin_number<385):
         #print("in between 320-384")
         card_id = 0x7D6
         pin_number=pin_number-320

    elif(pin_number > 384 and pin_number<449):
         #print("in between 384-448")
         card_id = 0x7D7
         pin_number=pin_number-384

    elif(pin_number > 448 and pin_number<513):
         #print("in between 448-512")
         card_id = 0x7D8
         pin_number=pin_number-448

    elif(pin_number > 512 and pin_number<577):
         #print("in between 512-576")
         card_id = 0x7D9
         pin_number=pin_number-512

    elif(pin_number > 576 and pin_number<641):
         #print("in between 576-640")
         card_id = 0x7DA
         pin_number=pin_number-576

    elif(pin_number > 640 and pin_number<705):
         #print("in between 640-704")
         card_id = 0x7DB
         pin_number=pin_number-640

    elif(pin_number > 704 and pin_number<769):
         #print("in between 704-768")
         card_id = 0x7DC
         pin_number=pin_number-704

    elif(pin_number > 768 and pin_number<833):
         #print("in between 768-832")
         card_id = 0x7DD
         pin_number=pin_number-768

    elif(pin_number > 832 and pin_number<897):
         #print("in between 832-896")
         card_id = 0x7DE
         pin_number=pin_number-832

    elif(pin_number > 896 and pin_number<961):
         #print("in between 896-960")
         card_id = 0x7DF
         pin_number=pin_number-896

    elif(pin_number > 960 and pin_number<1025):
         #print("in between 960-1024")
         card_id = 0x7D10
         pin_number=pin_number-960
    GV.msg = can.Message(arbitration_id= card_id, data=[0x01,pin_number,0x01,0x00],extended_id=False)
    data=send_msg()
    if(data==0):
        try:
            GV.message = GV.bus.recv(0.01) 
            s=''
            for i in range(GV.message.dlc ):
                s +=  '{0:x} '.format(GV.message.data[i])
##            print(GV.message.data[3])
            return(GV.message.data[3])
        except(AttributeError, IOError, ValueError, TypeError):
            print("Error while reciving Data")
            return('NONE')
#---------------------------------------single pin Write function---------------------------------------------------#    
def single_write(pin_number,pin_status):
    data_write_flag=0 # flag for data write error
    if(pin_number<=64):
        #print("in between 1-64")
        card_id = 0x7D1
       
    elif(pin_number > 64 and pin_number<129):
         #print("in between 64-128")
         card_id = 0x7D2
         pin_number=pin_number-64

    elif(pin_number > 128 and pin_number<193):
         #print("in between 128-192")
         card_id = 0x7D3
         pin_number=pin_number-128

    elif(pin_number > 192 and pin_number<257):
         #print("in between 192-256")
         card_id = 0x7D4
         pin_number=pin_number-192      
    elif(pin_number > 256 and pin_number<321):
         #print("in between 256-320")
         card_id = 0x7D5
         pin_number=pin_number-256

    elif(pin_number > 320 and pin_number<385):
         #print("in between 320-384")
         card_id = 0x7D6
         pin_number=pin_number-320

    elif(pin_number > 384 and pin_number<449):
         #print("in between 384-448")
         card_id = 0x7D7
         pin_number=pin_number-384

    elif(pin_number > 448 and pin_number<513):
         #print("in between 448-512")
         card_id = 0x7D8
         pin_number=pin_number-448

    elif(pin_number > 512 and pin_number<577):
         #print("in between 512-576")
         card_id = 0x7D9
         pin_number=pin_number-512

    elif(pin_number > 576 and pin_number<641):
         #print("in between 576-640")
         card_id = 0x7DA
         pin_number=pin_number-576

    elif(pin_number > 640 and pin_number<705):
         #print("in between 640-704")
         card_id = 0x7DB
         pin_number=pin_number-640

    elif(pin_number > 704 and pin_number<769):
         #print("in between 704-768")
         card_id = 0x7DC
         pin_number=pin_number-704

    elif(pin_number > 768 and pin_number<833):
         #print("in between 768-832")
         card_id = 0x7DD
         pin_number=pin_number-768

    elif(pin_number > 832 and pin_number<897):
         #print("in between 832-896")
         card_id = 0x7DE
         pin_number=pin_number-832

    elif(pin_number > 896 and pin_number<961):
         #print("in between 896-960")
         card_id = 0x7DF
         pin_number=pin_number-896

    elif(pin_number > 960 and pin_number<1025):
         #print("in between 960-1024")
         card_id = 0x7D10
         pin_number=pin_number-960
##    print("pin_number",pin_number)     
    GV.msg = can.Message(arbitration_id= card_id, data=[0x02,pin_number,0x00,pin_status],extended_id=False)
    data=send_msg()
    if(data==0):
        #print("pin is high")
        dummy=can_rx_task()
        if(dummy[1]==0):# condition for data is write successfully and get responce from controller
            data_write_flag=0
        else:
            data_write_flag=1 
    else:
        data_write_flag=1
        print("IO error occured")
    return data_write_flag    

#---------------------------------------multiple pin read function---------------------------------------------------#        
def multiple_read():
    multiple_read_flag=0   #flag for card read error
    for i in range(GV.Card_counter):
        GV.msg = can.Message(arbitration_id=(0x7D0 | (i+1)), data=[0x03,0x00,0x00,0x00],extended_id=False)
        data=send_msg()
        if(data==0):
            rawdata=can_rx_task()
            if(rawdata[1]==0):# rawdata[0]is card data and rawdata[1]is data recive flag
                multiple_read_flag=0
                for position in range(64):
                    r=2**position
                    result=rawdata[0] & r
                    result=result>>position
                    array[position+(i*64)]=result
                # print("test point..")
            else:
                multiple_read_flag=1                
        else:
            multiple_read_flag=1
            print("IO error occured")
    return multiple_read_flag    
#----------------------------------------------------------------------------------------------------------------------------------#        
def IOclear_and_IOread(pin_number): 
    R1=single_write(pin_number,1)
    R2=multiple_read()
    R3=single_write(pin_number,0)
    return (R1 or R2 or R3)       
#---------------------------------------Analog pin read function---------------------------------------------------#    
def analog_read(pin_number):
    if (pin_number <= 64):
        # print("in between 1-64")
        card_id = 0x7D1
    elif (pin_number > 64 and pin_number < 129):
        # print("in between 64-128")
        card_id = 0x7D2
        pin_number = pin_number - 64
    elif(pin_number > 128 and pin_number<193):
         #print("in between 128-192")
        card_id = 0x7D3
        pin_number=pin_number-128

    elif(pin_number > 192 and pin_number<257):
         #print("in between 192-256")
        card_id = 0x7D4
        pin_number=pin_number-192     

    elif(pin_number > 256 and pin_number<321):
         #print("in between 256-320")
         card_id = 0x7D5
         pin_number=pin_number-256

    elif(pin_number > 320 and pin_number<385):
         #print("in between 320-384")
         card_id = 0x7D6
         pin_number=pin_number-320

    elif(pin_number > 384 and pin_number<449):
         #print("in between 384-448")
         card_id = 0x7D7
         pin_number=pin_number-384

    elif(pin_number > 448 and pin_number<513):
         #print("in between 448-512")
         card_id = 0x7D8
         pin_number=pin_number-448

    elif(pin_number > 512 and pin_number<577):
         #print("in between 512-576")
         card_id = 0x7D9
         pin_number=pin_number-512

    elif(pin_number > 576 and pin_number<641):
         #print("in between 576-640")
         card_id = 0x7DA
         pin_number=pin_number-576

    elif(pin_number > 640 and pin_number<705):
         #print("in between 640-704")
         card_id = 0x7DB
         pin_number=pin_number-640

    elif(pin_number > 704 and pin_number<769):
         #print("in between 704-768")
         card_id = 0x7DC
         pin_number=pin_number-704

    elif(pin_number > 768 and pin_number<833):
         #print("in between 768-832")
         card_id = 0x7DD
         pin_number=pin_number-768

    elif(pin_number > 832 and pin_number<897):
         #print("in between 832-896")
         card_id = 0x7DE
         pin_number=pin_number-832

    elif(pin_number > 896 and pin_number<961):
         #print("in between 896-960")
         card_id = 0x7DF
         pin_number=pin_number-896

    elif(pin_number > 960 and pin_number<1025):
         #print("in between 960-1024")
         card_id = 0x7D10
         pin_number=pin_number-960
    GV.msg = can.Message(arbitration_id = card_id, data=[0x06,pin_number,0x0A,0x00],extended_id=False)
    data = send_msg()
    if(data == 0):
        try:
            GV.message = GV.bus.recv(0.01)
            s=''
            for i in range(GV.message.dlc ):
                s +=  '{0:x} '.format(GV.message.data[i])
            #print((GV.message.data[2]<<8)|(GV.message.data[3]))
            return ((GV.message.data[2]<<8)|(GV.message.data[3]))
        except(AttributeError, IOError,IndexError, ValueError, TypeError):
            print("Error while reciving Data")
            return ('NONE')
#---------------------------------------All pin status---------------------------------------------------#
def can_rx_task():
    data_recive_flag=0 # flag for data recive error
    try:
        GV.message = GV.bus.recv(0.03)
        #print("test",GV.message)
        if(GV.message.arbitration_id==0x30):
            rawdata =(((GV.message.data[7]) << 56) + ((GV.message.data[6]) << 48)+ ((GV.message.data[5]) << 40) + ((GV.message.data[4]) << 32) + ((GV.message.data[3]) << 24)+((GV.message.data[2]) << 16) + ((GV.message.data[1]) << 8) + (GV.message.data[0]))
            data_recive_flag=0
        else:
            rawdata=0
            data_recive_flag=1
    except(AttributeError, IOError,IndexError, ValueError, TypeError):
        CAN_stop()
        time.sleep(1)
        CAN_start()
        rawdata=0
        data_recive_flag=1
        print("Error while reciving Data")
            
  
    return(rawdata,data_recive_flag)


####################################################################################   
##if __name__=='__main__':
##    CAN_configuration()
##    GV.Card_counter=card_status()
##    print("total_card", GV.Card_counter)
##    now=time.time()
####    Learn_Harness()
##    Self_Test()
##    current=time.time()
##    print("time",current-now)
##    card_init()
##    single_write(1,1)
##  
##    GV.msg = can.Message(arbitration_id= 0x7D1, data=[0x03,0x00,0x00,0x00],extended_id=False)
##    data=send_msg()
##    rawdata=can_rx_task()
##    print(rawdata)
##
##    IOclear_and_IOread(3)
##    print(array)
##    i=1
##    card_init()
##    while (1):
##        checkboard()
##        single_write(i,0)
##        i=i+1
##        if(i>64):
##            i=1
        
##        
##        time.sleep(0.4)
##    t =threading.Thread(target = can_rx_task, args=())
##    t.start()
##    single_write()
##    time.sleep(1)
##    single_read()
##    time.sleep(1)
    
        
##    time.sleep(1)
##    analog_read()
##    time.sleep(1)
    
##    time.sleep(1)
##    start=time.time()
##    single_write()
##    can_rx_task()
##    for i in range(10000):
##        single_write()
##        can_rx_task()
##    stop=time.time()
##    print("time diffrence   ",stop-start)
