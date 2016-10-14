#!/usr/bin/env python
import lavavu

#This test ensures legacy viewport support in image output works correctly
output = ["window-00300.png", "window-00400.png", "window-00500.png"]

dbfile = "uw1-vp-gLucifer.gldb"

#Using automated image output
lv = lavavu.Viewer(writeimage=True, timestep=[300, 500], database=dbfile, figure=-1, quality=3, port=0)

lv.testimages(output)
lv.clearimages(output)

#Again using "images" command
lv = lavavu.Viewer(database=dbfile, quality=3, port=0)
lv.timestep(300)
lv.images(500)

lv.testimages(output)
lv.clearimages(output)

#Using image output scripted through python 
lv = lavavu.Viewer(quality=3, port=0)
lv.file(dbfile)

lv.open()

for ts in range(300,501,100):
    lv.timestep(ts)
    lv.image("window-" + str(ts).zfill(5))

lv.testimages(output)
lv.clearimages(output)
