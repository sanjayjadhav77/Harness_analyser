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
GPIO.setup(vaccume_sense, GPIO.IN)
GV.ConnPresent=0
GV.leakage = [[1, 1],[3, 14], [4, 21]]
GV.switch = [[1, 3], [2, 9], [3, 16], [4, 23]]
GV.led = [[1, 2], [3, 15], [4, 22]]

def Frl_on():
     single_write(64,1)
def Frl_off():
     single_write(64,0)

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

##     print(GV.switch_status)                             

def Leak_Test():
     waitTime=3
     x=len(GV.switch)
     y=0
     
     while(x!=y):
          
          Connector_Availability()
##          print("Y.............",y)
          if(GV.switch_status[y][1]==1):
               print("Connector " +str(GV.switch_status[y][0])+ " present")
               z=list((np.zeros(len(GV.leakage),dtype='i')))
               for j in range(len(GV.leakage)):
                    
                    if(GV.switch_status[y][0] in GV.leakage[j]):

                         single_write(GV.leakage[j][1],1)
                         single_write(GV.led[j][1],1)
                         Frl_on()
                         
                         now=time.time()
                         print("Sense",GPIO.input(vaccume_sense))
                         while (GPIO.input(vaccume_sense)==0 and (time.time()-now)<waitTime):
                              time.sleep(0.06) #save the cpu from running at 100%
                         if(GPIO.input(vaccume_sense)==1):
                              Frl_off()
                              single_write(GV.leakage[j][1],0)
                              single_write(GV.led[j][1],0)
                              print("Leak Test pass")
                              time.sleep(0.5)
                              y+=1
                              break

                         else:
                              
                              Frl_off()
                              GV.ConnPresent=0
                              single_write(GV.leakage[j][1],0)
                              single_write(GV.led[j][1],0)
                              print("Leak Test Fail")
                              time.sleep(0.5)
                              break
                         z[j]=0
                    else:
                         z[j]=1

##               print("Z......",z)
               if(z.count(z[0]) == len(z)) :
                    if (z[0]==1):
                         y+=1
                         print("Leak Test Group"+str(GV.switch_status[y-1][0])+" Absent")
                         
          else:
               
               print("Connector "+ str(GV.switch_status[y][0])+" Absent")


   
    

# if __name__=='__main__':
#     CAN_configuration()
# ##    single_write(2,0)
# ##    single_write(22,0)
# ##    single_write(15,0)
# ##    single_write(8,0)
# ##    Leak_Test()
#     while True:
#          Leak_Test()
##         Connector_Availability()

     
