import sys

class Log(object):
    """description of class"""
    def __init__(self,filename):
        self.file=file(filename,'w+')

    def __del__(self):
        self.file.close()

    def write(self,value):
        self.file.write(value)
        return

    def writelines(self,value):
        self.file.writelines(value)
        return

if __name__=="__main__":
    log=Log("1.txt")
    log.writelines("hello");
    #li=["hello world\n","hello china\n"]
    #log.writelines(li)
    #print "ok"




