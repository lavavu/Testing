#This test runs notebooks that produce image output and checks the images against expected output
# coding: utf-8
import lavavu
import os
import glob
import subprocess
import shutil

#Viewer instance for running image tests
lv = lavavu.Viewer(quality=1)

nbdir = os.path.join(os.path.dirname(lavavu.__file__), "notebooks")
print nbdir 
#files = glob.glob(nbdir  + "/*.ipynb")
files = [
    'ColourMaps.ipynb'
    ]

print files

#Save working dir
wd = os.getcwd()

#Process list of notebooks
for f in files:
    fname = os.path.join(nbdir, f)
    #Get filename without path and extension
    notebook = os.path.splitext(os.path.basename(fname))[0]
    print "Testing Notebook: " + notebook
    #Check if the test dir exists, if not create
    dirfound = os.path.exists(notebook)
    if not dirfound: 
        print "Creating dirs: " + notebook + '/expected'
        os.makedirs(os.path.join(notebook, 'expected'))
    #Create log file
    outName = notebook + "/convert.out"
    with open(outName, "w") as outFile:
        if not os.path.exists(notebook):
            os.makedirs(notebook)

        #Notebooks must be converted to py before running or images will be generated inline and not saved to disk
        subprocess.check_call(['jupyter', 'nbconvert', '--to', 'script', fname, '--output', os.path.join(wd,notebook, notebook)],
                stdout=outFile, stderr=outFile )
        #Change to working dir for test
        os.chdir(notebook)
        #Execute converted script
        subprocess.check_call(['python', notebook+".py"], stdout=outFile, stderr=outFile )

    #Use output of the initial run as expected data
    if not dirfound:
        print "Using files created by initial run as expected output for tests"
        images = glob.glob("*.png")
        for f in images:
            shutil.move(f, os.path.join('expected', f))
    else:
        #Check the image results
        lv.testimages(tolerance=1e-3)

    #Restore working dir
    os.chdir(wd)

