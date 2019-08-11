#!/usr/bin/env python
# coding: utf-8

# ## Memory leak tests and graphs
# 

# In[ ]:


import lavavu
print(lavavu.version,lavavu.__file__)
import numpy


# In[ ]:


import mem
log = mem.Log('memtest')


# **Create a viewer**

# In[ ]:


#Get a new viewer instance with required settings
def newViewer():
    lv = lavavu.Viewer(resolution=(200,200))
    #lv.test()
    lv.render()


# **Iterate**

# In[ ]:


lv = None
for i in range(20):
    lv = newViewer()
    log.log()


# In[ ]:


#%matplotlib inline
#log.plot()


# ### Test: attempt to detect a memory leak from log
# 
# - Need to check the gradient is mostly flat,
# - Jumps are ok but should not increase every step
# - Median change between steps?

# In[ ]:


increase = []
#print(log.fn)
log.logfile.close() #Ensure file closed/flushed
with open(log.fn, 'r') as f:
    last = None
    diffs = []
    percent = None
    lines = f.readlines()
    for line in lines: #[-6:]:
        val = float(line)
        if last is not None:
            #Calculate percentage increase
            percent = 100 * (val/last - 1.0)
            diffs.append(percent)
        #    print(val, val-last, percent, "%")
        #else:
        #    print(val)
        increase.append(percent)
        last = val

med = numpy.median(diffs)
print("Median diff ", med, "%")
if med > 1.0:
    raise(Exception("Memory leak detected, median increase > 1%"))


# In[ ]:




