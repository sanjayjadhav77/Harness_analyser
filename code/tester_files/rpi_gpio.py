import RPi.GPIO as GPIO
import time
#--------------------------------Relay Initialization----------------------------------------------------#
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
Relay_1=4
Relay_2=24
vaccume_sense=18
GPIO.setup(Relay_1, GPIO.OUT)
GPIO.setup(Relay_2, GPIO.OUT)
GPIO.setup(vaccume_sense, GPIO.IN, pull_up_down = GPIO.PUD_UP)


while 1:
##    if(GPIO.input(vaccume_sense) == 0):
##        print("Button 2 pressed")
##    GPIO.output(Relay_1,GPIO.LOW)
##    time.sleep(1)
##    GPIO.output(Relay_1,GPIO.HIGH)
##    time.sleep(1)
##    GPIO.output(Relay_2,GPIO.LOW)
##    time.sleep(1)
    GPIO.output(Relay_2,GPIO.HIGH)
    time.sleep(1)
    

    
