#!/usr/bin/env python
# coding: utf-8

# In[9]:


n=5
for i in range(0,n):
    for j in range(0,i+1):
        print('*',end=' ')
    print()
for i in range(1,n):
    for j in range(0,n-i):
        print('*',end=' ')
    print()


# In[12]:


a=input('enter a word:')
print(a[::-1])


# In[ ]:




