#!/usr/bin/env python
import lavavu

#This tests multiple db scan from filenames with sequential numbering
dbfile = "subduction.gldb"

#Using automated image output
lv = lavavu.Viewer(writeimage=True, database=dbfile, quality=1)

#Compare the output to expected results
lv.testimages()

#Using scripted image output
lv = lavavu.Viewer(database=dbfile, quality=1)

lv.open()

#Re-visualise the final timestep
steps = lv.timesteps()
print(steps)
lv.timestep(steps[-1])
figures = lv.figures
for name in figures:
    lv.figure(name)
    lv.display()
    lv.camera()
    print(lv)
    lv["title"] = "Timestep ##"
    lv.display()
    #lv.image(name + "-%05d.png" % steps[-1])

#Compare the output to expected results
lv.testimages()

