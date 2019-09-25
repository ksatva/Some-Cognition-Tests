#!/usr/bin/env python
# choice reaction time test 01
from expyriment import design, control, stimuli,io,misc

#Creating and initializing an experimnet
exp=design.Experiment("CRT test")
control.initialize(exp)

#Defining stimuli
fixcross=stimuli.FixCross()
fixcross.preload()
#left and right keys for responses
response_keys = [misc.constants.K_LEFT, misc.constants.K_RIGHT]

#design
for mapping in ["left","right"]:
    b = design.Block()
    b.set_factor("Mapping", mapping)
    for where in [["left",-300],["right",300]]:     #defining left and right coordinates on screen
        for what in
