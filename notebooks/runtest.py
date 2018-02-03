#!/usr/bin/env python
#This test runs notebooks that produce image output and checks the images against expected output
# coding: utf-8
import lavavu
import os
import glob
import subprocess
import shutil

#Viewer instance for running image tests
lv = lavavu.Viewer(quality=1)

#Save working dir
wd = os.getcwd()

def testNotebook(path):
    #Get filename without path and extension
    notebook = os.path.splitext(os.path.basename(path))[0]
    print("Testing Notebook: " + notebook)
    #Check if the test dir exists, if not create
    dirfound = os.path.exists(notebook)
    if not dirfound: 
        print("Creating dirs: " + notebook + '/expected')
        os.makedirs(os.path.join(notebook, 'expected'))

    if not os.path.exists(notebook):
        os.makedirs(notebook)

    #Notebooks must be converted to py before running or images will be generated inline and not saved to disk
    try:
        import nbformat
        from nbconvert import PythonExporter
        with open(path) as fh:
            nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)
        exporter = PythonExporter()
        source, meta = exporter.from_notebook_node(nb)
        with open(os.path.join(wd, notebook, notebook) + '.py', 'w+') as f:
            f.write(source) #lines(source.encode('utf-8'))
    except:
        print("Notebook conversion failed")
        pass

    #Change to working dir for test
    os.chdir(notebook)

    #Remove any images from partial test run
    for im in glob.glob("*.png"):
        os.remove(im)

    #Execute converted script
    subprocess.check_call(['python', notebook+".py"])

    #Use output of the initial run as expected data
    if not dirfound:
        print("Using files created by initial run as expected output for tests")
        images = glob.glob("*.png")
        for f in images:
            shutil.move(f, os.path.join('expected', f))
    else:
        #Check the image results
        lv.testimages(tolerance=1e-3)

    #Restore working dir
    os.chdir(wd)

#Process list of notebooks, local and in LavaVu notebooks folder
nbdir = os.path.join(os.path.dirname(lavavu.__file__), "notebooks")
print(nbdir)
files = [
    'ColourMaps.ipynb',
    'Camera.ipynb'
    ]

print(files)
for f in files:
    fname = os.path.join(nbdir, f)
    if not os.path.isfile(fname):
        fname = f
    print(fname)
    testNotebook(fname)

