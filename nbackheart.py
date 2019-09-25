#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:50:48 2018

@author: k
"""
import random

C=[0,1,2,3,4,5,6,7,8,9]
Output=[]

#flags and flagvariables
tcount=0
ncount, ocount = 0,0
doubleflag=0
tempncount, tempocount=0,0
lflag=0
#nflag,oflag=0,0
flag=-1 #n-0 o-1
#Logic
m1,m2=random.choice(C),random.choice(C)
Output.append(m1)
Output.append(m2)
#print(m1,m2)
tcount=2

while ncount<=15:
    m3=random.choice(C)
    print(m3)   
    """if tempncount==2:
        flag=1
        tempncount=0"""
    if m1==m3:
        if flag==0:
            Output.append(m3) #insert
            ncount+=1
            tcount+=1
            print(1,m1,m2,m3)
            m1,m2=m2,m3
            tempncount+=1
            tempocount=0
            if tempncount==2:
                tempncount=0
                flag=1
        else:
            if m3 in C[0:int(len(C)/2)]:
                m3=random.choice(C[int(len(C)/2):])
                Output.append(m3) #insert
                print(11,m1,m2,m3)
                m1,m2=m2,m3
                tcount+=1
                tempocount+=1
                tempncount=0
                
                 
    elif m1!=m3:
        """if tempocount==3:
            flag=1
            tempocount=0"""
        if flag==00:
            Output.append(m3) #insert
            ocount+=1
            tcount+=1
            print(2,m1,m2,m3)
            m1,m2=m2,m3
            
            tempocount+=1
            tempncount=0
            if tempocount==3:
                flag=11
                tempocount=0
            
        elif flag == 11:
            m3=m1
            Output.append(m3) #insert
            print(22,m1,m2,m3)
            m1=m2
            m2=m3
            tcount+=1
            ncount+=1
            tempncount+=1
            tempocount=0
            if tempncount==2:
                flag=0
                tempncount=0
            #print(22)
            
    
print(Output)       
print(ncount)
print(ocount)
print(tcount)


        
        
                
