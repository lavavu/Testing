#!/usr/bin/env python
"""
Custom rendering from LavaVu Python
"""

import lavavu
lv = lavavu.Viewer(axis=False, border=0, resolution=(400,400))

###################################################################

#Custom fullscreen shader

#Provide shaders in strings
frag = """
in vec4 vColour;
in vec3 vVertex;
in vec2 vTexCoord;
void main(void)
{
  gl_FragColor = vColour + vec4(vVertex, 1.0) * 0.5 + 0.5;
}
"""

vert = """
in vec3 aVertexPosition;
in vec3 aVertexNormal;
in vec4 aVertexColour;
in vec2 aVertexTexCoord;
uniform mat4 uMVMatrix;
uniform mat4 uPMatrix;
uniform mat4 uNMatrix;

uniform vec4 uColour;

out vec4 vColour;
out vec3 vVertex;

void main(void) {
  gl_Position = vec4(aVertexPosition, 1.0);

  if (uColour.a > 0.0)
    vColour = uColour;
  else
    vColour = aVertexColour;

  vVertex = aVertexPosition;
}
"""

obj = lv.screen(shaders=[vert, frag], vertices=[[0,0,0]], depthwrite=False)

###################################################################

shaderfiles = ['mandel.vert', 'mandel.frag']

#Without setting renderer=custom this will work, but only until another object is added to the default triangles renderer (which will reset the shader back to the defaults as sortedtriangles are drawn all with a single shader)
obj = lv.triangles(shaders=shaderfiles, renderer="custom", vertices=lavavu.grid2d(corners=[[-1,-1,0], [2,2,0]], dims=(2,2)), colourmap="black white", texture="colourmap")

#Setup custom uniforms using a dictionary of names and initial values
uniforms = {}
uniforms["iterations"]  = 100
uniforms["zoom"]        = 0.5
uniforms["origin"]      = [-1.5, -1.0]
uniforms["palette"]     = "colourmap" #Texture/Sampler: will copy colourmap data to texture
uniforms["background"]  = [0.0, 0.0, 0.0, 1.0]
uniforms["params"]      = []

obj["uniforms"] = uniforms

###################################################################

#Use a different triangle renderer "basictriangles"
d = lv.triangles(renderer="mesh", colour="red") 
d.vertices([[0,0,0], [1,1,1], [1,0,0.25]])

#Use a custom renderer, based on specific renderer "triangles"
e = lv.triangles(renderer="mymesh:mesh", colour="yellow")
e.vertices([[-1,0,0], [0,1,1], [0,0,0.25], [0,1,1], [0,0,0.25], [1,0,0]])

#Create another object using the previously created custom renderer
f = lv.triangles(renderer="mymesh:mesh", colour="blue")
f.vertices([[0,0,0], [1,1,1], [1,0,0.25], [1,1,1], [1,0,0.25], [2, 0, 0]])

#Use a custom renderer, but without specifying which so based on default "sortedtriangles"
b = lv.triangles(renderer="mytris", opacity=0.5, colour="green")
b.vertices([[0,0,0], [0.5,1.5,1], [1,0,0.5]])

###################################################################

#Use the default renderer for .triangles() "sortedtriangles", allows opacity
a = lv.triangles(opacity=0.5, colour="orange")
a.vertices([[0,-0.5,0.5], [0.5,1,0.25], [1,-0.5,0.5]])

#Create another object using a points based renderer
g = lv.points(renderer="cubes")
g = lv.points(renderer="pointcubes", pointsize=4, opacity=0.75)
g.vertices([[-1,0,0], [2,0,0], [0.5,1.5,1]])

#Use a different renderer from default for triangles: "particles" (sortedpoints)
c = lv.triangles(renderer="particles", pointsize=45, pointtype="sphere")
c.vertices([[0,0,0], [1,1,1], [1,0,0.5]])


###################################################################
lv.list('render')

lv.image('custom.png')
lv.testimages()
