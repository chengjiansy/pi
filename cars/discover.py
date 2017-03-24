import sys
sys.path.append("../tools");
sys.path.append("tools");
import time  
import dev as devs
from action import Action
import threading

class Discover(Action):
    GPIO_IN=12  
    GPIO_OUT=8  
    value=0
    def __init__(self,dev_):
        super(Discover, self).__init__()
        self.dev=dev_
        dev=self.dev
        dev.setup(dev_.in_discover_in,dev.IN)
        dev.setup(dev_.in_discover_out,dev.OUT)

    def SetDo(self):
        sendDataThread=threading.Thread(target=self.Do)
        sendDataThread.start()
        return super(Discover, self).SetDo()

    def Do(self):
        self.value=self.ToDo()
        return super(Discover, self).SetDone()

    def GetValue(self):
        return self.value

    def ToDo(self):  
        dev=self.dev
        dev.output(dev.in_discover_out,dev.HIGH)  
        time.sleep(0.5)  
        dev.output(dev.in_discover_out,dev.LOW)  
        time.sleep(2)  
        inValue=dev.input(dev.in_discover_in) 
        return inValue

    
if __name__ == '__main__':
    dev=devs.Dev()
    distance=Discover(dev)
    distance.ToDo()