#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 08:44:13 2018

Name: runscript -arithmetic test - Difficulty level 2 (Cognitive fn: Working memory)
@author: Kishore, 217BM1284, MEI Lab, NITR
Project: Biosignal Processing
"""

from expyriment import control, misc
import startTrial as start
import writetofile as fwrite
import time

#control.set_develop_mode(True)
control.set_develop_mode(False)

NUMBER = [1,2,3,4,5]#,6,7,8,9]
OPERATOR = ["+","x","-"]
response_key = [misc.constants.K_SPACE]

#tr=[0,0,0,0,0,0,0,0,0]
for i in range(0,1):
    start_t0=time.time()
    Matrix=start.startTrial(NUMBER,OPERATOR) #stim 1 to stim n-1
    end_tend=time.time()-start_t0
    Matrix[2][5]=end_tend

    print(Matrix)
    fwrite.writetofile("L2math_"+str(i+1),Matrix)
    #fixcross.present()
    #exp.clock.wait(10000)

#exp = design.Experiment("Arithmetic test")
#control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
