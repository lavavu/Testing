#!/usr/bin/env python
import lavavu
import os

#This test covers multiple OBJ model loading, grouping and labelling
# along with transparent surface rendering

#Using automated image output with the provided init.script to load/setup
lv = lavavu.Viewer(quality=2, port=0, initscript=True)

lv.open()
#lv.display()
#lv.image("output")
#lv.image("kookaburra1.png")
#Test against current framebuffer contents
lv.testimage("kookaburra.png", "")
#lv.testimage("orig1.jpg", "orig2.jpg")

