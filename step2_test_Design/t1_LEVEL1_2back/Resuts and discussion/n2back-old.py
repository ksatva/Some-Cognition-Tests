#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:31:49 2018

Name: function -n2back(list) 

@author: kishore, 217BM1284, MEI LAB, NITR 
Project: Biosignal Processing (EEG and Cognition)
"""
#fN2 --------- n2back(listofobjects)--------
#C=[0,1,2,3,4,5,6,7,8,9]
import random
def n2back(C):
    #print(C)
    Output=[]
    
    #flags and flagvariables
    numelOutput=0
    ncount, ocount = 0,0
    tempNcount, tempOcount=0,0
    doubflagN=0 #n-0 o-1
    doubflagO=0

    #Logic
    m1,m2=random.choice(C),random.choice(C)
    Output.append(m1)
    Output.append(m2)
    #print(m1,m2)
    numelOutput=2
    while (ncount<10):
        m3=random.choice(C)
        #print(m3)
        """if tempNcount==2:
            flag=1
            tempNcount=0"""
        
        if doubflagN==0 and doubflagO==0:
            Output.append(m3) #insert
            numelOutput+=1
            #print(1,m1,m2,m3) #remove #
            m1,m2=m2,m3

            if m1==m3:
                #ncount+=1
                tempNcount+=1
                if tempNcount==2:
                    tempNcount=0
                    doubflagN=1
            else:
                #ocount+=1
                tempOcount+=1
                if tempOcount==3:
                    doubflagO=1
                    tempOcount=0

        elif doubflagN==1:
            if m1!=m3:
                Output.append(m3) #insert
                ocount+=1
                numelOutput+=1
                #print(11,m1,m2,m3) #remove #
                m1,m2=m2,m3
                tempOcount+=1
                tempNcount=0
                doubflagN=0
                if tempOcount==3:
                    doubflagO=1
                    tempOcount=0
            else:
                if m3 in C[0:int(len(C)/2)]:
                    m3=random.choice(C[int(len(C)/2):])
                    Output.append(m3) #insert
                    print(11,m1,m2,m3)
                    m1,m2=m2,m3
                    numelOutput+=1
                    tempOcount+=1
                    doubflagN=0
                    if tempOcount==3:
                        doubflagO=1
                        tempOcount=0
        elif doubflagO==1:
            if m1==m3:
                Output.append(m3) #insert
                ncount+=1
                numelOutput+=1
                #print(11,m1,m2,m3) #remove #
                m1,m2=m2,m3
                tempNcount+=1
                tempOcount=0
                doubflagO=0
                if tempNcount==2:
                    doubflagN=0
                    tempNcount=0
            else:
                m3=m1
                Output.append(m3) #insert
                #print(22,m1,m2,m3) #remove #
                doubflagO=0
                m1=m2
                m2=m3
                numelOutput+=1
                ncount+=1
                tempNcount+=1
                if tempNcount==2:
                    doubflagN=0
                    tempNcount=0

    if len(Output)>36:
        n2back(C)
    elif len(Output)<=36:
        print(Output)
        print("fN n2back: ncount = %d"%ncount)
        print(ocount)
        print(numelOutput)
        return Output # C is a list
#n2back(C)

