from action import Action
import time
import threading
class timerEx(Action):
    def __init__(self):
        return

    def SetDo(self,value):
        t = threading.Timer(value, self.SetDone).start()
        return  Action.SetDo(self)

    def SetDone(self):
        return Action.SetDone(self)

if __name__=="__main__":
    t=timerEx()
    t.SetDo(1)
    print 'done'




