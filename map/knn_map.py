# -*- coding: utf-8 -*-
import sys
import string
from numpy import *
import operator

##给出训练数据以及对应的类别
def createDataSet():

    filename='map_training.txt'
    fileIn = open(filename)  
    data = loadtxt('map_training.txt')
    line_len=len(data)
    group = zeros((line_len,4))
    labels =zeros((line_len))
    directions =zeros((line_len))
    
    for i in range(0,line_len):
        print data[i]
        group[i,0]=data[i,0]
        group[i,1]=data[i,1]
        group[i,2]=data[i,2]
        group[i,3]=data[i,3]
        directions[i]=data[i,4]
        labels[i]=data[i,5]

    return group,labels,directions

###通过KNN进行分类
def classify(input,dataSet,label,k):
    dataSize = dataSet.shape[0]
    ####计算欧式距离
    diff = tile(input,(dataSize,1)) - dataSet
    sqdiff = diff ** 2
    squareDist = sum(sqdiff,axis = 1)###行向量分别相加，从而得到新的一个行向量
    dist = squareDist ** 0.5
    
    ##对距离进行排序
    sortedDistIndex = argsort(dist)##argsort()根据元素的值从大到小对元素进行排序，返回下标

    classCount={}
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        ###对选取的K个样本所属的类别个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    ###选取出现的类别次数最多的类别
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key

    return classes
if __name__=="__main__":
    
    sys.path.append("...文件路径...")
    dataSet,labels,directions = createDataSet()
    print dataSet,labels,directions 
    input = array([3,4,7,1])
    K = 1
    output = classify(input,dataSet,labels,K)
    
    print u'测试数据为:',input,u"分类结果为：",output
