#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:19:39 2018

Name: function -arithmetictriall1(num, operator)

@author: kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing (EEG and Cognition)
"""
import random
import resultant as res
#N=[1,2,3,4,5]#,6,7,8,9]
#O=['+','x','-']
def arithmetictriall1(NUMBER,OPERATOR):
    #print(C)
    Output=[]
    MAXNUM=3
    MAXOP=MAXNUM-1

    #flags and flagvariables
    tcount=0

    #Logic
    ans=0
    for l in range(0,MAXNUM):
        n,o=random.choice(NUMBER),random.choice(OPERATOR);
        Output.append(n)
        tcount+=1

        if l!=MAXOP:
            Output.append(o)
        #print(m1,m2)
    print(Output) # TRIAL CREATED

    #CALCULATING THE RESULT of created Trial--
    ans=res.resultant(Output)  #------------end calculating
    print(ans)
    return [Output,ans]

#arithmetictriall1(N,O)
