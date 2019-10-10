#!/usr/bin/env python
import lavavu

#Test caching with multiple models with differing timesteps
dbfiles = ["PolymerA.gldb", "PolymerB.gldb"]
#dbfiles = "Polymer*.gldb" #TODO: fix

#lv = lavavu.Viewer(cache=True)
lv = lavavu.Viewer(arglist=dbfiles, resolution=[400,300], cache=True)

lv.open()

lv.image("model-1-step-0")

lv.model(1)
lv.image("model-2-step-0")

lv.timestep(10)
lv.image("model-2-step-10")

lv.model(0)
lv.image("model-1-step-10")

lv.timestep(5)
lv.image("model-1-step-5")

lv.timestep(0)
lv.image("model-1-step-0b")

lv.model(1)
lv.image("model-2-step-0b")

#Compare the output to expected results
lv.testimages()

#Test with gpucache?
#lv["gpucache"] = True

