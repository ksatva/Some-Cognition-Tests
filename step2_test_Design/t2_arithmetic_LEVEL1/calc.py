#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:26:08 2018

Name: function calc
    
@author: kishore, 217BM1284, MEI LAB, NITR 
Project: Biosignal Processing (EEG and Cognition)
"""
def calculate(n1,n2,op):
    if op=='+':
        return n1+n2
    elif op=='x':
        return n1*n2
    elif op=='-':
        return n1-n2

#a=calc(2,3,"+")
#b=calc(2,3,"x")
#c=calc(2,3,"-")