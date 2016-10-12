#!/usr/bin/env python
import lavavu
import os

import importlib
import imp
path = os.getcwd()
dirs = [os.path.join(path,o) for o in os.listdir(path) if os.path.isdir(os.path.join(path,o))]

for d in dirs:
    os.chdir(d)
    print "Running tests in " + os.getcwd()
    print "==================================================="
    #import runtest
    testmod = imp.load_source('runtest', d + '/runtest.py')
    os.chdir(path)
    print "==================================================="

