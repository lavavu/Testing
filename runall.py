#!/usr/bin/env python
import lavavu
import os
import sys
import subprocess
import imp
path = os.getcwd()

#Below settings don't work unless tests run as modules
module = True

if "echo" in sys.argv:
    lavavu.settings["echo_fails"] = True

if "verbose" in sys.argv:
    lavavu.settings["default_args"] += ['-v']

for d in os.listdir(path):
    if not os.path.isdir(os.path.join(path,d)): continue
    if str(d)[0] == '.': continue
    fn = os.path.join(path, str(d) + '/runtest.py')
    if not os.path.isfile(fn): continue;
    os.chdir(d)
    print("Running tests in " + os.getcwd())
    print("===================================================")
    if module:
        testmod = imp.load_source('runtest', fn)
    else:
        subprocess.check_call(["python", fn])
    os.chdir(path)
    print("===================================================")

