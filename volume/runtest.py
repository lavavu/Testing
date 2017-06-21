#!/usr/bin/env python
import lavavu

lv = lavavu.Viewer(resolution=[800,300])

#lv["depthtest"] = False
#lv["gpucache"] = True

#Test volume render, with colour map and translation / rotation
vols = []
for x in range(-1,2):
    lv.voltest(64, 64, 64)
    cbar = lv.getobject() #Get last added = colourbar
    lv.delete(cbar.id)
    vol = lv.getobject() #Get last added = volume
    vols.append(vol)
    vol["translate"] = [x, 0, 0]
    print vol["translate"]

vols[0]["rotate"] = [0, 45, 0]
vols[2]["rotate"] = [45, 0, 0]

lv.images()

#lv.interactive()

#Compare the output to expected results
lv.testimages()
