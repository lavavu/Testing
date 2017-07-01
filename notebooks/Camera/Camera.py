
# coding: utf-8

# In[ ]:

import lavavu
lv = lavavu.Viewer(background="white")


# In[ ]:

#Create regular grid with numpy
import numpy
def makegrid(width=5, height=5, offset=[0,0,0], scale=[1,1,1], axis=2):
    if axis == 0:
        axis1 = 1
        axis2 = 2
    elif axis == 1:
        axis1 = 0
        axis2 = 2
    else:
        axis1 = 0
        axis2 = 1
    width+=1 #Cells in x + 1 = vertices in x
    height+=1 #Cells in y + 1 = vertices in y
    #Calculate the x and y coord ranges
    x = numpy.arange(0, width) * scale[axis1] + offset[axis1]
    y = numpy.arange(0, height) * scale[axis2] + offset[axis2]
    #Place them in a 2d grid
    xx,yy = numpy.meshgrid(x, y)
    #Create a 3d vertex array of the required grid resolution
    verts = numpy.zeros(shape=(width*height,3), dtype='float32')
    #Copy 2d grid to 3d vertex x,y columns
    z = numpy.arange(0, width*height) * scale[axis]
    z.fill(offset[axis])
    verts[:, axis] = z
    verts[:, axis1] = xx.ravel()
    verts[:, axis2] = yy.ravel()
    return verts


# In[ ]:

#The quads() method plots a set of 3d vertices as a connected grid of quadrilaterals
#(must provide dims[0]*dims[1] 3d vertices)
x0 = lv.quads("x0", vertices=makegrid(), dims=[6,6], colour="red")
x1 = lv.quads("x1", vertices=makegrid(offset=[0,0,5]), dims=[6,6], colour="orange")
y0 = lv.quads("y0", vertices=makegrid(offset=[0,0,0], axis=0), dims=[6,6], colour="darkgreen")
y1 = lv.quads("y1", vertices=makegrid(offset=[5,0,0], axis=0), dims=[6,6], colour="chartreuse")
z0 = lv.quads("z0", vertices=makegrid(offset=[0,0,0], axis=1), dims=[6,6], colour="blue")
z1 = lv.quads("z1", vertices=makegrid(offset=[0,5,0], axis=1), dims=[6,6], colour="cyan")


# In[ ]:

lv["axislength"] = 0.35
def camset(axis, angle):
    lv.reset()
    lv.rotate(axis, angle)
    lv.display(resolution=[300,200])

def camcheck():
    cam = lv.camera()
    lv.reset()
    lv.rotation(*cam['rotation'])
    lv.translation(*cam['translation'])
    lv.display(resolution=[300,200])

camset('x', 90)
camcheck()
camset('x', -90)
camcheck()
camset('y', 90)
camcheck()
camset('y', -90)
camcheck()
camset('z', 90)
camcheck()
camset('z', -90)
camcheck()

lv.rotation(180, 0, -90)
lv.display(resolution=[300,200])
camcheck()

#Random values with fixed seed
import random
random.seed(64)
for c in range(10):
    lv.rotation(random.random()*360, random.random()*360, random.random()*360)
    lv.display(resolution=[300,200])
    camcheck()


# In[ ]:



