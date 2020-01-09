#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 02:30:11 2018

@author: kishore, 217BM1284, MEI Lab, NITR
Program: generate n-back task array of min 15 nos wih no consecutive more
than 2 n-backs
"""
#n1back(C)

import random

#C=[0,1,2,3,4,5,6,7,8,9]

def n1back(C):
    #print(C)
    Output=[]

    #flags and flagvariables
    tcount=0
    ncount, ocount = 0,0
    doubleflag=0
    tempNcount, tempOcount=0,0
    lflag=0
    #nflag,oflag=0,0
    doubflagN=0 #n-0 o-1
    doubflagO=0

    #Logic
    m1,m2=random.choice(C),random.choice(C)
    Output.append(m1)
    Output.append(m2)
    #print(m1,m2)
    tcount=2
    while (ncount<10):
        m3=random.choice(C)
        #print(m3)
        """if tempNcount==2:
            flag=1
            tempNcount=0"""
        if doubflagN==0 and doubflagO==0:
            Output.append(m3) #insert

            tcount+=1
            #print(1,m1,m2,m3) #remove #
            m1,m2=m2,m3

            if m1==m3:
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
            if m1!=m3:
                Output.append(m3) #insert
                ocount+=1
                tcount+=1
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
                    tcount+=1
                    tempOcount+=1
                    doubflagN=0
                    if tempOcount==3:
                        doubflagO=1
                        tempOcount=0
        elif doubflagO==1:
            if m1==m3:
                Output.append(m3) #insert
                ncount+=1
                tcount+=1
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
                tcount+=1
                ncount+=1
                tempNcount+=1
                if tempNcount==2:
                    doubflagN=0
                    tempNcount=0


    if len(Output)>36:
        n1back(C)
    elif len(Output)<=36:
        print(Output)
        print(ncount)
        print(ocount)
        print(tcount)
        return Output
#n1back(C)
