# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 15:44:21 2021

@author: vk779
"""


    
y = int(input())
for i in range(y):
    x =list(map(int,input().split()) )
    n=x[0]
    e=x[1]
    h=x[2]
    a=x[3]
    b=x[4]
    c=x[5]
    sup = -1
    possible= False
    count =0
    if(a>=b>=c):
        ff = 0
    elif(a>c>b):
        ff = 1
    elif(b>c>a):
        ff = 2
    elif(b>a>c):
        ff = 3
    elif(c>a>b):
        ff = 4 
    elif(c>b>a):
        ff =5 
    for j in range(n+1):
        for k in range(n+1):
            
            if(j+k>n):
                break
            
            l=n-j-k
           # print(j,k,l)
            if(j+k+l==n):
                if(ff ==0 ):
                    ja , ka , la =j , k , l
                elif(ff ==1):
                    ja , ka , la =j , l , k
                elif(ff ==2 ):
                    ja , ka , la =k , l , j
                elif(ff == 3):
                    ja , ka , la =k , j , l
                elif(ff == 4):
                    ja , ka , la =l , j , k
                elif(ff == 5):
                    ja , ka , la =l , k , j
                egg = e - (2*ja + la)
                choco = h - (3*ka + la)
                if(choco >= 0 and egg >= 0):
                    m= ja*a + b*ka+ la*c
                    print(ja,ka,la, m)
                    if(possible == False):
                        sup= m
                        possible = True    
                        
                        #break
                    else:
                        sup= min(sup,m)
                    count =count + 1

        #print(count)
        if(count > min(100, n)):
           break
                    
                    
#                    else:
#                        sup = min(m, sup)
#                    print(ja,ka,la, m)
    print(sup)