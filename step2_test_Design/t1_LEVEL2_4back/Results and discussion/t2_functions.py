#===fUNCTIONS
#1.createBlock(list,str)
#2.n1back(listofobjects)
#3.startTrial(Block)
from expyriment import design, control, stimuli, io, misc
#======Defining functions======
#fN1 ----------createBlock(list,str)
def createBlock(COLORS,blockname,exp): # i/p list 'COLORS' and RETURNS a stimuli block 'b'
    #for level in ["LEVEL 1"]:#,"LEVEL 2"]:
        #print(level)
    b = design.Block(name=blockname)
    b.set_factor("level",blockname) #blockname as level
    for color in COLORS:
        t = design.Trial()
        t.set_factor("COLOR",color[0])
        #print(type(color[1]))
        #print(color[0])
        s = stimuli.Rectangle([200,200],position=[0,0],colour=color[1])
        t.add_stimulus(s)
        b.add_trial(t, copies=1)
    #b.shuffle_trials() #never use this line
    #print(b.trials)
    exp.add_block(b)
    return b # b IS AN EXPERIMENT TRIAL <INPUT LIST 'COLORS' is coverted to Experiment object>

#fN2 --------- n1back(listofobjects)--------
#C=[0,1,2,3,4,5,6,7,8,9]
import random
def n5back(C):
    #print(C)
    Output=[]
    #flags and flagvariables
    tcount=0
    ncount, ocount = 0,0
    doubleflag=0
    tempNcount, tempOcount=0,0
    lflag=0
    #nflag,oflag=0,0
    doubflagN=0 #n-0 o-1
    doubflagO=0

    #Logic
    m1,m2=random.choice(C),random.choice(C)
    m3,m4,m5=random.choice(C),random.choice(C),random.choice(C)
    Output.append(m1)
    Output.append(m2)
    Output.append(m3)
    Output.append(m4)
    Output.append(m5)
    #print(m1,m2)
    tcount=2
    while (ncount<10):
        m6=random.choice(C)
        #print(m3)
        """if tempNcount==2:
            flag=1
            tempNcount=0"""
        if doubflagN==0 and doubflagO==0:
            Output.append(m6) #insert

            tcount+=1
            #print(1,m1,m2,m3) #remove #
            m1,m2,m3,m4,m5=m2,m3,m4,m5,m6

            if m1==m6:
                ncount+=1
                tempNcount+=1
                if tempNcount==2:
                    tempNcount=0
                    doubflagN=1
            else:
                ocount+=1
                tempOcount+=1
                if tempOcount==3:
                    doubflagO=1
                    tempOcount=0

        elif doubflagN==1:
            if m1!=m6:
                Output.append(m6) #insert
                ocount+=1
                tcount+=1
                #print(11,m1,m2,m3) #remove #
                m1,m2,m3,m4,m5=m2,m3,m4,m5,m6
                tempOcount+=1
                tempNcount=0
                doubflagN=0
                if tempOcount==3:
                    doubflagO=1
                    tempOcount=0
            else:
                if m6 in C[0:int(len(C)/2)]:
                    m6=random.choice(C[int(len(C)/2):])
                    Output.append(m6) #insert
                    print(11,m1,m2,m3,m4,m5,m6)
                    m1,m2,m3,m4,m5=m2,m3,m4,m5,m6
                    tcount+=1
                    tempOcount+=1
                    doubflagN=0
                    if tempOcount==3:
                        doubflagO=1
                        tempOcount=0
        elif doubflagO==1:
            if m1==m6:
                Output.append(m6) #insert
                ncount+=1
                tcount+=1
                #print(11,m1,m2,m3) #remove #
                m1,m2,m3,m4,m5=m2,m3,m4,m5,m6
                tempNcount+=1
                tempOcount=0
                doubflagO=0
                if tempNcount==2:
                    doubflagN=0
                    tempNcount=0
            else:
                m6=m1
                Output.append(m6) #insert
                #print(22,m1,m2,m3) #remove #
                doubflagO=0
                m1,m2,m3,m4,m5=m2,m3,m4,m5,m6
                tcount+=1
                ncount+=1
                tempNcount+=1
                if tempNcount==2:
                    doubflagN=0
                    tempNcount=0

    """if len(Output)>36:
        n1back(C)
    elif len(Output)<=36:
        print(Output)"""
    print("fN n1back: ncount = %d"%ncount)
    print(ocount)
    print(tcount)
    return Output # C is a list
