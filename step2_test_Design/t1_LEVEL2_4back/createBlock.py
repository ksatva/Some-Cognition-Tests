#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:06:18 2018

Name: function -createBlock(list,string,exp-obj) -4back

@author: kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing (EEG and Cognition)
"""

from expyriment import design, stimuli #control, io, misc
#======Defining functions======
#fN1 ----------createBlock(list,str)
def createBlock(COLORS,blockname,exp): # i/p list 'COLORS' and RETURNS a stimuli block 'b'
    #for level in ["LEVEL 1"]:#,"LEVEL 2"]:
        #print(level)
    b = design.Block(name=blockname)
    b.set_factor("level",blockname) #blockname as level
    for color in COLORS:
        t = design.Trial()
        t.set_factor("COLOR",color[0])
        #print(type(color[1]))
        #print(color[0])
        s = stimuli.Rectangle([200,200],position=[0,0],colour=color[1])
        t.add_stimulus(s)
        b.add_trial(t, copies=1)
    #b.shuffle_trials() #never use this line
    #print(b.trials)
    exp.add_block(b)
    return b # b IS AN EXPERIMENT TRIAL <INPUT LIST 'COLORS' is coverted to Experiment object>
