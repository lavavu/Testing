#!/usr/bin/env python
import lavavu
import random
import math

lv = lavavu.Viewer(resolution=[640,480])

lv["gpucache"] = True

#Points
random.seed(0) # Use a constant seed for determinism
def randomPoints(count, minvert=[-1.0, -1.0, -1.0], maxvert=[1.0, 1.0, 1.0]):
    ptlist = []
    vallist = []
    for p in range(0,count):
        pt = [random.uniform(minvert[0], maxvert[0]),
              random.uniform(minvert[1], maxvert[1]),
              random.uniform(minvert[2], maxvert[2])]
        ptlist.append(pt)
        #vallist.append(random.uniform(0.0, 1.0))
        vallist.append(math.sqrt(pt[0]*pt[0] + pt[1]*pt[1] + pt[2]*pt[2]))
    return (ptlist, vallist)

#Static data: Axis lines
lines = lv.lines("axes", link=False, vertices=[[-1.5, 0, 0], [1.5, 0, 0], [0, -1.5, 0], [0, 1.5, 0], [0, 0, -1.5], [0, 0, 1.5]], colours="red green blue")

#Time varying data: points
points = lv.points(pointsize=16, opacity=0.75, pointtype="shiny")
points.colourmap(lavavu.cubeHelix())
points.colourbar()

for step in range(3):
    lv.addstep()
    randpts = randomPoints(5000)
    points.vertices(randpts[0])
    points.values(randpts[1])

lv.timestep(0)

lv.open()
steps = lv.timesteps()
print steps

lv.translation(0, 0, -3.5)

lv.image("unfiltered")

#Filter test

#Clear filters
points["filters"] = []
#Filter out a range of values
myfilter = points.excludemap('default', (0.4, 0.6))

lv.images()

#Compare the output to expected results
lv.testimages()
