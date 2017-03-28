#!/usr/bin/env python
import lavavu

#Colourbar overlay rendering test

#lv = lavavu.Viewer(resolution=[500,500], quality=3)
lv = lavavu.Viewer(resolution=[500,500], quality=1)

lv.test()

particles = lv.getobject('particles')

right = particles.colourbar(align="right")
top = particles.colourbar(align="top")
left = particles.colourbar(align="left")

obj = right
obj["font"] = "vector"
obj["fontscale"] = 0.5
obj["ticks"] = 4
obj["outline"] = 0

obj = top
obj["size"] = [200,5]
obj["position"] = 60

obj = left
obj["size"] = [0.5,0.1]
obj["position"] = -60
obj["offset"] = 30
obj["font"] = "vector"
obj["tickvalues"] = [2,4,5]
obj["outline"] = 2
obj["fontcolour"] = "#888888"

lines = lv.objects["line-segments"]
cmap = lv.colourmap("line-segments", "red green blue")
lines["colourmap"] = cmap
lines.colourbar(align="right") #Another on right

particles.select()
lv.colourbar()
obj = lv.getobject() #Gets most recently added
print obj
obj["font"] = "fixed"

lv.border(0)
lv.axis(0)
lv.hide(1,3,4,5,6)

lv.image("LavaVu.png")
lv["background"] = "white"
lv.image("LavaVu-1.png")

lv.testimages()

