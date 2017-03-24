#-*-coding:utf-8 -*-
import sys
sys.path.append("../tools");
#import gpio_vm as GPIO
import RPi.GPIO as GPIO
class Dev(object):
    #tt
    BOARD=0
    BCM=0
    IN=0
    OUT=0
    HIGH=0
    LOW=0

    in_left_g=11
    in_left_b=12
    in_righ_g=13
    in_righ_b=15
    
    in_dist_t = 16  
    in_dist_e = 18

    in_trun   = 29

    in_discover_in=0 
    in_discover_out=0 
    def __init__(self):
        self.BOARD=GPIO.BOARD
        self.BCM=GPIO.BCM
        self.IN=GPIO.IN
        self.OUT=GPIO.OUT
        self.HIGH=GPIO.HIGH
        self.LOW=GPIO.LOW

        GPIO.setmode(GPIO.BOARD)
        return 
    def __del__(self):
        GPIO.cleanup()

    def setmode(self,mode):
        GPIO.setmode(mode)
        return
    
    def setwarnings(self,bvalue):
        GPIO.setwarnings(bvalue)
        return 

    def PWM(self,channel,initial):
        return GPIO.PWM(channel,initial)
        
    def setup(self,channel,initial=GPIO.HIGH):
       # print channel,initial
        return GPIO.setup(channel,initial)
        

    def input(self,channel):
        return GPIO.input(channel)

    def output(self,channel,state):
        return GPIO.output(channel,state)
        

    def cleanup(self):
        GPIO.cleanup()
        return
   
if __name__=="__main__":
    
    dev=Dev()
    dev.PWM(dev.in_trun,50)
    dev.setmode(GPIO.BOARD)
    dev.setwarnings(False)
    dev.setup(1)
    dev.output(1,1)
    dev.cleanup()


        
