#!/usr/bin/env python
# coding: utf-8

# ## Memory leak tests and graphs
# 

# In[ ]:


import lavavu
print(lavavu.version,lavavu.__file__)
lavavu.settings["default_args"] = []
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
# 
# Just test viewer creation and rendering without any real data

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
# - Tracks median gradient over 5 steps

# In[ ]:


log.leaktest()


# In[ ]:




