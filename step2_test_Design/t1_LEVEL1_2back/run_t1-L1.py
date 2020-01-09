 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:20:00 2018

Name: runscript - 2-back test (Cognitive function: short term memory)

@author: Kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing (EEG and Cognition)

#===fUNCTIONS support===
#1.createBlock(list,str)
#2.n2back(listofobjects)
#3.startTrial(Block)
#=======================
"""
#[run] start
#import random
from expyriment import design, control, stimuli, misc, io
import createBlock as cB
import n2back as n2b
import startTrial as start
import writetofile as fwrite
import time

control.set_develop_mode(False)
#control.set_develop_mode(True)
#TEST 01 DESIGN
rCOLORS=[["red",misc.constants.C_RED],["green",misc.constants.C_GREEN],["blue",misc.constants.C_BLUE],["yellow",misc.constants.C_YELLOW]]

#START TEST: ONSCREEN
for i in range(0,1):                                                            #SET (0,3) ON COMMISSION
    trialname="trial no. _0"+str(i+1)
    print("*** [%s start]-----------"%trialname)

    COLORS1=n2b.n2back(rCOLORS)
    while type(COLORS1)!=list: #BUG removal : since sometimes n2back returns Nonetype
        COLORS1=n2b.n2back(rCOLORS)
        print(type(COLORS1))

    exp = design.Experiment(trialname)
    b1=cB.createBlock(COLORS1,trialname,exp)
    fixcross = stimuli.FixCross(size=(40,40),colour=misc.constants.C_WHITE)

    control.initialize(exp)

    control.start()

    inputNAME=io.TextInput("ENTER NAME: ")
    VolunteerNAME = inputNAME.get() # First input by volunteer

    stimuli.TextScreen("2-BACK GAME",". . . RELAX . . .\n\n\n\n\n\n+\n\nlook at fixcross\n\n\nSTARTS IN 10 SECONDS",heading_size=40,text_size=20,heading_colour=misc.constants.C_WHITE,text_colour=misc.constants.C_WHITE).present()
    exp.clock.wait(10000)     #stim -1                                         <REMOVE # ON COMMISSION>
    fixcross.preload()
    fixcross.present()
    exp.clock.wait(10000)     #stim 0                                          <REMOVE # ON COMMISSION>

    start_t0=time.time()
    Matrix=start.startTrial(b1,exp)   #stim 1 to stim n-1
    end_tend=time.time()-start_t0
    Matrix[2][5]=end_tend
    Matrix[2][1]=VolunteerNAME

    fixcross.present()
    exp.clock.wait(5000)       #stim n
    control.end()
    print(Matrix)
    fwrite.writetofile("2back_"+str(i+1),Matrix,VolunteerNAME)
    #control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
