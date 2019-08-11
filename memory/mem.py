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
        self.logfile = open(self.fn, "w")
        self.count = 0
        self.last = 0
        self.name = name

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


