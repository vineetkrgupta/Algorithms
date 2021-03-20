# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:48:39 2021

@author: vk779
"""



def cakeme(e,h,j,k,l , a , b ,c):
    egg = e - (2*j + l)
    choco = h - (3*k + l)
    if(choco >= 0 and egg >= 0):
        m= j*a + b*k+ l*c
        #print(m , egg, choco)
        return (m)
    
    else:
        #print(2**10 , egg, choco)
        return 2**100
    
y = int(input())
for i in range(y):
    x =list(map(int,input().split(" ")) )
    n=x[0]
    e=x[1]
    h=x[2]
    a=x[3]
    b=x[4]
    c=x[5]
    
    #best=0
    sup = 2**100
    if(n*2 > e+h):
        print("-1")
        continue
    else:
        if(a<b and a< c):
            #print("a")
            sup = cakeme(e,h,n,0,0,a,b,c)
        elif(b<a and b< c):
            #print("b")
            sup = cakeme(e,h,0,n,0,a,b,c)
        elif(c<a and c< b):
            #print("c")
            sup = cakeme(e,h,0,0,n,a,b,c)
#    
        
#    print(cakeme(e,h,0,0,n,a,b,c))
#    print(sup)
    
    if(sup == 2**100):
        for j in range(n+1):
            for k in range(n+1):
                if(j+k>n):
                    #print(j,k)
                    break
                #for l in range(n+1):
               # print(j,k,n-j-k)
                l=n-j-k
                if(j+k+l==n):
                    
                    sup = min( sup, cakeme(e , h , j , k , l , a , b , c ))
                #print(j, k , l , end =" ----")
    if(sup == 2**100):
        print("-1")
    else:
        print(sup)

            
            
            