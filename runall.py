#!/usr/bin/env python
import lavavu
import os
import sys
import subprocess
import platform
path = os.getcwd()

#Run the doctests
print("Running doctests...")
os.chdir(os.path.dirname(lavavu.__file__))
subprocess.check_call(["python", "-m", "doctest", "-v", "lavavu.py"])
os.chdir(path)

disabled = ["memory"]
disabled_macos = ["custom", "notebooks", "uw1-viewports"]

for d in sorted(os.listdir(path)):
    if not os.path.isdir(os.path.join(path,d)): continue
    if str(d)[0] == '.': continue
    fn = os.path.join(path, str(d) + '/runtest.py')
    if not os.path.isfile(fn): continue

    #Disabled tests
    if d in disabled:
        continue

    #Disabled on MacOS
    if platform.system() == 'Darwin' and d in disabled_macos:
        continue

    os.chdir(d)
    print("Running tests in " + os.getcwd())
    print("===================================================")
    subprocess.check_call(["python", fn])
    os.chdir(path)
    print("===================================================")

