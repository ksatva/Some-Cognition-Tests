#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 17:22:55 2018

@author: k
"""
def __eq__(self, other):
        #return self._id == other._id
        print(self._id)

from expyriment import design, control, stimuli, io, misc

control.set_develop_mode(True)

exp=design.Experiment("n-back test")
control.initialize(exp)
fixcross = stimuli.FixCross() #Defining a fixcross stimuli
fixcross.preload()
response_key = [misc.constants.K_SPACE]
STIMULI=[9, 0, 9, 7, 9, 4, 7, 6, 7, 6]

for level in ["LEVEL 1"]:#,"LEVEL 2"]:
    print(level)
    b = design.Block(name=level)
    b.set_factor("LEVEL",level)
    for st in STIMULI:
        t = design.Trial()
        #t.set_factor("COLOR",color[0])
        #print(type(color[1]))
        s=stimuli.TextLine(text=str(st),text_size=60)
        #s = stimuli.Rectangle([50,50],position=[0,0],colour=color[1])
        t.add_stimulus(s)
        b.add_trial(t, copies=1)
    #b.shuffle_trials()
    #print(b)
    print(t.stimuli)
    exp.add_block(b)
#==========================================================
#START TEST: ONSCREEN
control.start()
n_trial_total=8  #compute


mem=[0,0,0]
for b in exp.blocks:
    #------------monitoring variables
    nback_count=0 # counting nbacks in  the block && reset nback_count for next block
    count=0
    n_mem = n_trial_total-3+1 # since 121
    #----------monitoring variables...[end]
    for t in b.trials:
        count+=1
        fixcross.present()
        exp.clock.wait(2000-t.stimuli[0].preload())
        t.stimuli[0].present()  # Presenting the stimulus onscreen

        rt=exp.keyboard.wait(keys=response_key,duration=2000)
        #print(rt[0])
        print(rt)
        if rt[0]!=None:
            print("flag set")
            keypress_flag=1

        if count == 1:
            mem[0]=t.stimuli[0]
            keypress_flag=0
        if count == 2:
            mem[1]=t.stimuli[0]
            keypress_flag=0
        if count == 3:
            mem[2]=t.stimuli[0]
            count=2
            n_mem-=1
            # 3 memories here
            print(mem)
            #...compare...[start]

            __eq__(mem[0],mem[2])


            if mem[0]==mem[2]:  #Counting nback in stimuli
                nback_count+=1
                print("nback occured")

            if mem[0]==mem[2] and keypress_flag==1:
                print('HIT')
                keypress_flag=0
            elif mem[0]!=mem[2] and keypress_flag==1:
                print('MISS')
                keypress_flag=0
            else:
                keypress_flag=0 #reset flag
            #...compare...[end]

            if n_mem != 0:
                mem[0]=mem[1]
                mem[1]=mem[2]


print("nbacks in stimuli %d"%nback_count)

        #exp.clock.wait(1000)        # Wait 1000ms for the stimulus to be present on screen
"""
cog fn2
cog fn3
"""
control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
