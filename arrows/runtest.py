#!/usr/bin/env python
import lavavu

#This tests multiple db scan from filenames with sequential numbering
output = ["test-00050.png", "test-00100.png", "test-00150.png", 
          "VectorArrows_0-00050.png", "VectorArrows_0-00100.png", "VectorArrows_0-00150.png"]

dbfile = "dbFig_Base_50.gldb"

#Using automated image output
lv = lavavu.Viewer(arglist=["scan"], writeimage=True, database=dbfile, quality=2, port=0)

#Compare the output to expected results
lv.testimages(output)
lv.clearimages(output)

