#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_valume_surfacearea(l=1,w=1,h=1):
    volume=(l*w*h)
    surfacearea=2*((l*w)+(w*h)+(h*l))

    return(volume,surfacearea)


# In[2]:


find_valume_surfacearea(4)


# In[ ]:




