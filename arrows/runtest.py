#!/usr/bin/env python
import lavavu

#This tests multiple db scan from filenames with sequential numbering
dbfile = "dbFig_Base_50.gldb"

#Using automated image output
lv = lavavu.Viewer(arglist=["scan"], writeimage=True, database=dbfile, quality=2, port=0)

#Compare the output to expected results
lv.testimages()

