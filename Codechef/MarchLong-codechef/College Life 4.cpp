#include<iostream>
#include<stdlib.h>
#include<stdio.h>
//#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;


    cin >> t;
    
    int x[6];
    
    int n, e, h , a, b , c ,l , egg , choco , sup;
    int count = 0, temp = 0;
    bool possible = false;
    while(t > 0){
        sup = -1;
        for (int i = 0; i < 6; i++)
        {
            cin >>x[i];
        }
        n=x[0];
        e=x[1];
        h=x[2];
        a=x[3];
        b=x[4];
        c=x[5];

        for( int j=0 ; j<(n+1); j++)
        for(int k=0 ; k<(n+1); k++)
        {
            if(j+k>n){
                break;
            }
                
            l = n-j-k;
            egg = e - (2*j + l);
            choco = h - (3*k + l);
            if(choco >= 0 && egg >= 0)
            {
            int m= j*a + b*k+ l*c;
            
            if(possible == false){
                sup = m;
                possible = true; }  
            else
            {
            sup= (m > sup) ? sup : m;
            }
            }
                   // count =count + 1

        }
        
        t = t-1;
    }
    return 0;
}
