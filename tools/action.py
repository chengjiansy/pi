
class Action(object):
    READY=0
    DOING=1
    DONE=2

    def __init__(self):
        self.state=self.READY
        pass

    def __del__(self):
        pass

    def SetReady(self):
        self.state=self.READY
        return 

    def SetDo(self):
        self.state=self.DOING
        return

    def SetDone(self):
        self.state=self.DONE
        return

    def GetIsReady(self):
        if self.state==0:
            return True
        return False

    def GetIsDoing(self):
        if self.state==self.DOING:
            return True
        return False

    def GetIsDone(self):
        if self.state==self.DONE:
            return True
        return False
    def WriteLog(self,value):
        print value

if __name__=="__main__":
    pass