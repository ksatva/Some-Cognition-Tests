#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:04:13 2018

Name: function -n4back(list)

@author: kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing (EEG and Cognition)
"""
def setdoubNflag(tempNcount_):
    global tempNcount
    if tempNcount_==2:
        tempNcount=0
        return 1
    else:
        return 0

def setdoubOflag(tempOcount_):
    global tempOcount
    if tempOcount_==3:
        #print("doubOflag0 set")
        tempOcount=0
        #print("in flag %d"%tempOcount)
        return 1
    else:
        return 0

import altchoice as alt

#fN2 --------- n1back(listofobjects)--------
#C=[0,1,2,3,4,5,6,7,8,9]
import random
def n4back(C):
    #print(C)
    global tempOcount
    global tempNcount
    Output=[]

    #flags and flagvariables
    numelOutput=0
    ncount, ocount = 0,0
    tempNcount, tempOcount=0,0
    doubflagN, doubflagO=0,0

    #Logic
    m1,m2=random.choice(C),random.choice(C)
    m3,m4=random.choice(C),random.choice(C)
    Output.append(m1)
    Output.append(m2)
    Output.append(m3)
    Output.append(m4)
    #print(m1,m2)
    numelOutput=4
    while (ncount<10): #Commossion: set to 10
        m5=random.choice(C)
        #print(m5)

        if m5==m1:
            if doubflagN==1: #2 prev nbacks in list
                m5=alt.altchoice(C,m5) #new m3
                Output.append(m5)
                ocount+=1
                doubflagN=0 #reseting doubflagN
                numelOutput+=1
                tempOcount+=1 #if 2 setflag
                doubflagO = setdoubOflag(tempOcount)
                print(str(1))
                m1,m2,m3,m4=m2,m3,m4,m5
            else:
                Output.append(m5)
                ncount+=1
                numelOutput+=1
                tempNcount+=1 #if 2 setflag
                doubflagN = setdoubNflag(tempNcount)
                print(str(2))
                m1,m2,m3,m4=m2,m3,m4,m5
        elif m5!=m1:
            if doubflagO==1: #3 prev not-nbacks in list
                m5=m1
                Output.append(m5)
                ncount+=1
                doubflagO=0  #reseting doubflagO
                #print("doubflagO reset")
                numelOutput+=1
                tempNcount+=1 #if 2 setflag
                #print("tempNcount:"+str(tempNcount))
                doubflagN = setdoubNflag(tempNcount)
                print(str(8))
                m1,m2,m3,m4=m2,m3,m4,m5
            else:
                Output.append(m5)
                ocount+=1
                numelOutput+=1
                tempOcount+=1 #if 2 setflag
                #print("tempOcount:"+str(tempOcount))
                doubflagO = setdoubOflag(tempOcount)
                #print("doubflagO:"+str(doubflagO))
                print(str(9))
                m1,m2,m3,m4=m2,m3,m4,m5

    if len(Output)==30:                                                         #SET ON COMMISSION len(Output)==30:
        print("+++")
        print(Output)
        print(type(Output))
        print("+++ from n4back fn = %d nos."%ncount)
        print("+++ NOT n-backs = %d"%ocount)
        print("+++ total elememts = %d"%numelOutput)
        return Output

    else:#if len(Output)!=30:
        print("----")
        Output=n4back(C)

#n4back(C)
