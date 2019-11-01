#!/usr/bin/env python
import lavavu

#This test saves images from a database containing the Underworld2 user guide visualisation notebook figures

dbfile = "uw_vis.gldb"

#Using automated image output
lv = lavavu.Viewer(writeimage=True, database=dbfile, quality=3, resolution=[440,320])

#Custom image
lv.image("highdef.jpg", resolution=(1200,1000), quality=20) #Set jpeg quality to 20%

"""
Generated databases by inserting following code in 07_Visualisation.ipynb

def newshow(self):
    self.save_database(self.name)
vis.Figure.show = newshow
"""

import glob
files = glob.glob('Fig*.gldb', recursive=True)
print(files)
for f in files:
    print(f)
    lv = lavavu.Viewer(database=f, quality=3)
    print(lv["caption"])
    lv.image(lv["caption"])

#Run comparison
lv.testimages()


