#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:47:15 2018

@author: Kishore
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 08:44:13 2018

Name: Arithmatic test (Cognitive fn: Working memory)
@author: Kishore, 217BM1284, MEI Lab, NITR
"""

from expyriment import design, control, stimuli, io, misc
import random

control.set_develop_mode(True)

#Creating and initializing an experimnet
exp = design.Experiment("Arithmatic test")
control.initialize(exp)
#----------------------------------------------------------
#DEFINING STIMULI
fixcross = stimuli.FixCross()
fixcross.preload()
response_key = [misc.constants.K_SPACE]
#----------------------------------------------------------
#TEST 01 DESIGN
NUMBER = [1,2,3,4,5,6,7,8,9]
OPERATOR = ["+","-"]
#tr=[0,0,0,0,0,0,0,0,0]
tr=[]
trl2=[]
for l in range(0,5):
    #t=design.Trial()
    n,o=random.choice(NUMBER),random.choice(OPERATOR);
    #t.set_factor("DIGIT",digit)
    tr.append(n)

    #s0 = stimuli.TextLine(text=str(n),text_size=60)
    #t.add_stimulus(s0)
    #t.stimuli[0].present()
    #exp.clock.wait(1000)
    #b.add_trial(t)
    if l!=4:
        tr.append(o)
        #exp.clock.wait(1000)
        #s1 = stimuli.TextLine(text=str(o),text_size=60)
        #t.add_stimulus(s1)
        #t.stimuli[0].present()
        #exp.clock.wait(1000)
    #b.add_trial(t)
print(tr)

for level in ["LEVEL 1","LEVEL 2"]:
    print(level)
    b = design.Block(name=level)
    b.set_factor("LEVEL",level)
    for el in tr:
        t = design.Trial()
        trial.set_factor("ELEMENT",el)
    #b.shuffle_trials()
    #print(t.stimuli)
    exp.add_block(b)
    tr=[]
    #==========================================================
    #START TEST: ONSCREEN
    #control.start()
    n_trial_total=8  #compute

    for b in exp.blocks:
        for t in b.trials:

            exp.clock.wait(1000)#-t.stimuli[0].preload())
            #t.stimuli[0].present()
            #print(type(t.stimuli[1]))
            #s0.present()
            #exp.clock.wait(1000-t.stimuli[0].preload())
            #t.stimuli[0].present()
            #s1.present()


control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
