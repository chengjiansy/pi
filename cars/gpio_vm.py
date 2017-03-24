#!/usr/bin/python
# -*- coding: UTF-8 -*-

BOARD=0
BCM=1
IN=3
OUT=4
HIGH=5
LOW=6
class Pwm:
    def start(self,value):
        return 
    def ChangeDutyCycle(self,value):
        return 
    def stop(self):
        return 
def ToEnumString(value):
    if value==BOARD:return "BOARD"
    if value==BCM:return "BCM"
    if value==IN:return "IN"
    if value==OUT:return "OUT"
    if value==HIGH:return "HIGH"
    if value==LOW:return "LOW"

def WriteLog(value):
    #pass
    print value
def setmode(state):
   WriteLog("setmode:%s"%ToEnumString(state))
   return
def setwarnings(bvalue):
   WriteLog("setwarnings:%d"%bvalue)
   return 

def setup(channel,state):
   WriteLog("setup:(channel:%d,%s)"%(channel,ToEnumString(state)))
   return

def input(chanel):
   WriteLog("input:(channel:%d)"%chanel)
   return False
        
def output(channel,state):
   WriteLog("output:(channel:%d,%s)"%(channel,ToEnumString(state)))
   return

def PWM(channel,initial):
   WriteLog("input:(channel:%d,initial:%d)"%(channel,initial))
   pwm=Pwm()
   return pwm
def cleanup():
   WriteLog("cleanup:")
   return
   
if __name__ == "__main__":
   WriteLog('GPIO:')
   setmode(BOARD)
   setwarnings(False)
   setup(1)
   input(1)
   output(1,1)
   cleanup()
