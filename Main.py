#!/bin/python3 
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import PWMOutputDevice
from picamera import PiCamera
GPIO.setwarnings(False)


#Motor Definations

RMF=17 #Front motor Right Forward 
RMR=18 #Front motor Right Reverse
LMF=22 #Front motor Left Forward
LMR=23 #Front motor Left Reverse
PWMR=16 #Rear Motor Right Forward
PWML=18 #Rear Motor Right Reverse

#SERVO Intializations


#PAN CAMERA INTIALIZATION
GPIO.setup(20,GPIO.OUT)
pan=GPIO.PWM(20,50)

#TILT CAMERA INTIALIZATION
GPIO.setup(26,GPIO.OUT)
tilt=GPIO.PWM(26,50)


#Motor Intializations

#Right Motor Forward
GPIO.setup(RMF,GPIO.OUT)
GPIO.output(RMF,GPIO.LOW)

#Right Motor Reverse 
GPIO.setup(RMR,GPIO.OUT)
GPIO.output(RMR,GPIO.LOW)

#Left Motor Forward
GPIO.setup(LMF,GPIO.OUT)
GPIO.output(LMF,GPIO.LOW)

#Left Motor Reverse
GPIO.setup(LMR,GPIO.OUT)
GPIO.output(LMR,GPIO.LOW)

RF = PWMOutputDevice(RMF, True, 0, 1000)
RR = PWMOutputDevice(RMR, True, 0, 1000)
 
LR = PWMOutputDevice(LMR, True, 0, 1000)
LF = PWMOutputDevice(LMF, True, 0, 1000)

camera=PiCamera()

speed=0.20

def drivemotor(motornumber,speed):
    
    #GPIO.setmode(GPIO.BOARD)
    motornumber.value=speed
    return
   

def stopmotor(motornumber):
    
    #GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motornumber,GPIO.OUT)
    #print ("Turning "+ 'motornumber'+ " on")
    GPIO.output(motornumber,GPIO.LOW)
   
def stoprobot():
    
    RF.value=0
    RR.value=0
    LF.value=0
    LR.value=0
    
def  goingforward():
    
    drivemotor(RF,speed)
    drivemotor(LF,speed)
    #stopmotor(RMR)
    #stopmotor(LMR)
    
def goingbackward():
    
    drivemotor(RR,speed)
    drivemotor(LR,speed)
    #stopmotor()
    #stopmotor(LMF)
    
def goingright():
    
    drivemotor(RF,speed)
    drivemotor(LR,speed)
    #stopmotor(RMF)
    #stopmotor(LMR)
    
def goingleft():
    
    drivemotor(RR,speed)
    drivemotor(LF,speed)
    #stopmotor(RMR)
    #stopmotor(LMF)
   
import evdev

device = evdev.InputDevice('/dev/input/event0')
#device /dev/input/event1, name "USB Keyboard", phys "usb-0000:00:12.1-2/input0"
#while

#for event in device.read_loop():
    

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        
                if evdev.events.KeyEvent(event).keycode=='KEY_Z':
                    if speed<0.9:
                        speed=speed+0.1
                
                elif evdev.events.KeyEvent(event).keycode=='KEY_X':
                    if speed>0.2:
                        speed=speed-0.1
                
                elif evdev.events.KeyEvent(event).keycode=='KEY_UP':
                    #if evdev.events.KeyEvent(event).key_hold==2:
                        goingforward()
                        sleep(0.05)
                        stoprobot()
        
                    #condition to move backward with down arrow
                elif evdev.events.KeyEvent(event).keycode=='KEY_DOWN':
                    if evdev.events.KeyEvent(event).key_hold==2:
                        goingbackward()
                        sleep(0.05)
                        stoprobot()
        
                    #condition to move right with right arrow
                elif evdev.events.KeyEvent(event).keycode=='KEY_RIGHT':
                    if evdev.events.KeyEvent(event).key_hold==2:
                        goingright()
                        sleep(0.05)
                        stoprobot()
                #condition to move left with left arrow
                elif evdev.events.KeyEvent(event).keycode=='KEY_LEFT':
                    if evdev.events.KeyEvent(event).key_hold==2:
                        goingleft()
                        sleep(0.05) 
                        stoprobot()
                #Condition to TSart Camera Preview
                elif evdev.events.KeyEvent(event).keycode=='KEY_V':
            
                        camera.start_preview()
                #Condition to Stop Preview
                elif evdev.events.KeyEvent(event).keycode=='KEY_B':
            
                        camera.stop_preview()
                
                #Condition to emergency Brake
                elif evdev.events.KeyEvent(event).keycode=='KEY_SPACE':
            
                        stoprobot()
                #Condition to PAN LEFT
                elif evdev.events.KeyEvent(event).keycode=='KEY_A':
                    if evdev.events.KeyEvent(event).key_hold==2:
                         pan.start(2.3)
                         sleep(0.05) 
                         pan.ChangeDutyCycle(0)
                     
                #Condition to PAN RIGHT 
                elif evdev.events.KeyEvent(event).keycode=='KEY_D':
                    if evdev.events.KeyEvent(event).key_hold==2:
                        pan.start(2.1)
                        sleep(0.05) 
                        pan.ChangeDutyCycle(0)
                        
                #Condition to TILT UP
                elif evdev.events.KeyEvent(event).keycode=='KEY_W':
                    if evdev.events.KeyEvent(event).key_hold==2:
                        tilt.start(20)
                        sleep(0.05) 
                        tilt.ChangeDutyCycle(0)
                     
                #Condition to TILT DOWN
                elif evdev.events.KeyEvent(event).keycode=='KEY_S':
                    if evdev.events.KeyEvent(event).key_hold==2:
                        tilt.start(12.8)
                        sleep(0.05) 
                        tilt.ChangeDutyCycle(0)

                               
GPIO.cleanup()
    


