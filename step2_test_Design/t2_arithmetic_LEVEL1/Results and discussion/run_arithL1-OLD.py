#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 08:44:13 2018

Name: Arithmatic test (Cognitive fn: Working memory)
@author: Kishore, 217BM1284, MEI Lab, NITR
"""

from expyriment import design, control, stimuli, io, misc
import arithmaticheart_v00 as atl

control.set_develop_mode(True)

#Creating and initializing an experimnet

#----------------------------------------------------------
#DEFINING STIMULI
fixcross = stimuli.FixCross()
fixcross.preload()
response_key = [misc.constants.K_SPACE]
txt_input=io.TextInput("= ")
#design.experiment.register_wait_callback_function
#----------------------------------------------------------
#TEST 01 DESIGN
NUMBER = [1,2,3,4,5]#,6,7,8,9]
OPERATOR = ["+","x","-"]
#tr=[0,0,0,0,0,0,0,0,0]

for i in range(0,3)#["LEVEL 1"]:#,"LEVEL 2"]:
    print("---lap no. %d---"%i)#level)

    exp = design.Experiment("Arithmetic test")
    control.initialize(exp)
    control.start()

    b = design.Block()
    for i in range (0,10):  #FOR 10 TRIALS
        b.clear_trials()
        b = design.Block()
        print(i)
        tr=atl.arithmetictriall1(NUMBER,OPERATOR)
        print(tr)
        for trel in tr[0]:
            t=design.Trial()
            s = stimuli.TextLine(text=str(trel),text_size=100,text_colour=misc.constants.C_GREEN)
            t.add_stimulus(s)
            b.add_trial(t)
        #print(b.trials)
        exp.add_block(b)
        #==========================================================
        #START TEST: ONSCREEN
        #n_trial_total=8  #compute
        for b in exp.blocks:
            fixcross.present()
            exp.clock.wait(2000)

            for t in b.trials:
                t.stimuli[0].present()
                exp.clock.wait(2000)
        print(b)
        exp.clock.reset_stopwatch()
        answer = txt_input.get()
        if int(answer)==tr[1]:
            print("Correct")
        else:
            print("incorrect")

#control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
