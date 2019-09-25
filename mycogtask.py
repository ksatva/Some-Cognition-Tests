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