#n1back(C)

#fN3 ---------------startTrial(Block,exp)
def startTrial(b,exp):
    numelTrial=len(b.trials)
    print(numelTrial)
    mem=[0,0,0,0,0,0]
    response_key = [misc.constants.K_SPACE]

    for b in exp.blocks:
        #------------monitoring variables
        Ncount=0 # counting nbacks in  the block && reset Ncount for next block
        totcount,memcount=0,0
        n_mem = numelTrial-6+1 # since 121
        #keyprflag=1 #flag intially set
        #----------monitoring variables...[end]
        #leftovertime=0

        for t in b.trials:
            keyprflag=1 # flag initially set
            memcount+=1
            #t.stimuli[0].preload()
            fixcross = stimuli.FixCross()
            fixcross.present()
            exp.clock.wait(500)#-t.stimuli[0].preload) #remove #
            t.stimuli[0].present()  # Presenting the stimulus onscreen

            if memcount==1 or memcount==2 or memcount==3 or memcount==4 or memcount==5: #no need of key_response
                """rt=exp.keyboard.wait(keys=response_key,duration=3000) #remove #
                try:
                    leftovertime=3000-rt[1]   #LEFT OVER TIME AFTER KEYPRESS ::ADJUST TIME FOR NEXT STIMULI
                    print(leftovertime)
                    exp.clock.wait(leftovertime)
                except:
                    print(None)"""
                exp.clock.wait(3000)

            if memcount == 1:
                mem[0]=t.factor_dict['COLOR']
                keyprflag=0
                #print(mem[0])
                #mem[0]=t.stimuli[0]
            if memcount == 2:
                mem[1]=t.factor_dict['COLOR']#t.stimuli[0]
                keyprflag=0
            if memcount == 3:
                mem[2]=t.factor_dict['COLOR']#t.stimuli[0]
                keyprflag=0
            if memcount == 4:
                mem[3]=t.factor_dict['COLOR']#t.stimuli[0]
                keyprflag=0
            if memcount == 5:
                mem[4]=t.factor_dict['COLOR']#t.stimuli[0]
                keyprflag=0

            if memcount == 6:
                mem[5]=t.factor_dict['COLOR']

                memcount=5
                n_mem-=1
                # 3 memories here
                #print(mem)

                #...CHECKING nback or not...[start]
                if mem[0]==mem[5]:  #Counting nback in stimuli
                    Ncount+=1
                    nbackoccured=True
                else:
                    nbackoccured=False #.....CHECK COMPLETE

                #if keyprflag==1:
                #    keyprflag=0
                    #print("keyprflag reset") #remove#
                rt=exp.keyboard.wait(keys=response_key,duration=3000) #remove #

                if rt[0]!=None:
                    #print("keyprflag set") #remove#
                    keyprflag=1
                    leftovertime=3000-rt[1]   #LEFT OVER TIME AFTER KEYPRESS <ADJUST TIME FOR NEXT STIMULI>
                    exp.clock.wait(leftovertime)
                    #print(rt)
                    #print(leftovertime)
                else:
                    keyprflag=0

                if nbackoccured==True and keyprflag==1:
                    print('HIT')
                    keyprflag=0
                elif nbackoccured==True and keyprflag==0:
                    print('MISS')
                elif nbackoccured==False:
                    print(-1)
                 #   keyprflag=0 #reset flag
                #...compare...[end]
                print(mem) # put#
                if n_mem != 0:
                    #mem[0]=mem[1]
                    #mem[1]=mem[2] #b is a list
                    mem[0],mem[1],mem[2],mem[3],mem[4]=mem[1],mem[2],mem[3],mem[4],mem[5]
    print("*** fN startTrial: ncount = %d "%Ncount)
