#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:20:00 2018

Name: runscript -5-back test (Cognitive function: short term memory)

@author: Kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing (EEG and Cognition)

#===fUNCTIONS support=========
#1.createBlock(list,str)
#2.n1back(listofobjects)
#3.startTrial(Block)
#=============================
"""

from expyriment import design, control, stimuli, misc
import createBlock as cB
import n5back as n5b
import startTrial as start

control.set_develop_mode(True)
#TEST 01 DESIGN
rCOLORS=[["red",misc.constants.C_RED],["green",misc.constants.C_GREEN],["blue",misc.constants.C_BLUE],["yellow",misc.constants.C_YELLOW]]

#START TEST: ONSCREEN
for i in range(0,3):
    COLORS1=n5b.n5back(rCOLORS)
    exp = design.Experiment("n-back test")
    b1=cB.createBlock(COLORS1,'name',exp)
    fixcross = stimuli.FixCross()

    control.initialize(exp)

    control.start()
    stimuli.TextScreen("5-BACK GAME","EXPERIMENT STARTED",heading_size=40,text_size=60,heading_colour=misc.constants.C_WHITE,text_colour=misc.constants.C_WHITE).present()
    exp.clock.wait(2000) #stim -1
    fixcross.preload()
    fixcross.present()
    exp.clock.wait(10000) #stim 0

    start.startTrial(b1,exp) #stim 1 to stim n-1

    fixcross.present()
    exp.clock.wait(10000) #stim n
    #control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
