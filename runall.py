#!/usr/bin/env python
import lavavu
import os
import sys
import subprocess
path = os.getcwd()

#Run the doctests
if sys.version_info[0] < 3:
    print("Python 2, Skip doctests")
else:
    print("Running doctests...")
    os.chdir(os.path.dirname(lavavu.__file__))
    subprocess.check_call(["python", "-m", "doctest", "-v", "lavavu.py"])
    os.chdir(path)

for d in sorted(os.listdir(path)):
    if not os.path.isdir(os.path.join(path,d)): continue
    if str(d)[0] == '.': continue
    fn = os.path.join(path, str(d) + '/runtest.py')
    if not os.path.isfile(fn): continue;
    if d == "memory": continue
    os.chdir(d)
    print("Running tests in " + os.getcwd())
    print("===================================================")
    subprocess.check_call(["python", fn])
    os.chdir(path)
    print("===================================================")

