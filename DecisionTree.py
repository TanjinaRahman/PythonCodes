# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 06:15:44 2018

@author: Aspire
"""
#A=age B=weight C=plays football
import numpy as np
A = np.array([4.8,5,5,5.2,5.2,4.7,4.8,5.4,7,6.4,6.9,5.5,6.5,5.7,6.3,4.9])
B = np.array([3.4,3,3.4,3.5,3.4,3.2,3.1,3.4,3.2,3.2,3.1,2.3,2.8,2.8,3.3,2.4])
C = np.array([1.9,1.6,1.6,1.5,1.4,1.6,1.6,1.5,4.7,4.7,4.9,4,4.6,4.5,4.7,3.3])
E = np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
#data(iris)
c = len(E)
#print c
def find_gini(c,c1,c2,c3,c4,f1,f2):
    gini1=1-((c1/f1)**2+(c2/f1)**2)
    gini2=1-((c3/f2)**2+(c4/f2)**2)
    gini=((f1/c)*gini1)+((f2/c)*gini2)
    #return gini1,gini2,gini
    return gini

#print find_gini(float(16),float(5),float(7),float(3),float(1),float(12),float(4))

def group(Gr,P,v):
    f1=0.0
    f2=0.0
    c1=0.0
    c2=0.0
    c3=0.0
    c4=0.0
    for i in range(0,16):
             if(Gr[i]>=v):
                 f1=f1+1
                 if(P[i] == 1):
                     c1=c1+1
                 else:
                     c2=c2+1
             else:
                    f2=f2+1
                    if(P[i] == 1):
                        c3=c3+1
                    else:
                        c4=c4+1
            
            
       
    #return f1,f2,c1,c2,c3,c4
    return find_gini(c,c1,c2,c3,c4,f1,f2)
    

gA= group(A,E,5)
gB= group(B,E,3)
gC= group(C,E,4.2)
li=[gA,gB,gC]
li.sort()
print li
for i in li:
    if(i==gA):
        print "A"
    elif(i==gB):
        print "B"
    else:
       print "C"
        

