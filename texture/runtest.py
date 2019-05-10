#!/usr/bin/env python
import lavavu

#Textured mesh tests
# - Test auto texcoord generation and loading our own texcoords
# - Test loading texture data directly rather than from a file
# - Tests clearing data before loading new content, entire model and just texcoord data
# - Test autozoom mode and margin set

lv = lavavu.Viewer(quality=2, axis=False, border=0, margin=0)

#Create a texture image for the tests
lv.test()
lv.hide(2, 3, 4, 5, 6)
lv["pointsize"] = 2
lv.image('tex.png', resolution=(256,256), transparent=True)

lv.clear()
lv.autozoom()

#Use grid layout, from array shape
V = [[[-1.,0.,0.], [1., 0., 0.]], [[-1., 1., 0.1], [1.,1.,0.]]]
#Tweaked texcoords
T = [[0.,0.5], [1., 0.5], [0., 1.], [1., 1.]]

#Use auto texcoords
grid = lv.triangles(vertices=V, texture="tex.png", colour="grey")

lv.image("test1.jpg", resolution=(200,150))
lv.clear()

#Provided texcoords
grid = lv.triangles(vertices=V, texcoords=T, texture="tex.png", colour="grey")

lv.image("test2.jpg", resolution=(200,150))
lv.clear()

#Adjust margin
lv["margin"] = 10

#Use triangles
V = [[-1.,0.,0.], [1., 0., 0.], [1., 1., 0.1], [-1.,0.,0.], [1., 1., 0.1], [-1.,1.,0.]]
#Tweaked texcoords
T = [[0.5,0.], [1., 0.], [1., 1.], [0.5,0.], [1., 1.], [0.5, 1.]]

#Use auto texcoords
tris = lv.triangles(vertices=V, texture="tex.png", colour="grey")

lv.image("test3.jpg", resolution=(200,150))

#Clear texcoord data only
tris.cleardata("texcoords")

#Load replacement texcoords
tris.texcoords(T)

lv.image("test4.jpg", resolution=(200,150))

lv.clear()

#Load a procedurally generated texture
import numpy as np
np.random.seed(0)
img = np.random.random([500, 500])

#Convert to uint8 rgb
img = 255 * img
img = img.astype(np.uint8)
img = np.stack([img, img, img], axis=-1)

#Use triangles with auto-texcoords
V = [[-1.,0.,0.], [1., 0., 0.], [1., 1., 0.1], [-1.,0.,0.], [1., 1., 0.1], [-1.,1.,0.]]
tris = lv.triangles(vertices=V, colour="grey")
tris.texture(img)
img = None

lv.image("test5.jpg", resolution=(200,150))

#Remove the test texture, so will not be copied to expected
import os
os.remove('tex.png')

lv.testimages()

