# -*- coding: utf-8 -*-
import sys
import numpy as np

def turning(post,post_next):
    diff=post_next - post
    min_data=diff[0]
    min_index=0
    for i in range(len(diff)):
        value=abs(diff[i])
        if min_data>value:
            min_data=value
            min_index=i
    return min_data,min_index

if __name__=="__main__":
    post = np.arange(4).reshape(4)
    post_next = np.arange(4,8).reshape(4)
    min_data,min_index= turning(post,post_next)
    print min_data,min_index
