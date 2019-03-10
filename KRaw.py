# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:18:59 2018

@author: Aspire
"""

def DistFunc(x1,y1,x2,y2):
    p=float((x1-x2)**2)
    q=float((y1-y2)**2)
    r=float((p+q)**0.5)
    return r
group=[0,0,0,0,0,0]
Xcor =[0,20,40,60,800,1000]
Ycor=[1,0,1,10,100,567]
initialX1=Xcor[3]
initialY1=Ycor[3]
nPoint=6

initialX2=Xcor[1]
initialY2=Ycor[1]



while(1):
    for i in range(0,5):
        a=initialX1
        b=initialY1
        c=initialX2
        d=initialY2

        d1=DistFunc(initialX1 ,initialY1,Xcor[i],Ycor[i])
        d2=DistFunc(initialX2 ,initialY2,Xcor[i],Ycor[i])
        if d1<d2:
            group[i]=1
        else:
            group[i]=2
        sumx1=0
        sumy1=0
        count1=0
        count2=0
        sumx2=0
        sumy2=0
    for i in range(0,5):
        if group[i]==1:
            sumx1=sumx1+Xcor[i]
            sumy1=sumy1+Ycor[i]
            count1=count1+1

        else:
            sumx2=sumx2+Xcor[i]
            sumy1=sumy2+Ycor[i]
            count2=count2+1
    initialX1=sumx1/count1
    initialY1=sumy1/count1
    initialX2=sumx2/count2
    initialY2=sumy2/count2
    if a-initialX1<0.01 and b-initialY1<0.1 and c-initialX2<0.1 and d-initialY2<0.1:
        break

print("Group1 co-ordinates:\n")
for i in range(0,5):
    if(group[i]==1):
        print("({},{})".format(Xcor[i], Ycor[i]))

print("Group2 co-ordinates:\n")
for i in range(0,5):
    if(group[i]==2):
        print("({},{})".format(Xcor[i], Ycor[i]))


