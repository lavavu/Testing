import sys
import gc

import resource
def usage():
    gc.collect()
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == 'darwin':
        return usage / 1048576.
    return usage / 1024.

"""
import subprocess
import os
def usage():
    cmd = "ps u -p %d | awk '{sum=sum+$6}; END {print sum/1024}'" % os.getpid()
    res = subprocess.check_output(cmd, shell=True)
    return float(res)
"""

class Log(object):
    def __init__(self, name="MemLog"):
        self.fn = name+".txt"
        self.name = name
        self.clear()

    def clear(self):
        self.logfile = open(self.fn, "w")
        self.count = 0
        self.last = 0

    def log(self):
        musage = usage()
        if musage != self.last or self.count % 20 == 0:
            print(self.count,musage,"MB")
        self.count += 1
        self.last = musage
        self.logfile.write(str(musage) + '\n')

    def plot(self, imgfile=None):
        self.logfile.flush()
        memlog = []
        with open(self.fn) as f:
            memlog = [float(line) for line in f]
        import pylab as pl
        pl.plot(memlog, color='blue', label='resource', lw=4)
        pl.legend(loc='upper left')
        pl.ylabel('Memory usage in MB')
        if imgfile is None: imgfile = self.name + ".png"
        pl.savefig(imgfile)
        pl.show()

    def leaktest(self, threshold=0.1, window=5):
        """
        An attempt to check for memory leaks
        Measures the gradient of the usage over a short window
        If the median is above the threshold, the test fails
        """
        self.logfile.flush() #Ensure entries all written
        with open(self.fn, 'r') as f:
            grads = []
            percent = None
            lines = f.readlines()
            #Calculate gradients over a window of steps (default 5)
            if len(lines) < window:
                print("Require at least %d log entries", window)
                return
            for l in range(window, len(lines)):
                diff = float(lines[l]) - float(lines[l-window])
                grad = diff / float(window)
                #print(l, l-window, diff, grad, float(lines[l]), float(lines[l-window]))
                grads.append(grad)

        import numpy
        med = numpy.median(grads)
        avg = numpy.mean(grads)
        print("Median gradient ", med)
        print("Mean gradient ", avg)
        if med > threshold:
            print(lines[-window:])
            print(grads)
            raise(Exception("Memory leak detected, median gradient > " + str(threshold)))

