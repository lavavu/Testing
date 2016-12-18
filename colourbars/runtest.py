#!/usr/bin/env python
import lavavu

#Colourbar overlay rendering test

lv = lavavu.Viewer(resolution=[500,500], quality=3)

lv.test()

lv.select("particles")

lv.colourbar("right")
lv.colourbar("top")
lv.colourbar("left")

obj = lv.getobject(7)
obj["font"] = "vector"
obj["fontscale"] = 0.5
obj["ticks"] = 4
obj["outline"] = 0

obj = lv.getobject(8)
obj["size"] = [200,5]
obj["position"] = 60

obj = lv.getobject(9)
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
lines.colourbar(align="right")

lv.colourbar()
obj = lv.getobject()
obj["font"] = "fixed"

lv.border(0)
lv.axis(0)
lv.hide(4,5,6)

lv.image("LavaVu.png")
lv["background"] = "white"
lv.image("LavaVu-1.png")

lv.testimages(clear=True)

