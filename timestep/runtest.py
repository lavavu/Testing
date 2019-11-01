#!/usr/bin/env python
import lavavu

#Tests:
#timestep + fixed data and objects
#shapes renderer
#auto bounds calc
#auto zoom

lv = lavavu.Viewer(axis=False, border=1, rulers=True, resolution=[300,200], fontscale=1.5, rulerscale=1, background="white")

#object with fixed vertices and time varying values
s0 = lv.cuboids(scaling=0.2, vertices=[0.5,0.0,1.0], colourmap="cubelaw")

lv.addstep(title="STEP 0")
s0.values(0)

#Object with all time varying data
s1 = lv.spheres(scaling=0.2, vertices=[0,0,0], colour="red")

lv.addstep(title="STEP 1")

s0.values(1)
s1.vertices([0.1, 0., 0.])

#Fixed objects
s2 = lv.cuboids(scaling=0.4, vertices=[0,0.5,0], colour="green", fixed=True)
s3 = lv.shapes(shape=1, scaling=0.3, vertices=[0.5,0.5,0], colour="blue", fixed=True)
s4 = lv.shapes(shape=1, scaling=0.2, vertices=[0.5,0.5,0.5], colour="yellow", fixed=True)

#Also add some fixed data to s1 now...
s1["fixed"] = True
s1.vertices([-0.5, 0., 0.])
s1["fixed"] = False

lv.addstep(title="STEP 2")
s0.values(2)
s1.vertices([0.2, 0., 0.])
lv.addstep(title="STEP 3")
s0.values(3)
s1.vertices([0.3, 0., 0.])

#Also test custom bounding box
lv["min"] = [-1, -0.5, -0.5]
lv["max"] = [0.8, 0.8, 0.8]
#Set margin and zoom to fit
lv["margin"] = 20
lv.fit()

#Images per step
lv.timestep(0)
lv.images()

#Recalc bounds & zoom to fit
lv.bounds()
lv.image("autobounds")
lv.fit()
lv.image("autofit")

#Compare the output to expected results
lv.testimages()

