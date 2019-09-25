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

#INITIALIZING
control.initialize(exp)
# Design: 2 response mappings x 4 stimuli x 2 repitions
for level in ["LEVEL 1","LEVEL 2"]:
    b = design.Block()
    b.set_factor("LEVEL",level)
    for color in [["red",misc.constants.C_RED],["green",misc.constants.C_GREEN],["blue",misc.constants.C_BLUE],["yellow",misc.constants.C_YELLOW]]:
        t = design.Trial()
        t.set_factor("COLOR",color[0])
        s = stimuli.Rectangle([50,50],position=[0,0],colour=color[1])
        #s.preload()
        t.add_stimulus(s)
        b.add_trial(t, copies=2)
    b.shuffle_trials()
    exp.add_block(b)

exp.data_variable_names=["b","LEVEL","t","COLOR","ISI","btn"]
#Defining stimuli
#blankscreen=stimuli.BlankScreen()
#blankscreen.preload()
fixcross = stimuli.FixCross()
fixcross.preload()
#left and right keys for responses
response_keys = [misc.constants.K_SPACE]

#additional variables
t_fixcross=500
min_max_ISI = [200,750] # [min, max] inter_stimulus interval
ITI = 1000
t_error_screen = 2000
no_training_trials = 10



#defining a trial
def run_trial(cnt,trial):
    #present a fixation cross and prepare a trial for the meantime
    fixcross.present()
    exp.clock.reset_stopwatch()
    #>>>ISI = design.randomize.rand_int(min_max_ISI[0],min_max_ISI[1])
    color=trial.get_factor("COLOR")
    s = stimuli.Rectangle([50,50],position=[0,0],colour=color)
    s.preload()
    exp.clock.wait(t_fixcross - exp.clock.stopwatch_time)
    #presenting blankscreen for a random interval
    blankscreen.present()
    exp.clock.wait(ISI)
    btn,rt = exp.keyboard.wait(constants.K_SPACE)
    exp.clock.reset_stopwatch()
    exp.data.add([block.id,block.get_factor("LEVEL"),cnt,s.colour,ISI,btn,rt])
    exp.data.save()
    s.unload()
    exp.clock.wait(ITI - exp.clock.stopwatch_time)
"""
control.start()

for block in exp.blocks:
    stimuli.TextScreen("Instructions",block.get_factor("Level")).present()
    exp.keyboard.wait()
    for trial in block.trials:
        fixcross.present()
        exp.clock.wait(1000-trial.stimuli[0].preload())
        trial.stimuli[0].present()  # Presenting the stimulus onscreen
        exp.clock.wait(1000)        # Wait 1000ms for the stimulus to be present on screen
        """
for  cnt,trial in enumerate(b.trials):
    run_trial(cnt,trial)

"""
cog fn2
cog fn3
"""

control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
