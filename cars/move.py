# -*- coding:UTF-8 -*-
import dev as devs
import sys
sys.path.append("../tools");
sys.path.append("tools");
import time
import sys
from action import Action
import threading
class Move(Action):

    FORWARD=0
    REVERSE=1
    LEFT=2
    RIGHT=3
    LEFT_B=4
    RIGHT_B=5
    LEFT_P=6
    RIGHT_P=7

    def __init__(self,dev_):
        super(Move, self).__init__()
        self.dev=dev_
        dev=self.dev
        self.dev.setup(dev_.in_left_g,dev.OUT)
        self.dev.setup(dev_.in_left_b,dev.OUT)
        self.dev.setup(dev_.in_righ_g,dev.OUT)
        self.dev.setup(dev_.in_righ_b,dev.OUT)
    def __del__(self):
        self.clearup()

    in_left_g=12
    in_left_b=11
    in_righ_g=15
    in_righ_b=13
    
    in_dist_t = 16  
    in_dist_e = 18 
    in_trun   = 29
    def SetDo(self,dire,tf):
        sendDataThread=threading.Thread(target=self.Do, args=(dire,tf,))
        sendDataThread.start()
        return super(Move, self).SetDo()

    def Do(self,dire,tf):
        self.Todo(dire,tf)
        self.cleanup()
        return super(Move, self).SetDone()

    def Todo(self,dire,tf):
        if dire==self.FORWARD:
            self.forward(tf)
        elif dire==self.REVERSE:
            self.reverse(tf)
        elif dire==self.LEFT:
            self.left(tf)
        elif dire==self.RIGHT:
            self.right(tf)
        elif dire==self.LEFT_B:
            self.b_left(tf)
        elif dire==self.RIGHT_B:
            self.b_right(tf)
        elif dire==self.LEFT_P:
            self.p_left(tf)
        elif dire==self.RIGHT_P:
            self.p_right(tf)
        else :
            print "err dire\n"

        time.sleep(tf)  
        self.clearup()
    # 前进
    def forward(self,tf):
            dev=self.dev
            dev.output(dev.in_left_g,dev.HIGH)
            dev.output(dev.in_left_b,dev.LOW)
            dev.output(dev.in_righ_g,dev.HIGH)
            dev.output(dev.in_righ_b,dev.LOW)

    # 后退
    def reverse(self,tf):
            dev=self.dev
            dev.output(dev.in_left_g,dev.LOW)
            dev.output(dev.in_left_b,dev.HIGH)
            dev.output(dev.in_righ_g,dev.LOW)
            dev.output(dev.in_righ_b,dev.HIGH)

    # 左转弯
    def left(self,tf):
            dev=self.dev
            dev.output(dev.in_left_g,dev.LOW)
            dev.output(dev.in_left_b,dev.LOW)
            dev.output(dev.in_righ_g,dev.HIGH)
            dev.output(dev.in_righ_b,dev.LOW)

    # 右转弯
    def right(self,tf):
            dev=self.dev
            dev.output(dev.in_left_g,dev.HIGH)
            dev.output(dev.in_left_b,dev.LOW)
            dev.output(dev.in_righ_g,dev.LOW)
            dev.output(dev.in_righ_b,dev.LOW)

    # 后左转弯
    def b_left(self,tf):
            dev=self.dev
            dev.output(dev.in_left_g,dev.LOW)
            dev.output(dev.in_left_b,dev.HIGH)
            dev.output(dev.in_righ_g,dev.LOW)
            dev.output(dev.in_righ_b,dev.LOW)

    # 后右转弯
    def b_right(self,tf):
            dev=self.dev
            dev.output(dev.in_left_g,dev.LOW)
            dev.output(dev.in_left_b,dev.LOW)
            dev.output(dev.in_righ_g,dev.LOW)
            dev.output(dev.in_righ_b,dev.HIGH)

    # 原地左转
    def p_left(self,tf):
            dev=self.dev
            dev.output(dev.in_left_g,dev.LOW)
            dev.output(dev.in_left_b,dev.HIGH)
            dev.output(dev.in_righ_g,dev.HIGH)
            dev.output(dev.in_righ_b,dev.LOW)

    # 原地右转
    def p_right(self,tf):
            dev=self.dev
            dev.output(dev.in_left_g,dev.HIGH)
            dev.output(dev.in_left_b,dev.LOW)
            dev.output(dev.in_righ_g,dev.LOW)
            dev.output(dev.in_righ_b,dev.HIGH)

    def clearup(self):
            dev=self.dev
            dev.output(dev.in_left_g,dev.LOW)
            dev.output(dev.in_left_b,dev.LOW)
            dev.output(dev.in_righ_g,dev.LOW)
            dev.output(dev.in_righ_b,dev.LOW)
            #dev.cleanup()

    def help(self):
            print "FORWARD=0   "
            print "REVERSE=1   "
            print "LEFT=2      "
            print "RIGHT=3     "
            print "LEFT_B=4    "
            print "RIGHT_B=5   "
            print "LEFT_P=6    "
            print "RIGHT_P=7   "
            print "============"
if __name__ == '__main__':
        dd=devs.Dev()
        car=Move(dd)
        car.help()
        while True:
            key = raw_input("input:\n")
            print key
	    for i in range(len(key)):
		k=key[i]
                car.Todo(ord(k)-48,1)
            #if car.GetIsReady:
            #    car.SetDo(ord(key)-48,1)
            #elif car.GetIsDone:
            #    car.SetReady()

