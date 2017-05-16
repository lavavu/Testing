#!/usr/bin/env python
import lavavu
import os
import importlib
import imp
import sys
path = os.getcwd()

#Pass "xvfb" to open a virtual display for testing
if len(sys.argv) > 1 and sys.argv[1] == "echo":
    lavavu.echofails = 1

for d in os.listdir(path):
    if not os.path.isdir(os.path.join(path,d)): continue
    if str(d)[0] == '.': continue
    modfile = os.path.join(path, str(d) + '/runtest.py')
    if not os.path.isfile(modfile): continue;
    os.chdir(d)
    print "Running tests in " + os.getcwd()
    print "==================================================="
    #print modfile
    testmod = imp.load_source('runtest', modfile)
    os.chdir(path)
    print "==================================================="

