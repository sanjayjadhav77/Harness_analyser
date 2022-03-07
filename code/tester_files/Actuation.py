import global_test_var as GV
import global_var
from main_new_Mdi import *
from global_files import*
import RPi.GPIO as GPIO
import sys
import time
'''--------------------------raspberry pi GPIO pin setup --------------------------- '''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
cutter_module= 19
Qmark_set =18
release=26
##Buzzer= 27
##vaccume_sense=13
pass_led=4
fail_led=24
Start_Button=20
Abort_Button=21
GPIO.setup(fail_led, GPIO.OUT)
GPIO.setup(pass_led, GPIO.OUT)
##GPIO.setup(Buzzer, GPIO.OUT)
GPIO.setup(cutter_module, GPIO.OUT)
GPIO.setup(Qmark_set, GPIO.OUT)
GPIO.setup(release, GPIO.OUT)
##GPIO.setup(vaccume_sense, GPIO.IN)
GPIO.setup(Start_Button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(Abort_Button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

'''--------------------------------------------------------------------------------------'''


def Release_on():
    #print("Release_on")
    GPIO.output(release, GPIO.HIGH)


def Release_off():
    #print("Release off")
    GPIO.output(release, GPIO.LOW)

def passled_on():
    print("led_on")
    GPIO.output(pass_led, GPIO.LOW)


def passled_off():
    print("led off")
    GPIO.output(pass_led, GPIO.HIGH)    
    

def Buzzer_set():
    print("Buzzer_set")
    GPIO.output(Buzzer, GPIO.HIGH)

def Buzzer_reset():
    GPIO.output(Buzzer, GPIO.LOW)
    
def Qmarkset():
    print("Qmarkset")
    GPIO.output(Qmark_set, GPIO.HIGH)


def Qmark_reset():
    GPIO.output(Qmark_set, GPIO.LOW)


def cutter_set():
    print("cutter_set")
    GPIO.output(cutter_module, GPIO.HIGH)


def cutter_reset():
    GPIO.output(cutter_module, GPIO.LOW)


def failled_on():
    print("led_on")
    GPIO.output(fail_led, GPIO.LOW)


def failled_off():
    print("led off")
    GPIO.output(fail_led, GPIO.HIGH)

def learn_key():
    if GPIO.input(vaccume_sense):
        status=1
    else:
        status=0
    return(status)

def Ent_button_press(event):
    if (GPIO.input(Start_Button)==1):
        if (global_var.state_machine == 4):
            if(GV.Estate==9 or GV.Estate==10):
                pass
            else:
                GV.Start_Event_flag=1
        else:
            pass
    else:
        print("enter button not press")

def Abort_button_press(event):
    if (GPIO.input(Abort_Button)==1):
        if (global_var.state_machine == 4):
            if(GV.Estate==9 or GV.Estate==10):
                pass
            else:
                GV.Abort_Event_flag=1
                GV.Abort_flag=1

        else:
            pass
    else:
        print("abort not press")

GPIO.add_event_detect(Abort_Button, edge=GPIO.RISING, callback=Abort_button_press, bouncetime=500)

GPIO.add_event_detect(Start_Button, edge=GPIO.RISING, callback=Ent_button_press, bouncetime=500)  

###--------------------------------------------------------------------------------------------------------------------------------  
# if __name__=='__main__':
#     print("fff")
#     while(1):
#         print("Abort=",GPIO.input(Abort_Button))
#         print("enter=",GPIO.input(Start_Button))
#         time.sleep(0.5)
# #    Qmarkset()
    


