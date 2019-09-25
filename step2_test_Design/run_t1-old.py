#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:20:00 2018

Name: n-back test (Cognition)
@author: Kishore, 217BM1284, MEI LAB, NITR
"""
import random
from expyriment import design, control, stimuli, io, misc
import t1_functions as nbh

control.set_develop_mode(True)
#Creating and initializing an experimnet
#fixcross.preload()
#response_key = [misc.constants.K_SPACE]
#----------------------------------------------------------
#TEST 01 DESIGN
rCOLORS=[["red",misc.constants.C_RED],["green",misc.constants.C_GREEN],["blue",misc.constants.C_BLUE],["yellow",misc.constants.C_YELLOW]]

#COLORS1=nbh.n1back(rCOLORS) #fn call
#COLORS2=nbh.n1back(rCOLORS)
#COLORS3=nbh.n1back(rCOLORS)
#b1=nbh.createBlock(COLORS1,'name',exp)                #fn call
#b2=nbh.createBlock(COLORS2,'name',exp)
#b3=nbh.createBlock(COLORS3,'name',exp)
#==========================================================
#START TEST: ONSCREEN
for i in range(0,3):
    COLORS1=nbh.n1back(rCOLORS)
    exp = design.Experiment("n-back test")
    b1=nbh.createBlock(COLORS1,'name',exp)

    control.initialize(exp)
    #DEFINING STIMULI ----------
    fixcross = stimuli.FixCross()

    control.start()
    stimuli.TextScreen("2-BACK GAME","EXPERIMENT STARTED",heading_size=40,text_size=60).present()
    exp.clock.wait(2000)
    fixcross.preload()
    fixcross.present()
    exp.clock.wait(10000)
    #n_trial_total=8  #compute
    nbh.startTrial(b1,exp)
    #nbh.startTrial(b2,exp)
    #nbh.startTrial(b3,exp)




#print("nbacks in stimuli %d\ntotal elements"%nback_count)# %totcount)
    fixcross.present()
    exp.clock.wait(10000) #exp.clock.wait(1000)        # Wait 1000ms for the stimulus to be present on screen
    #control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)

"""
cog fn2
cog fn3
"""
