#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:20:00 2018

@author: kishore, 217BM1284, MEI LAB, NITR
"""

from expyriment import design, control, stimuli, io, misc

control.set_develop_mode(True)

#Creating and initializing an experimnet
exp = design.Experiment("n-back test")
control.initialize(exp)

#DEFINING STIMULI
#blankscreen=stimuli.BlankScreen()
#blankscreen.preload()
fixcross = stimuli.FixCross()
fixcross.preload()
#left and right keys for responses
response_keys = [misc.constants.K_SPACE]

#TEST 01 DESIGN
for level in ["LEVEL 1","LEVEL 2"]:
    print(level)
    b = design.Block()
    b.set_factor("LEVEL",level)
    for color in [["red",misc.constants.C_RED],["green",misc.constants.C_GREEN],["blue",misc.constants.C_BLUE],["yellow",misc.constants.C_YELLOW]]:
        t = design.Trial()
        t.set_factor("COLOR",color[0])
        #print(type(t))
        #print(color)
        #print(type(color[1]))
        #print("color1:" + str(color[1])
        s = stimuli.Rectangle([50,50],position=[0,0],colour=color[1])
        #print(type(s))
        #s.preload()
        t.add_stimulus(s)
        b.add_trial(t, copies=2)
    b.shuffle_trials()
    print(b)
    #print(s)
    #print(trial.stimuli[0])
    exp.add_block(b)

#START TEST: ONSCREEN
control.start()
for block in exp.blocks:
    """
    if block.get_factor(level) == "LEVEL 1":
        instruction="Level 1 \n\n2 back \neg. 1 2 1 \n\nPress SPACEBAR when there is a match"
    else:
        instruction="Level 2 \n\n2 back \neg. 1 2 5 1 \n\nPress SPACEBAR when there is a match"

    stimuli.TextScreen("start",instruction+"\n\nPress ENTER to start training").present()
    exp.keyboard.wait(misc.constants.K_SPACE)
    """
    for trial in block.trials:
        """
        #TRAINING:
        stimuli.TextScreen(instruction+"\n\nPress ENTER to start training")
        exp.keyboard.wait(constants.K_ENTER)
        #TRAINING TRIALS
        for count in range(0,9)"""
        fixcross.present()
        exp.clock.wait(1000-trial.stimuli[0].preload())
        trial.stimuli[0].present()  # Presenting the stimulus onscreen
        exp.clock.wait(1000)        # Wait 1000ms for the stimulus to be present on screen
"""
cog fn2
cog fn3
"""
control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
