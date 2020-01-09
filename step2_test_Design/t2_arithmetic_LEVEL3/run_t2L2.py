#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 08:44:13 2018

Name: Arithmetic test - Difficulty level 1 (Cognitive fn: Working memory)
@author: Kishore, 217BM1284, MEI Lab, NITR
Project: Biosignal Processing
"""

from expyriment import design, control, stimuli, io, misc
import t2L2_startTrial as trial

control.set_develop_mode(True)

NUMBER = [1,2,3,4,5,6,7,8,9]#,6,7,8,9]
OPERATOR = ["+","x","-"]
response_key = [misc.constants.K_SPACE]

#tr=[0,0,0,0,0,0,0,0,0]
for i in range(0,3):

    trial.startTrial(NUMBER,OPERATOR) #stim 1 to stim n-1

    fixcross.present()
    exp.clock.wait(10000)

#exp = design.Experiment("Arithmetic test")
#control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
