import RPi.GPIO as GPIO
import time
import numpy as np
import global_test_var as GV
# from HDM import *
##from  Sql_db import *
from CAN_Bus import *
'''--------------------------raspberry pi GPIO pin setup --------------------------- '''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
vaccume_sense=13
frl_pin=23
GPIO.setup(frl_pin, GPIO.OUT)
GPIO.setup(vaccume_sense, GPIO.IN)
GPIO.setup(vaccume_sense, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def Leak_pin_test():
     if(GPIO.input(vaccume_sense)==1):
          print("Done-----")
          return 1
     else:
          print("testing")
          return 0


def Frl_on():
     GPIO.output(frl_pin, 1)

def Frl_off():
     GPIO.output(frl_pin, 0)


def Connector_Availability():
     GV.switch_status=[]
     for i in range (len(GV.switch)):
          
          Switch_status=single_read(GV.switch[i][1])
          x=[GV.switch[i][0],Switch_status]
          GV.switch_status.append(x)
     for j in range(len(GV.switch_status)):
          for k in range(len(GV.led)):            
               if(GV.switch_status[j][0] == GV.led[k][0]):
                    if(GV.switch_status[j][1]==0):
                         single_write(GV.led[k][1],1)
                    else:
                         single_write(GV.led[k][1],0)

     print(GV.switch_status)
     print("GV.switch",GV.switch)                             

def Leakage_Test():                        
     waitTime=3
     x=len(GV.switch)
     GV.Stop_Leakage=0
     # GV.leakage=[]
     # GV.led=[[4,57],[5,62]]
     while(x!=GV.Stop_Leakage and GV.Abort_flag==0):
          
          Connector_Availability()
##          print("Y.............",y)

          if(GV.switch_status[GV.Stop_Leakage][1]==1):
               print("Connector " +str(GV.switch_status[GV.Stop_Leakage][0])+ " present")
               GV.Display_Message=("Leakage Test " +str(GV.switch_status[GV.Stop_Leakage][0])+ " Start")
               GV.data_delivered=13
               GV.message_color=1
               
               z=list((np.zeros(len(GV.leakage),dtype='i')))
               # if(len(GV.leakage)!=0):
               #      z[0]=1
               for j in range(len(GV.leakage)):
                    
                    if(GV.switch_status[GV.Stop_Leakage][0] in GV.leakage[j]):
                         # z[j]=0

                         single_write(GV.leakage[j][1],1)
                         try:
                              single_write(GV.led1[j][1],1)
                         except(IndexError):
                              print("Led Pin Not Present")
                         Frl_on()
                         time.sleep(1)
                         now=time.time()
                         print("Sense",GPIO.input(vaccume_sense))
                         time.sleep(1)
                         while (((GPIO.input(vaccume_sense)==0 and (time.time()-now)<waitTime)) and GV.Abort_flag==0):
                              time.sleep(0.06) #save the cpu from running at 100%
                         if(GPIO.input(vaccume_sense)==1):
                              Frl_off()
                              single_write(GV.leakage[j][1],0)
                              try:
                                   single_write(GV.led1[j][1],0)
                              except(IndexError):
                                   print("Led Pin Not Present")
                              print("Leak Test pass")
                              GV.Display_Message=("Leak Test "+ str(GV.switch_status[GV.Stop_Leakage][0])+" pass")
                              time.sleep(0.5)
                              GV.Stop_Leakage+=1
                              GV.message_color=3
                              break

                         else:
                              
                              Frl_off()
                              GV.ConnPresent=0
                              single_write(GV.leakage[j][1],0)
                              single_write(GV.led1[j][1],0)
                              # print("Leak Test Fail",GV.Stop_Leakage,x)
                              # print("GV.switch_status",GV.switch_status)
                              try:
                                   GV.Display_Message=("Leak Test "+ str(GV.switch_status[GV.Stop_Leakage][0])+" fail")
                                   GV.message_color=2
                              except(IndexError):
                                   print("Index Out of bound")
                                   

                              time.sleep(0.5)
                              break
                         z[j]=0
                    else:
                         z[j]=1
               
               if(len(z)!=0):
                    if(z.count(z[0]) == len(z)) :
                         if (z[0]==1):
                              GV.Stop_Leakage+=1
                              print("Leak Test Group"+str(GV.switch_status[GV.Stop_Leakage-1][0])+" Absent")
               else:
                    GV.Stop_Leakage+=1

          else:
               GV.Display_Message=("Connector "+ str(GV.switch_status[GV.Stop_Leakage][0])+" Absent")
               print("Connector "+ str(GV.switch_status[GV.Stop_Leakage][0])+" Absent")
               GV.data_delivered=13


     print("Out From while.")
     if(GV.Abort_flag==1):
          GV.Abort_flag=0
          
          # GV.Fo_test_Flag=0
          GV.Estate=0
          print("exit")
     else:
          GV.Estate=4
        
    

# if __name__=='__main__':
    
# ##    CAN_configuration()
# ##    single_write(2,0)
# ##    single_write(22,0)
# ##    single_write(15,0)
# ##    single_write(8,0)
# ##    Leak_Test()
#    while True:
#      Frl_on()
#      time.sleep(1)
#      Frl_off()
#      time.sleep(1)
##         Leak_Test()
##         Connector_Availability()

     
