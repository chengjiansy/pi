#!/usr/bin/env python    
#-*-coding:utf-8 -*-
#舵机  
import sys
sys.path.append("../tools");
sys.path.append("tools");
import dev as devs
import time  
import signal  
import atexit  
import thread
import threading
from action import Action

class Steering(Action):
    def __init__(self,dev_):
        super(Steering, self).__init__()
        self.dev=dev_
        dev=self.dev
        dev.setup(dev_.in_trun,dev.OUT)
        self.p = dev.PWM(dev.in_trun,50) #50HZ  

    def SetDo(self,value):
        sendDataThread=threading.Thread(target=self.Do, args=(value,))
        sendDataThread.start()
        return super(Steering, self).SetDo()

    def Do(self,value):
        Todo(value)
        return super(Steering, self).SetDone()
    def Todo(self,value):
        dev=self.dev
        p=self.p
        p.start(0) 
        time.sleep(2)   
        p.ChangeDutyCycle(2.5 + 10 * value / 180) #设置转动角度  
        time.sleep(0.02)                      #等该20ms周期结束  
        p.ChangeDutyCycle(0)                  #归零信号  
        time.sleep(0.2)  
        p.stop()

if __name__ == '__main__':
        dev=devs.Dev()
        turning=Steering(dev)
        turning.SetDo(20)
        print ("ok\n")
