# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '�� �'
#    __date__ = '2016/8/6'
#    __Desc__ = ����ת�������

import pyttsx
engine = pyttsx.init()
engine.say('hello world')
engine.say('��ã����')
engine.runAndWait()
# �ʶ�һ��
engine.endLoop()
