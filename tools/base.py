class Base(object):
    enable=False

    def __init__(self):
        return 

    def SetLog(self,value):
        self.enable=value
        return 

    def WriteLog(self,value):
        if self.enable==True:
            print value
        return 


