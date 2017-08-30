#!/usr/bin/env python
import lavavu

#This tests multiple db scan from filenames with sequential numbering
dbfile = "Tracers.gldb"

#Using automated image output
lv = lavavu.Viewer(database=dbfile, quality=1)

#lv.scale('tracers', 'up')
#lv.scale('tracers', 'up')

lv.open()

for ts in range(0,11,5):
    lv.timestep(ts)
    lv.image("window-" + str(ts).zfill(5))
    #lv.image()

#Compare the output to expected results
lv.testimages()

lv.open()

#Using automated image output
lv = lavavu.Viewer(database=dbfile, quality=1, cache=True)
for ts in range(0,11,5):
    lv.timestep(ts)
    lv.image("window-" + str(ts).zfill(5))

#Compare the output to expected results
lv.testimages()

#Using automated image output to write last image first with initial timestep param
lv = lavavu.Viewer(database=dbfile, timestep=10, quality=1)
lv.image("window-00010")
#Write the others or test will fail because expected not created
lv.timestep(5)
lv.image("window-00005")
lv.timestep(0)
lv.image("window-00000")

#Compare the output to expected results
lv.testimages()

