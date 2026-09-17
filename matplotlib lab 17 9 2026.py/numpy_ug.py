#!/usr/bin/env python
# coding: utf-8

# # #print("hello student")

# In[ ]:





# In[ ]:


print("hello")


# In[15]:


import numpy as np

a = np.array([1,2,3])
print(a, type(a))


# In[17]:


x1 = [1,2,3]
print(x1)
print(type(x1))


# In[21]:


x1 = [1,2,3.91, "a"]
print(x1)
print(type(x1))
print(np.ndim(x1))


# In[28]:


a = '1 2 3 4'
b = '123'
y = np.fromstring(b, sep = ' ')
x = np.fromstring(a, sep = ' ', dtype = int)
x = np.full()
print(x)
print(y)

#np.full
#np.zero
#np.one


# In[30]:


x = '1 2 3 4 5 6'
x = np.full(shape, fill_value, order="C")
print(x)


# In[ ]:




