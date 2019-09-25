#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:04:13 2018

Name: function -n5back(list) 
    
@author: kishore, 217BM1284, MEI LAB, NITR 
Project: Biosignal Processing (EEG and Cognition)
"""

#fN2 --------- n1back(listofobjects)--------
#C=[0,1,2,3,4,5,6,7,8,9]
import random
def n5back(C):
    #print(C)
    Output=[]
    #flags and flagvariables
    tcount=0
    ncount, ocount = 0,0
    tempNcount, tempOcount=0,0
    #lflag=0
    #nflag,oflag=0,0
    #doubleflag=0
    doubflagN=0 #n-0 o-1
    doubflagO=0

    #Logic
    m1,m2=random.choice(C),random.choice(C)
    m3,m4,m5=random.choice(C),random.choice(C),random.choice(C)
    Output.append(m1)
    Output.append(m2)
    Output.append(m3)
    Output.append(m4)
    Output.append(m5)
    #print(m1,m2)
    tcount=2
    while (ncount<10):
        m6=random.choice(C)
        #print(m3)
        """if tempNcount==2:
            flag=1
            tempNcount=0"""
        if doubflagN==0 and doubflagO==0:
            Output.append(m6) #insert

            tcount+=1
            #print(1,m1,m2,m3) #remove #
            m1,m2,m3,m4,m5=m2,m3,m4,m5,m6

            if m1==m6:
                ncount+=1
                tempNcount+=1
                if tempNcount==2:
                    tempNcount=0
                    doubflagN=1
            else:
                ocount+=1
                tempOcount+=1
                if tempOcount==3:
                    doubflagO=1
                    tempOcount=0

        elif doubflagN==1:
            if m1!=m6:
                Output.append(m6) #insert
                ocount+=1
                tcount+=1
                #print(11,m1,m2,m3) #remove #
                m1,m2,m3,m4,m5=m2,m3,m4,m5,m6
                tempOcount+=1
                tempNcount=0
                doubflagN=0
                if tempOcount==3:
                    doubflagO=1
                    tempOcount=0
            else:
                if m6 in C[0:int(len(C)/2)]:
                    m6=random.choice(C[int(len(C)/2):])
                    Output.append(m6) #insert
                    print(11,m1,m2,m3,m4,m5,m6)
                    m1,m2,m3,m4,m5=m2,m3,m4,m5,m6
                    tcount+=1
                    tempOcount+=1
                    doubflagN=0
                    if tempOcount==3:
                        doubflagO=1
                        tempOcount=0
        elif doubflagO==1:
            if m1==m6:
                Output.append(m6) #insert
                ncount+=1
                tcount+=1
                #print(11,m1,m2,m3) #remove #
                m1,m2,m3,m4,m5=m2,m3,m4,m5,m6
                tempNcount+=1
                tempOcount=0
                doubflagO=0
                if tempNcount==2:
                    doubflagN=0
                    tempNcount=0
            else:
                m6=m1
                Output.append(m6) #insert
                #print(22,m1,m2,m3) #remove #
                doubflagO=0
                m1,m2,m3,m4,m5=m2,m3,m4,m5,m6
                tcount+=1
                ncount+=1
                tempNcount+=1
                if tempNcount==2:
                    doubflagN=0
                    tempNcount=0

    """if len(Output)>36:
        n1back(C)
    elif len(Output)<=36:
        print(Output)"""
    print("fN n1back: ncount = %d"%ncount)
    print(ocount)
    print(tcount)
    return Output # C is a list
#n5back(C)
