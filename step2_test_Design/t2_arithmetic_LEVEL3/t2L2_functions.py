#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:21:53 2018

Name: [fUNCTION] arithmetictrialL2 : for arithmetic test -LEVEL 2 (Cognition)
@author: kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing
"""
import random

def calc(n1,n2,op):
    if op=='+':
        return n1+n2
    elif op=='x':
        return n1*n2
    elif op=='-':
        return n1-n2

#a=calc(2,3,"+")
#b=calc(2,3,"x")
#c=calc(2,3,"-")

def resultant(Output_list):
    O=Output_list
    l=len(O)
    ans=0
    print(O)
    for i in range(0,l-1):

        if i == 0:
            ans=O[0]

        if i%2 != 0:
            n1=ans
            n2=O[i+1]
            op=O[i]
            print("%d s d" %n1)# %op %n2)
            ans=calc(n1,n2,op)
    return ans

#X=[5, '-', 2, '-', 4, 'x', 5, 'x', 3, 'x', 5, '-', 1]
#res=resultant(X)
#print(res)

#N=[1,2,3,4,5]#,6,7,8,9]
#O=['+','x','-']
def arithmetictriall1(NUMBER,OPERATOR):
    #print(C)
    Output=[]
    MAXNUM=7
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
    ans=resultant(Output)
    print(ans)
    return [Output,ans]

#arithmetictriall1(N,O)
