#!/usr/bin/env python
import lavavu

#This test saves images from a database containing the Underworld2 user guide visualisation notebook figures

dbfile = "uw_vis.gldb"

#Using automated image output
lv = lavavu.Viewer(writeimage=True, database=dbfile, quality=3, resolution=[440,320])

#Custom image
lv.image("highdef.jpg", resolution=(1200,1000), quality=20) #Set jpeg quality to 20%

"""
Generated databases by running

jupyter nbconvert --to script $HOME/underworld2/docs/user_guide/07_Visualisation.ipynb --output `pwd`/07_Visualisation
sed -i 07_Visualisation.py -e 's/import underworld.visualisation as vis/import underworld.visualisation as vis\ndef newshow(self): self.save_database(self.name)\nvis.Figure.show = newshow\n/g'
python 07_Visualisation.py

"""

import glob
files = glob.glob('Fig*.gldb')
print(files)
for f in files:
    print(f)
    lv = lavavu.Viewer(database=f, quality=3)
    print(lv["caption"])
    lv.image(lv["caption"])

#Run comparison
lv.testimages()


