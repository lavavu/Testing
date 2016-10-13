#!/usr/bin/env python
import lavavu
import os

#This tests multiple db scan from filenames with sequential numbering
output = ["test-00050.png", "test-00100.png", "test-00150.png", 
          "VectorArrows_0-00050.png", "VectorArrows_0-00100.png", "VectorArrows_0-00150.png"]
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

dbfile = "dbFig_Base_50.gldb"

#Using automated image output
clean()
lv = lavavu.Viewer(arglist=["scan"], writeimage=True, database=dbfile, quality=2, port=0)

test(lv)

clean()

