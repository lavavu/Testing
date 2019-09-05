#!/usr/bin/env python
# coding: utf-8

# ## Memory leak tests and graphs
# 

# In[ ]:


import lavavu
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
    lv.test()
    return lv


# **Iterate**
# 
# Test the image creation and compositing API

# In[ ]:


lv = newViewer()
lv.image("default.png", resolution=(500,500))
for i in range(50):
    background = lavavu.Image((1200, 900), value=155, channels=4)
    log.log()

    #Paste from buffer
    background.paste(lv, resolution=(800, 500), position=(1, 1))

    #Paste from image
    array = lv.loadimage("default.png")
    
    background.paste(array, position=(100, 100))
    
    background.blend(array, position=(10, 50))
    
    #background.display()


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




