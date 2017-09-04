#!/usr/bin/env python
import lavavu

dbfile = "raytay150.gldb"

lv = lavavu.Viewer(database=dbfile, quality=3, resolution=(200,220), margin=3)

imgid = 0

def allsteps(label):
    global imgid
    for ts in lv.timesteps():
        lv.timestep(ts)
        imgid += 1
        lv.image(str(imgid).zfill(3) + "-" + label + "-" + str(ts).zfill(3) + ".jpg")

arrows = lv.objects["VectorArrows_1"]

arrows["arrowhead"] = 8

allsteps("default")

arrows["scaling"] = 1

allsteps("autoscaled")

arrows["length"] = 0.07

allsteps("fixedlength-1.0")

arrows["normalise"] = 0.6

allsteps("fixedlength-0.6")

arrows["normalise"] = 0.3

allsteps("fixedlength-0.3")

arrows["normalise"] = 0.1

allsteps("fixedlength-0.1")

arrows["arrowhead"] = 0.4
arrows["autoscale"] = False
arrows["radius"] = 0.05
lv["scalevectors"] = 10

allsteps("manual")

#Compare the output to expected results
lv.testimages()

