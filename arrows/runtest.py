#!/usr/bin/env python
import lavavu

#This tests multiple db scan from filenames with sequential numbering
dbfile = "dbFig_Base_50.gldb"

#Using automated image output
#(objects are in incorrect render order for this test so use a custom renderlist)
lv = lavavu.Viewer(dbfile, "scan", writeimage=True, quality=2, port=0, renderlist="quads vectors points")

#Compare the output to expected results
lv.testimages()

