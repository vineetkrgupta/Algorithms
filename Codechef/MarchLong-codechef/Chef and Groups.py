# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 12:05:10 2021

@author: vk779
"""

x = int(input())
for i in range(x):
    y = input()
    y=y+"0"
    print(y.count("10"))
#    temp=False
#    count=0
#    front,back=0,0
     
#    for j in range(len(y)):
#        if(y[j]=='1'):
#            front = j
#            break
#    for m in range(len(y)- 1,-1 , -1):
#        if(y[m]=='1'):
#            print("....",m)
#            back = min(m+1,len(y)-1)
#            break
#    #print()
#    print(y.count("10",front,back+1))
#    
#    
#    print(y[front:back+1])

    
#    print(front, back)
#    for j in range(front,back+1,1):
#        print(y[j],end="")
#        if(temp==True and y[j]=='0'):
#            count=1+count
#            temp=False
#        if(y[j]=='1'):
#            temp=True
#    print("jj",count)