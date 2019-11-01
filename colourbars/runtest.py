#!/usr/bin/env python
import lavavu

#Colourbar overlay rendering test

#lv = lavavu.Viewer(resolution=[500,500], quality=3)
lv = lavavu.Viewer(resolution=[500,500], quality=1)

lv.test()

particles = lv.Object('particles')

right = particles.colourbar(align="right")
top = particles.colourbar(align="top")
left = particles.colourbar(align="left")

obj = right
obj["font"] = "vector"
obj["fontscale"] = 1.26
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
obj["fontscale"] = 2.5
obj["tickvalues"] = [2,4,5]
obj["outline"] = 2
obj["fontcolour"] = "#888888"

lines = lv.objects["line-segments"]
cmap = lv.colourmap("red green blue", name="line-segments")
lines["colourmap"] = cmap
lines.colourbar(align="right") #Another on right

particles.select()
cb = lv.colourbar()
obj = lv.Object() #Gets most recently added
print(obj)
obj["font"] = "line"
cb["font"] = "vector"
cb["fontsize"] = 0.8 #Absolute font size

lv.border(0)
lv.axis(0)
#lv.hide(1,3,4,5,6)
lv.translate(1000, 0, 0)

lv.image("LavaVu.png")
lv["background"] = "white"
lv.image("LavaVu-1.png")

#Test modifying colourmaps
cmap = particles.colourmap('jet')
#cmap = particles.colourmap()

#Modify colours by list
cmap.colours[0] = 'magenta'
#Append a colour
cmap.colours += "#ffffcc"
#Modify position list, move last (appended) colour to middle
cmap.positions[-1] = 0.5
#Modify colour list by component, set last colour to transparent
cmap.colours[-1][3] = 0

lv.image("LavaVu-2.png")

lv.testimages()

