#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:20:00 2018

Name: n-back test (Cognition)
@author: Kishore, 217BM1284, MEI LAB, NITR
"""
print("-0start-")
from expyriment import design, control, stimuli, io, misc
print("-0-")
#import nbackheart_v00 as nbh
import t1_fN_n1back as nbh

print("-1-")
control.set_develop_mode(True)

#Creating and initializing an experimnet
exp = design.Experiment("n-back test")
control.initialize(exp)
print("-11-") # comment
#----------------------------------------------------------
#DEFINING STIMULI
fixcross = stimuli.FixCross()
fixcross.preload()
response_key = [misc.constants.K_SPACE]
#----------------------------------------------------------
#TEST 01 DESIGN
COLORS=[["red",misc.constants.C_RED],["green",misc.constants.C_GREEN],["blue",misc.constants.C_BLUE],["yellow",misc.constants.C_YELLOW]]
print("-2-")
#COLORS=nbh.n1back(rCOLORS)
for level in ["LEVEL 1"]:#,"LEVEL 2"]:
    print(level)
    b = design.Block(name=level) #-----CONV IN fN
    b.set_factor("LEVEL",level)
    for color in COLORS:
        t = design.Trial()
        t.set_factor("COLOR",color[0])
        #print(type(color[1]))
        #print(color[0])
        s = stimuli.Rectangle([50,50],position=[0,0],colour=color[1])
        t.add_stimulus(s)
        b.add_trial(t, copies=1)
    #b.shuffle_trials() #never use this line
    print(b.trials)
    exp.add_block(b)
#==========================================================
#START TEST: ONSCREEN
control.start()
#n_trial_total=8  #compute
n_trial_total=len(b.trials)
print(len(b.trials))

mem=[0,0,0]
for b in exp.blocks:
    #------------monitoring variables
    nback_count=0 # counting nbacks in  the block && reset nback_count for next block
    totcount,memcount=0,0
    n_mem = n_trial_total-3+1 # since 121
    #----------monitoring variables...[end]

    #leftovertime=0
    for t in b.trials:
        memcount+=1
        #t.stimuli[0].preload()

        fixcross.present()
        exp.clock.wait(500)#-t.stimuli[0].preload) #remove #
        t.stimuli[0].present()  # Presenting the stimulus onscreen

        if memcount==1 or memcount==2:
            rt=exp.keyboard.wait(keys=response_key,duration=3000) #remove #
            try:
                leftovertime=3000-rt[1]   #LEFT OVER TIME AFTER KEYPRESS ::ADJUST TIME FOR NEXT STIMULI
                print(leftovertime)
                exp.clock.wait(leftovertime)
            except:
                print(None)
        keypress_flag=1 # flag initially set
        if memcount == 1:
            mem[0]=t.factor_dict['COLOR']
            #print(mem[0])
            #mem[0]=t.stimuli[0]
            keypress_flag=0
        if memcount == 2:
            mem[1]=t.factor_dict['COLOR']#t.stimuli[0]
            keypress_flag=0
        if memcount == 3:
            mem[2]=t.factor_dict['COLOR']
            memcount=2
            n_mem-=1
            # 3 memories here
            #print(mem)

            #...compare...[start]
            if mem[0]==mem[2]:  #Counting nback in stimuli
                nback_count+=1
                nbackoccured=True
            else:
                nbackoccured=False

            if keypress_flag==1:
                keypress_flag=0
                #print("keypress_flag reset") #remove#
            rt=exp.keyboard.wait(keys=response_key,duration=3000) #remove #

            if rt[0]!=None:
                #print("keypress_flag set") #remove#
                keypress_flag=1
                leftovertime=3000-rt[1]   #LEFT OVER TIME AFTER KEYPRESS <ADJUST TIME FOR NEXT STIMULI>
                exp.clock.wait(leftovertime)
                #print(rt)
                #print(leftovertime)
            if nbackoccured==True and keypress_flag==1:
                print('HIT')
                keypress_flag=0
            elif nbackoccured==True and keypress_flag==0:
                print('MISS')
            elif nbackoccured==False:
                print(-1)
             #   keypress_flag=0 #reset flag
            #...compare...[end]
            print(mem) # put#
            if n_mem != 0:
                mem[0]=mem[1]
                mem[1]=mem[2]


print("nbacks in stimuli %d\ntotal elements"%nback_count)# %totcount)

        #exp.clock.wait(1000)        # Wait 1000ms for the stimulus to be present on screen
"""
cog fn2
cog fn3
"""
control.end(goodbye_text="Thank you very much for participating in the experiment",goodbye_delay=5000)
