#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 02:30:11 2018

@author: k
Program: generate n-back task array of min 15 nos wih no consecutive more
than 2 n-backs
"""

import random
test1l1 = n1back(C)
C=[0,1,2,3,4,5,6,7,8,9]
def n1back(C):
    #print(C)
    Output=[]

    #flags and flagvariables
    tcount=0
    ncount, ocount = 0,0
    doubleflag=0
    tempncount, tempocount=0,0
    lflag=0
    #nflag,oflag=0,0
    flag1=0 #n-0 o-1
    flag2=0

    #Logic
    m1,m2=random.choice(C),random.choice(C)
    Output.append(m1)
    Output.append(m2)
    #print(m1,m2)
    tcount=2
    while (ncount<10):
        m3=random.choice(C)
        #print(m3)
        """if tempncount==2:
            flag=1
            tempncount=0"""
        if flag1==0 and flag2==0:
            Output.append(m3) #insert

            tcount+=1
            print(1,m1,m2,m3)
            m1,m2=m2,m3

            if m1==m3:
                ncount+=1
                tempncount+=1
                if tempncount==2:
                    tempncount=0
                    flag1=1
            else:
                ocount+=1
                tempocount+=1
                if tempocount==3:
                    flag2=1
                    tempocount=0

        elif flag1==1:
            if m1!=m3:
                Output.append(m3) #insert
                ocount+=1
                tcount+=1
                print(11,m1,m2,m3)
                m1,m2=m2,m3
                tempocount+=1
                tempncount=0
                flag1=0
                if tempocount==3:
                    flag2=1
                    tempocount=0
            else:
                if m3 in C[0:int(len(C)/2)]:
                    m3=random.choice(C[int(len(C)/2):])
                    Output.append(m3) #insert
                    print(11,m1,m2,m3)
                    m1,m2=m2,m3
                    tcount+=1
                    tempocount+=1
                    flag1=0
                    if tempocount==3:
                        flag2=1
                        tempocount=0
        elif flag2==1:
            if m1==m3:
                Output.append(m3) #insert
                ncount+=1
                tcount+=1
                print(11,m1,m2,m3)
                m1,m2=m2,m3
                tempncount+=1
                tempocount=0
                flag2=0
                if tempncount==2:
                    flag1=0
                    tempncount=0
            else:
                m3=m1
                Output.append(m3) #insert
                print(22,m1,m2,m3)
                flag2=0
                m1=m2
                m2=m3
                tcount+=1
                ncount+=1
                tempncount+=1
                if tempncount==2:
                    flag1=0
                    tempncount=0


    print(Output)
    print(ncount)
    print(ocount)
    print(tcount)
    return Output
#n1back(C)