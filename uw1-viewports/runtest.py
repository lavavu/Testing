#!/usr/bin/env python
import lavavu
import os

#This test ensures legacy viewport support in image output works correctly
output = ["window-00300.png", "window-00400.png", "window-00500.png"]
def test(lv):
    #Compare the output to expected results
    global output
    lv.testimages(output)

def clean():
    global output
    try:
        for f in output:
            os.remove(f)
    except:
        pass

dbfile = "uw1-vp-gLucifer.gldb"

#Using automated image output
clean()
lv = lavavu.Viewer(writeimage=True, timestep=[300, 500], database=dbfile, figure=-1, quality=3, port=0)

test(lv)

#Again using "images" command
lv = lavavu.Viewer(database=dbfile, quality=3, port=0)
lv.timestep(300)
lv.images(500)

test(lv)
clean()

#Using image output scripted through python 
lv = lavavu.Viewer(quality=3, port=0)
lv.file(dbfile)

lv.open()

for ts in range(300,501,100):
    lv.timestep(ts)
    lv.image("window-" + str(ts).zfill(5))

test(lv)
clean()
