#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:21:08 2018

Name: function -startTrial(num,operator)

@author: kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing (EEG and Cognition)
"""
from expyriment import design, control, stimuli, io, misc
import arithmtrial_L1 as atl
import time

def startTrial(NUMBER,OPERATOR):

    w, h = 10, 3;
    Matrix = [[0 for x in range(w)] for y in range(h)]       # Define 2D array

    #fixcross.preload()
    exp = design.Experiment("MATH")
    control.initialize(exp)
    control.start()
    fixcross = stimuli.FixCross(size=(40,40),colour=misc.constants.C_WHITE,position=(0,200))
    txt_input=io.TextInput("= ")

    inputNAME=io.TextInput("ENTER NAME: ")
    VolunteerNAME = inputNAME.get() # First input by volunteer
    Matrix[2][1]=VolunteerNAME

    stimuli.TextScreen("MATH GAME -LEVEL 1",". . . RELAX . . .\n\n\n\n\n\n+\n\nlook at fixcross\n\n\nSTARTS IN 10 SECONDS",heading_size=40,text_size=20,heading_colour=misc.constants.C_WHITE,text_colour=misc.constants.C_WHITE).present()
    exp.clock.wait(10000) #stim -1                                               REMOVE # ON COMMISSION
    fixcross.preload()
    fixcross.present()
    exp.clock.wait(10000)                                                        # REMOVE # ON COMMISSION
    b = design.Block()

    for i in range (0,10):                                                       # cOMMISSION : 3->10 #FOR 10 TRIALS
        b.clear_trials()
        b = design.Block()
        print(i)
        tr=atl.arithmetictriall1(NUMBER,OPERATOR)
        print(tr)

        for trel in tr[0]:
            t=design.Trial()
            s = stimuli.TextLine(text=str(trel),text_size=200,text_colour=misc.constants.C_GREEN)
            t.add_stimulus(s)
            b.add_trial(t)
        #print(b.trials)
        exp.add_block(b)

        #START TEST: ONSCREEN
        #tx0=time.time()
        fixcross.present()
        exp.clock.wait(1000)
        #tx1=time.time()-tx0
        #print("ttt %d"%tx1)
        #xcount = 1                #debug fixcross timings (previously increasing time b=1)
        for b in exp.blocks:

            for t in b.trials:
                t.stimuli[0].present()
                exp.clock.wait(800) #>1000
            #xcount=0

        print(b)
        #exp.clock.reset_stopwatch()
        t0=time.time()
        answer = txt_input.get()
        responsetime=time.time()-t0     #response time

        try:
            answer=int(answer)
            if answer==tr[1]:
                print("Correct")
                Matrix[0][i]=5
                Matrix[1][i]=responsetime
            else:
                print("incorrect")
                Matrix[0][i]=-5
                Matrix[1][i]=responsetime
        except:
            print("incorrect")
            Matrix[0][i]=-5
            Matrix[1][i]=responsetime

    fixcross.present()
    exp.clock.wait(5000)
    control.end()
    #print(Matrix)
    return Matrix
