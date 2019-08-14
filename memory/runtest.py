#!/usr/bin/env python
# coding: utf-8
#Run a memory leak test
import subprocess
import shutil

try:
    subprocess.check_call(["jupyter", "nbconvert", "--to", "python", "memory_tests.ipynb"])
    subprocess.check_call(["jupyter", "nbconvert", "--to", "python", "memory_tests_images.ipynb"])
except (Exception) as e:
    print("Notebook conversion failed: ", e)
    pass

subprocess.check_call(["python", "memory_tests.py"])
subprocess.check_call(["python", "memory_tests_images.py"])

