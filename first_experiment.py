import expyriment
"""Hierarchical structure
> The experiment with one block
> The block has one trial
> The trial includes one stimulus
"""
exp = expyriment.design.Experiment(name="First Experiment")  # creating object:exp by calling class:Experiment in submodule design and naming it "First Experiment"
expyriment.control.initialize(exp) 
"""Initializing object:exp
1. Present a startup screen with the coundown 
2. Start an experimental clock (will be available as: exp.clock)
3. Create a screen (will be available as: exp.screen)
4. Create an event file (will be available as: exp.events)
5. Present the  Preparing experiment... screen 
"""

block = expyriment.design.Block(name="A name for the block") # Creating experimental block by calling class:Block and design:submodule 
trial = expyriment.design.Trial()                            # Creating experimental trial by calling class:trial

stim=expyriment.stimuli.TextLine(text="hello world")
stim.preload()          # Preloading the stimulus into memory

trial.add_stimulus(stim) # adding stimulus:stim to the trial
block.add_trial(trial)   # adding trial to block
exp.add_block(block)     # adding block to experiment

expyriment.control.start() 
"""Running the currently initialized experiment
1. Present the screen and ask for subject number and wait for RETURN key press
2. Create a data file (will be available as: exp.data)
3. Present a "Ready" screen
"""

stim.present()          # Presenting the stimulus onscreen
exp.clock.wait(1000)    # Wait 1000ms for the stimulus to be present on screen

expyriment.control.end() 
"""Quitting expyriment
1. will automatically save: data, the event file
2. Show "Ending experyment"
"""
