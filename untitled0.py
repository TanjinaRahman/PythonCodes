# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 18:25:47 2018

@author: Aspire
"""
import numpy as np

def DistFunc(x1,y1,x2,y2):
    p=float((x1-x2)**2)
    q=float((y1-y2)**2)
    s=float((p+q)**0.5)
    return s

x = np.array([3, 1, 1, 2, 1, 6, 6, 6, 5])
y = np.array([5, 4, 6, 6, 5, 8, 6, 7, 6])
i1=x[3]
j1=y[3]
for i in range(0,17):
        a=float((x[i]-i1)**2)
        d=float((y[i]-j1)**2)
        e=float((a+d)**0.5)
        print e