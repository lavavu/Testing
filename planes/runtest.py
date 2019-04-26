#!/usr/bin/env python
import lavavu
lv = lavavu.Viewer(border=0, verbose=0, axis=True)

x0 = 0
y0 = 0
z0 = 0
x1 = 1
y1 = 1
z1 = 1

#Canonical box: define the faces as if looking at them front on, starting from top left vertex
#first dim changes first, then second dim, grid point order (row by row)
#dims = [x,y] z fixed
front_face = [[[x0, y1, z1], [x1, y1, z1]], [[x0, y0, z1], [x1, y0, z1]]] #Start from x0,y1
back_face  = [[[x1, y1, z0], [x0, y1, z0]], [[x1, y0, z0], [x0, y0, z0]]] #Start from x1,y1 x order swapped from back view
#dims = [x,z] y fixed
top_face   = [[[x0, y1, z0], [x1, y1, z0]], [[x0, y1, z1], [x1, y1, z1]]] #Start from x0,z0
bot_face   = [[[x0, y0, z1], [x1, y0, z1]], [[x0, y0, z0], [x1, y0, z0]]] #Start from x0,z1
#dims = [z,y] x fixed
left_face  = [[[x0, y1, z0], [x0, y1, z1]], [[x0, y0, z0], [x0, y0, z1]]] #Start from z0,y1
right_face = [[[x1, y1, z1], [x1, y1, z0]], [[x1, y0, z1], [x1, y0, z0]]] #Start from z1,y1

def box(g, **kwargs):
    global lv
    lv.clear()
    lv = lavavu.Viewer(border=0, verbose=0, axis=True)

    #Correct box
    #Vertices interpreted as grid if dimensions provide (row by row), otherwise quads (counter clockwise travel per quad)
    # dimensions can be provided with dims=[w,h] or by array shape
    front   = lv.add("front", geometry=g, vertices=front_face, colour="blue", cullface=True, **kwargs)
    back    = lv.add("back", geometry=g, vertices=back_face, colour="blue", cullface=True, **kwargs)
    bottom  = lv.add("bottom", geometry=g, vertices=bot_face, colour="green", cullface=True, **kwargs)
    top     = lv.add("top", geometry=g, vertices=top_face, colour="green", cullface=True, **kwargs)
    left    = lv.add("left", geometry=g, vertices=left_face, colour="red", cullface=True, **kwargs)
    right   = lv.add("right", geometry=g, vertices=right_face, colour="red", cullface=True, **kwargs)

def test(out, exp):
    global lv
    #Enable transparent output
    lv["pngalpha"] = True
    lv.rotate('y', 45)
    lv.rotate('x', 25)
    lv.translation(0, 0.0, -2.25)
    lv.render()
    lv.image(out, resolution=[300, 300])

    if not lv.testimage("expected/" + exp, out):
        raise RuntimeError("Image tests failed due to one or more image comparisons above tolerance level!")

#Correct
box("quads")
test("quads.png", "box.png")

#Inverse
box("quads", flip=True)
test("quads_r.png", "reverse.png")

#Correct
box("triangles", dims=[2,2])
test("tris.png", "box.png")

#Inverse
box("triangles", flip=True, dims=[2,2])
test("tris_r.png", "reverse.png")

#Corner vertices of box, grid layout front then back
verts = [[x0, y0, z1],
         [x1, y0, z1],
         [x0, y1, z1],
         [x1, y1, z1],
         [x0, y0, z0],
         [x1, y0, z0],
         [x0, y1, z0],
         [x1, y1, z0]]

#lv.clear() #TODO: fix
lv = lavavu.Viewer(border=0, verbose=0, axis=True)

#Reverse box that works in old and new (as correct box above)
#Vertices interpreted as grid if dimensions provide (row by row), otherwise quads (counter clockwise travel per quad)
# dimensions can be provided with dims=[w,h] or by array shape
front   = lv.triangles(vertices=[[verts[0], verts[1]], [verts[2], verts[3]]], dims=[2,2], colour="blue", cullface=True)
back    = lv.triangles(vertices=[[verts[5], verts[4]], [verts[7], verts[6]]], dims=[2,2], colour="blue", cullface=True)
bottom  = lv.triangles(vertices=[[verts[0], verts[4]], [verts[1], verts[5]]], dims=[2,2], colour="green", cullface=True)
top     = lv.triangles(vertices=[[verts[2], verts[3]], [verts[6], verts[7]]], dims=[2,2], colour="green", cullface=True)
left    = lv.triangles(vertices=[[verts[4], verts[0]], [verts[6], verts[2]]], dims=[2,2], colour="red", cullface=True)
right   = lv.triangles(vertices=[[verts[1], verts[5]], [verts[3], verts[7]]], dims=[2,2], colour="red", cullface=True)

test("tris_r2.png", "reverse.png")

