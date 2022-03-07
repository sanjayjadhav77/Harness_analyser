from CAN_Bus import *
import time



def Resistance_test(Net1,Net2,Rval):
    print("----------------------------------------")
    Rmax=Rval+(0.20*Rval ) 
    Rmin=Rval-(0.20*Rval)
    single_write(Net1, 1)
    val=analog_read(Net2)
    voltage=(val*0.0008056640625)
    Dvoltage=(voltage*(22000+47000)/47000)
    print("Dvoltage",Dvoltage)
    x=((22000*4.88)/Dvoltage)-22000
    print("tolerance range",Rmax,Rmin)
    Resistance=x-500
    print("Resistance",Resistance)

    if(Resistance<Rmax and Resistance>Rmin ):
        print("Resistance test pass")
        return(1)
    else:
        print("Resistancee test fail")
        return(0)

    
def Diode_Orientation(Net1,Net2):
    single_write(Net1, 1)
    status=single_read(Net2)
    single_write(Net1, 0)

    single_write(Net2, 1)
    status1=single_read(Net1)
    single_write(Net1, 0)

    if(status==1 and status1==0 ):
        print("correct orienrtation")
        return(1)
    elif(status==0 and status1==1 ):
        print("wrong orientation ")
        return(2)
    elif(status==1 and status1==1 ):
        print("Short Diode")
        return(2)
    else:
        return(0)
    
def Diode_forward_voltage(Net1,Net2,Vf):
    vfmax=Vf+(0.25*Vf ) 
    vfmin=Vf-(0.25*Vf)
    
    single_write(Net1, 1)
    val=analog_read(Net2)
    voltage=(val*0.000805)
    Dvoltage=(voltage*(22000+46000))/46000
    #single_write(Net1, 0)
    Mesure_Vf=4.96-Dvoltage
    print("Forward voltage",Mesure_Vf)
    print("Forward voltage range",vfmax,vfmin)

    if(Mesure_Vf<vfmax and Mesure_Vf>vfmin ):
        print("Forward voltage test pass")
        return(1)
    else:
        print("Forward voltage test fail")
        return(0)  

def capacitor_test():
    print("Capacitor")

def voltage_test(pin_no):
    val=analog_read(pin_no)
    voltage=(val*0.000805)
    Dvoltage=(voltage*(22000+46000))/46000
    print("Dvoltage",Dvoltage)

def Sensor():
    print("sensor input")
#-----------------------------------------------------------------------------------------------------
if __name__=='__main__':
    CAN_configuration()
    #Diode_Orientation(1,8)
##    Diode_forward_voltage(1,8,0.7)
##    voltage_test(8)
    while 1:
        Resistance_test(1,8,400)
        time.sleep(1)
    
#-----------------------------------------------------------------------------------------------------
