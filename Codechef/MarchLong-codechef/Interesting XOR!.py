# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:30:41 2021

@author: vk779
"""

x = int(input())
for i in range(x):
    y = input()
    y= bin(int(y))

    y=str(y)[2:]
    print(y)
    a=list(str(10**(len(y)-1)))
    b=list(str(10**(len(y)-1)))
    a[0]='0'
    b[0]='0'
    
    print(a)
    maxo=0
    for x in range(len(y)-1,-1, -1):
        if(y[x]=='0'):
            a[x]=='1'
            b[x]=='1'
        else:
            a1=a
            a1[x]='1'
            a1=''.join(a1)
            
            a2=a
            a2[x]='0'
            a2=''.join(a2)
            
            b1=b
            b1[x]='1'
            b1=''.join(b1)
            
            b2=b
            b2[x]='0'
            b2=''.join(b2)
            
            print(int(a1,2)*int(b2,2), int(a2,2)*int(b1,2))
            print(a1,b2, a2, b1 , end=".....")
            print(int(a1,2) ,int(b2,2), int(a2,2) ,int(b1,2))
     
            if(int(a1,2)*int(b2,2) >= int(a2,2)*int(b1,2)):
               
                sums=int(a1,2)*int(b2,2)
                a[x]='1'
                b[x]='0'
            else:
                sums=int(a2,2)*int(b1,2)
                a[x]='0'
                b[x]='1'
          
            maxo = max(sums,maxo)
    print(maxo)
    print(a,b)
            
    