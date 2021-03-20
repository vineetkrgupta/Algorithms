# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 00:14:37 2021

@author: vk779
"""

T = int(input())
for i in range(T):
    n = int(input())
    temp = (n * (n+1))/2
    a = list(map(int,input().split(" ")))
    
    a.sort()
    #print(a)
    s = sum(a)
    #print(s ,temp)
    s = temp-s
    #print(s ,temp)
    j = 1 
    count =0
    for item in a: 
        if item > j:
            print("Second")
            count = 1
            break
        j = j + 1
    if count ==0 :
        if(s <= 0 or s%2 == 0): # odd even odd wala 
            print("Second")
        else:
            print("First")