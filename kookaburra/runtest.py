#!/usr/bin/env python
import lavavu
import os

#This test covers multiple OBJ model loading, grouping and labelling
# along with transparent surface rendering

#Organise the data by muscle group and provide group names and colours for elements
#dataset = {}
#Required for python 2.7
from collections import OrderedDict
dataset = OrderedDict()
dataset[""] = [("Mandible.obj", [170,151,114]),
               ("Cranium-reduced-100k.obj", [170,151,114])]

dataset["Depressor Muscles"] = [("1. Depressor Mandibulae.obj", [0.82,0.05,0.11])]

dataset["Temporal muscles"] = [("2. Adductor Mandibulae Externus profundus.obj", [0.93,0.40,0.43]),
    ("3. Adductor Mandibulae Externus superficialis.obj", [0.76,0.49,0.48]),
    ("4. Unnamed Temporal muscle.obj", [0.70,0.29,0.30]),
    ("5. Adductor Mandibulae Posterior.obj", [1.00,0.00,0.46])]

dataset["Pseudotemporalis muscles"] = [("6. Pseudotemporalis superficialis.obj", [0.91,0.43,0.46,1.0]),
    ("7. Pseudotemporalis profundus.obj", [0.87,0.64,0.67,1.0])]

dataset["Dorsal Pterygoid muscles"] = [("8. Pterygoideus Dorsalis Medialis anterior.obj", [0.89,0.56,0.76,1.0]),
    ("9. Pterygoideus Dorsalis Medialis posterior.obj", [1.00,0.00,0.10,1.0]),
    ("10. Pterygoideus Dorsalis Lateralis.obj", [0.89,0.33,0.67,1.0])]

dataset["Pterygoid Muscles"] = [("11. Pterygoideus Ventralis Medialis.obj", [1.00,0.59,0.00,1.0]),
    ("12. Pterygoideus Ventralis lateralis.obj", [0.91,0.47,0.25,1.0]), 
    ("13. Pterygoideus Ventralis lateralis Part2.obj", [0.86,0.58,0.36,1.0]),
    ("14. Pterygoideus Ventralis lateralis Part3.obj", [0.78,0.49,0.32,1.0])]

#Using automated image output with the provided init.script to load/setup
lv = lavavu.Viewer(quality=2, port=0)

#With this setting the OBJ loader will ignore the normals 
#in the OBJ file and recalculate them, it's usually not necessary but
#the downloaded model only has facet normals on the vertices.
#We get nicer lighting by getting LavaVu to calculate the correct vertex normals.
lv["trisplit"] = 1

#Flip the Y and Z axes on surface load
lv["swapyz"] = True

#Enable transparent output
lv["pngalpha"] = True
lv["diffuse"] = 0.8 #Increase lighting level

#Start with the Viewer object
obj = lv
for group in dataset:
    #Has a group name? create a vis object for the group
    if len(group):
        print("Creating:" + group)
        #Following files will be loaded into this object
        # creating a composite of the loaded surfaces
        obj = lv.triangles(group)

    #Load the list of files
    for el in dataset[group]:
        fn = el[0]
        colour = el[1]
        obj.file(fn, colours=[colour])
        if len(group): obj["opacity"] = 1.0


lv.translation(0, 0, -120)
#lv.rotation(0, 180, 0)
lv.rotation(0, 1, 0, 0)

lv.border(0)
lv.axis('off')
lv.list('objects')

print(lv.objects)

mandible = lv.objects["Mandible"]
cranium = lv.objects["Cranium-reduced-100k"]

mandible["opacity"] = 0.5
cranium["opacity"] = 0.5

lv.reload() #Some settings require data to be reloaded
#lv.display(resolution=[900,400])

#lv.display()
#lv.image("output")
#lv.image("kookaburra1.png")

#Test against current framebuffer contents
if not lv.testimage("kookaburra.png", ""):
    raise RuntimeError("Image tests failed due to one or more image comparisons above tolerance level!")
#lv.testimage("orig1.jpg", "orig2.jpg")

