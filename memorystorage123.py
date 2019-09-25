#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:01:26 2018

@author: k
"""
n_mem=10-3+1
count = 0
mem=[0,0,0]
for i in range(0,10):
    count+=1
    if count == 1:
        mem[0]=i
    if count == 2:
        mem[1]=i
    if count == 3:
        mem[2]=i
        count=2
        n_mem-=1
        print(mem)
        if n_mem != 0:
            mem[0]=mem[1]
            mem[1]=mem[2]
            