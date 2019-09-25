#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 02:30:11 2018

@author: k
Program: generate n-back task array of min 15 nos wih no consecutive more
than 2 n-backs
"""

import random

#N=[1,2,3,4,5]#,6,7,8,9]
#O=['+','x','-']
def arithmetictriall1(NUMBER,OPERATOR):
    #print(C)
    Output=[]

    #flags and flagvariables
    tcount=0
    #ncount, ocount = 0,0
    #doubleflag=0
    #tempncount, tempocount=0,0
    #lflag=0
    #nflag,oflag=0,0
    #flag1=0 #n-0 o-1
    #flag2=0

    #Logic
    ans=0
    for l in range(0,3):
        n,o=random.choice(NUMBER),random.choice(OPERATOR);
        Output.append(n)
        tcount+=1
        if l!=2:
            Output.append(o)

        #print(m1,m2)
    print(Output) # TRIAL created

    #caculating the arithmetic o/p of created Trial--
    num=[Output[0],Output[2],Output[4]]
    print(num)
    ops=[Output[1],Output[3]]
    print(ops)
    if ops[0]=='+':
        ans=Output[0]+Output[2]
        #print('+'+str(ans))
    elif ops[0]=='x':
        ans=Output[0]*Output[2]
    elif ops[0]=='-':
        ans=Output[0]-Output[2]

    if ops[1]=='+':
        ans+=Output[4]
    elif ops[1]=='x':
        ans*=Output[4]
    elif ops[1]=='-':
        ans-=Output[4] #------------end calculating

    #print(tcount)
    return [Output,ans]

#arithmetictriall1(N,O)
