# Two blocks two trials each
# also measuring reaction times

import expyriment

exp = expyriment.design.Experiment(name="First Experiment")  # creating object:exp by calling class:Experiment in submodule design and naming it "First Experiment"
expyriment.control.initialize(exp)
"""Initializing object:exp
1. Present a startup screen with the coundown
2. Start an experimental clock (will be available as: exp.clock)
3. Create a screen (will be available as: exp.screen)
4. Create an event file (will be available as: exp.events)
5. Present the  'Preparing experiment...' screen
"""
# BLOCK 1 [trial 1 & trial 2]
block_one = expyriment.design.Block(name="Block one") # Creating experimental block by calling class:Block and design:submodule
# Block1: trial 1
trial_one = expyriment.design.Trial()                 # Creating experimental trial by calling class:trial
stim=expyriment.stimuli.TextLine(text="Block one stimuli: trial one")
stim.preload()               # Preloading the stimulus into memory
trial_one.add_stimulus(stim) # adding stimulus:stim to the trial
# Block1: trial 2
trial_two=expyriment.design.Trial()
stim=expyriment.stimuli.TextLine(text="Block one stimuli: trial two")
stim.preload()
trial_two.add_stimulus(stim)
# block1 [trial 1 and trial2] created. now adding both trials to block. Finally  adding blocks to experiment
block_one.add_trial(trial_one)   # adding trial to block
block_one.add_trial(trial_two)
exp.add_block(block_one)         # adding block to experiment

# BLOCK 2 [trial 1 & trail 2]
block_two = expyriment.design.Block(name="Block two")
trial_one = expyriment.design.Trial()                            # Creating experimental trial by calling class:trial
stim=expyriment.stimuli.TextLine(text="Block one stimuli: trial one")
stim.preload()           # Preloading the stimulus into memory
trial_one.add_stimulus(stim) # adding stimulus:stim to the trial

trial_two=expyriment.design.Trial()
stim=expyriment.stimuli.TextLine(text="Block one stimuli: trial two")
stim.preload()
trial_two.add_stimulus(stim)

block_two.add_trial(trial_one)   # adding trial to block
block_two.add_trial(trial_two)
exp.add_block(block_two)         # adding block to experiment

# start of Experiment
expyriment.control.start()
#Running the currently initialized experimentimport expyriment

exp = expyriment.design.Experiment(name="First Experiment")  # creating object:exp by calling class:Experiment in submodule design and naming it "First Experiment"
expyriment.control.initialize(exp)
"""Initializing object:exp
1. Present a startup screen with the coundown
2. Start an experimental clock (will be available as: exp.clock)
3. Create a screen (will be available as: exp.screen)
4. Create an event file (will be available as: exp.events)
5. Present the  'Preparing experiment...' screen
""""""
1. Present the screen and ask for subject number and wait for RETURN key press
2. Create a data file (will be available as: exp.data)
3. Present a "Ready" screen
"""

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()  # Presenting the stimulus onscreen
        #exp.clock.wait(1000)        # Wait 1000ms for the stimulus to be present on screen
        key,rt =exp.keyboard.wait([expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])
        exp.data.add([block.name, trial.id, key, rt])

expyriment.control.end()
"""Quitting expyriment
1. will automatically save: data, the event file
2. Show "Ending experyment"
"""
