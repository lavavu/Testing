#!/usr/bin/env python
import lavavu

#This test ensures legacy viewport support in image output works correctly
#Same test is run using three different image output methods to verify
# all these pathways produce the same output

dbfile = "uw1-vp-gLucifer.gldb"

#Bounds, no longer support loading from window table
B0=[0., 0., 0.]
B1=[1., 1., 0.]

#Using image output scripted through python 
#(NOTE: something weird happens if this runs last, so moved to first)
lv = lavavu.Viewer(quality=1, min=B0, max=B1)
lv.file(dbfile)

lv.open()

for ts in range(300,501,100):
    lv.timestep(ts)
    lv.image("window-" + str(ts).zfill(5))

lv.testimages()

#Using automated image output
lv = lavavu.Viewer(writeimage=True, timestep=[300, 500], database=dbfile, figure=-1, quality=1, port=0, min=B0, max=B1)

lv.testimages(tolerance=0.001)

#Again using "images" command
lv = lavavu.Viewer(database=dbfile, quality=1, min=B0, max=B1)
lv.timestep(300)
lv.images(500)
lv.testimages()

