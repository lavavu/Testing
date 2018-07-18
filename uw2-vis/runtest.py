#!/usr/bin/env python
import lavavu

#This test saves images from a database containing the Underworld2 user guide visualisation notebook figures

dbfile = "uw_vis.gldb"

#Using automated image output
lv = lavavu.Viewer(writeimage=True, database=dbfile, quality=3, resolution=[440,320])

#Custom image
lv.image("highdef.jpg", resolution=(1200,1000), quality=20)

#Run comparison
lv.testimages()


