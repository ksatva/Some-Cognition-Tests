#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 09:10:36 2018

@author: k
"""

import random

num=[1,2,3]
op=["+","-"]

#for n in num:
 #   print(n)


#foo = ['a', 'b', 'c', 'd', 'e']
#print(random.choice(num),random.choice(op))
n,o=random.choice(num),random.choice(op);
print(n,o)

for i in range(0,5):
    print(i)
    
#############
import cv2
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

def repeat():

    frame = cv.QueryFrame(capture)
    cv.ShowImage("w1", frame)


while True:
    repeat()