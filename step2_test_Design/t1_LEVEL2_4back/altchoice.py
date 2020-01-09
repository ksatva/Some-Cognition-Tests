#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 12:31:22 2018

Name: function -altchoice(list,element)

@author: kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing (EEG and Cognition)
"""
import random
def altchoice(alist,element):
    templist=alist[:]
    templist.remove(element)
    #print(templist)
    newelement=random.choice(templist)
    return newelement

#l=[2,4,5,6,8]
#x=altchoice(l,5)
#print(x)
