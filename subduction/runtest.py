#!/usr/bin/env python
import lavavu

#This tests multiple db scan from filenames with sequential numbering
dbfile = "subduction.gldb"

#Using automated image output
lv = lavavu.Viewer(writeimage=True, database=dbfile, quality=1)

#Compare the output to expected results
lv.testimages()

