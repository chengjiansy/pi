#!/usr/bin/python  
#-*- coding: utf-8 -*-  
import sys
sys.path.append("../tools");
import time  
import dev as devs
from action import Action
import threading
class Distance(Action):
    value=0
    def __init__(self,dev_):
        super(Distance, self).__init__()
        self.dev=dev_
        dev=self.dev
    
    def SetDo(self):
        sendDataThread=threading.Thread(target=self.Do)
        sendDataThread.start()
        return super(Distance, self).SetDo()

    def Do(self):
        self.value=self.GetDistance()
        return super(Distance, self).SetDone()

    def GetValue(self):
        return self.value

    def GetDistance(self):  #测距函数
        dev=self.dev
        dev.output(dev.in_dist_t, False) #设置trigger为低电平  
        time.sleep(0.5)  
        dev.output(dev.in_dist_t, True) #设置trigger为高电平  
        time.sleep(0.00001)  
        dev.output(dev.in_dist_t, False)  
        start = time.time()  #记录发射超声波开始时间  
        stop=start

        while dev.input(dev.in_dist_e)==0:
            start = time.time()
            
        while dev.input(dev.in_dist_e)==1:
            stop = time.time()
          
        elapsed = stop-start   #计算一共花费多长时间  
        distance = elapsed * 34300  #计算距离，就是时间乘以声速  
        distance = distance / 2  #除以2得到一次的距离而不是来回的距离  
        return distance
    
if __name__ == '__main__':
    dev=devs.Dev()
    distance=Distance(dev)
    distance.GetDistance()

