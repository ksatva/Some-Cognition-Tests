
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:20:00 2018

Name: [fUNCTION] startTrial: for arithmetic test -LEVEL 1 (Cognition)
@author: Kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing
"""
from expyriment import design, control, stimuli, io, misc
import t2L2_functions as atl

def startTrial(NUMBER,OPERATOR):

    #fixcross.preload()
    exp = design.Experiment("MATH")
    control.initialize(exp)
    control.start()
    fixcross = stimuli.FixCross()
    txt_input=io.TextInput("= ")

    stimuli.TextScreen("MATH GAME","STARTING in 10 secs",heading_size=40,text_size=60).present()
    exp.clock.wait(2000) #stim -1
    fixcross.preload()
    fixcross.present()
    exp.clock.wait(10000)
    b = design.Block()

    for i in range (0,10):  #FOR 10 TRIALS
        b.clear_trials()
        b = design.Block()
        print(i)
        tr=atl.arithmetictriall1(NUMBER,OPERATOR)
        print(tr)

        for trel in tr[0]:
            t=design.Trial()
            s = stimuli.TextLine(text=str(trel),text_size=120,text_colour=misc.constants.C_GREEN)
            t.add_stimulus(s)
            b.add_trial(t)
        #print(b.trials)
        exp.add_block(b)

        #START TEST: ONSCREEN
        for b in exp.blocks:
            fixcross.present()
            exp.clock.wait(100)

            for t in b.trials:
                t.stimuli[0].present()
                exp.clock.wait(1000)

        print(b)
        exp.clock.reset_stopwatch()
        answer = txt_input.get()

        try:
            answer=int(answer)
            if answer==tr[1]:
                print("Correct")
            else: print("incorrect")
        except:
            print("incorrect")
