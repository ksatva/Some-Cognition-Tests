#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:17:00 2018

Name: runscriot -arithmetic trial - Difficulty level 1 (Cognitive function: working memory)

@author: kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing (EEG and Cognition)


"""
from expyriment import control, misc #design, stimuli, io
import startTrial as start
import writetofile as fwrite
import time

control.set_develop_mode(False)
#control.set_develop_mode(True)

NUMBER = [1,2,3,4,5]#,6,7,8,9]
OPERATOR = ["+","x","-"]
response_key = [misc.constants.K_SPACE]

#tr=[0,0,0,0,0,0,0,0,0]

for i in range(0,1):
    start_t0=time.time()                                                            #Commission 1->3
    Matrix=start.startTrial(NUMBER,OPERATOR) #stim 1 to stim n-1
    end_tend=time.time()-start_t0
    Matrix[2][5]=end_tend

    print(Matrix)
    fwrite.writetofile("L1math_"+str(i+1),Matrix)

#exp = design.Experiment("Arithmetic test")
#control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
