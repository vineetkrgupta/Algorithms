# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 21:55:09 2021

@author: vk779
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 21:21:40 2021

@author: vk779
"""

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
    #print(y)
    a=0
    b=0
    maxo=0
    z=len(y)
    for x in range(z):

        if(y[x]=='0'):
            a=a+2**(z-x-1)
            b=b+2**(z-x-1)

            sums= a*b

        else:
            a1=a+2**(z-x-1)
            a2=a

            
            b1=b+2**(z-x-1)
            
            b2=b

     
            if(a1*b2 >= a2*b1):
               
                sums=a1*b2
                a=a1

            else:
                sums=a2*b1
                b=b1
          
        maxo = max(sums,maxo)

    print(maxo)

            
    