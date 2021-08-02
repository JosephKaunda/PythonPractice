#!/usr/bin/env python
# coding: utf-8

# In[6]:


a = ["0", 1, "two", "3", 4]

print('a[0]:', a[0])
print("Ya pili ni:", a[1])
print(a[3])
print(a[2])


# In[1]:


import numpy as np
f1= np.array([44,5,7,14,16,33])
type(f1)


# In[2]:


f1.size


# In[9]:


f1.dtype


# In[14]:


f1[5]=11
f1


# In[13]:


print(f1)


# In[15]:


Slicedf1=np.array([63,4,55,99,3,10])
Slicedf1


# In[16]:


type(Slicedf1)


# In[18]:


b=Slicedf1[0:6]
b


# In[20]:


z=Slicedf1[1:5]
z


# In[21]:


x=Slicedf1[3:6]


# In[22]:


x


# In[23]:


select=[0,2,4,5]


# In[24]:


p=Slicedf1[select]
p


# In[25]:


select=[0,4,5]
r=Slicedf1[select]
r


# In[26]:


Slicedf1[select]=15
Slicedf1


# In[27]:


f1


# In[28]:


f1.ndim


# In[29]:


f1.shape


# In[31]:


f1.mean()


# In[3]:


f1[5]=33
f1


# In[34]:


f1.mean()


# In[35]:


f1.std()


# In[38]:


f1.min()


# In[36]:


f1.max()


# In[41]:


LH= np.array([2,44])
LH


# In[42]:


MS=np.array([32,47])
MS


# In[43]:


f1HisT= LH+MS
f1HisT


# In[44]:


print(f1HisT)


# In[45]:


type(f1HisT)


# In[47]:


f1HisT=2*LH
f1HisT


# In[48]:


f1HisT=2*MS
print(f1HisT)


# In[49]:


f1HisT=LH*MS
f1HisT


# In[50]:


np.dot(LH,MS)


# In[51]:


LH


# In[52]:


LH+7


# In[53]:


np.pi


# In[54]:


np.linspace(-5,5, num=100)


# In[55]:


np.linspace(-5,5, num=10)


# In[56]:


LH


# In[57]:


MS


# In[59]:


f1HisT


# In[60]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(LH,f1HisT,MS)


# In[61]:


f1=[[44,77,63], [16,55,7], [33,10,22]]
f1


# In[63]:


F1.ndim


# In[64]:


F1.shape


# In[66]:


F1.size


# In[4]:


F1=np.array(f1)
F1


# In[67]:


F1[2,1]


# In[68]:


F1[0,0]


# In[69]:


F1[0:3,2]


# In[70]:


F1[2]


# In[71]:


F1[0:2,1]


# In[72]:


F1[2, 1:3]


# In[73]:


F1[2,0]


# In[74]:


F1[0,0]


# In[76]:


F1[0:3, 0]


# In[77]:


F1[0:3, 0:2]


# In[78]:


F1[0:3, 1:3]


# In[79]:


F1[0:2, 1:3]


# In[80]:


F1[1:3, 1:3]


# In[82]:


MERC=F1[0]
MERC


# In[84]:


FER=F1[1]
FER


# In[85]:


RB=F1[2]
RB


# In[86]:


ans1=FER+RB


# In[87]:


print(ans1)


# In[88]:


ans2=MERC*RB
ans2


# In[89]:


ans3=F1*MERC
ans3


# In[90]:


plt.plot(MERC,RB,FER)


# In[91]:


F1


# In[93]:


plt.plot(F1)


# In[ ]:





# In[ ]:




