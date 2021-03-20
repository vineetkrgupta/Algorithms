# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:41:03 2021

@author: vk779
"""


x =list(map(int,input().split(" ")) )
y = max(list(map(int,input().split(" ")) )) + x[2]
print("Yes") if y >= x[1] else print("No")