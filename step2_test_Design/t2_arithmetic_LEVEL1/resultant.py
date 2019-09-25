#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:25:38 2018

Name: function -resultant
    
@author: kishore, 217BM1284, MEI LAB, NITR 
Project: Biosignal Processing (EEG and Cognition)
"""
import calc

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
            #print("%d s d" %n1)# %op %n2)
            ans=calc.calculate(n1,n2,op)
    return ans

#X=[5, '-', 2, '-', 4, 'x', 5, 'x', 3, 'x', 5, '-', 1]
#res=resultant(X)
#print(res)