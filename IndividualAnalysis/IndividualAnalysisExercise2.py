#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("datasets/axisdata.csv")
df.head()


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[6]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:


df['Years Experience'].mean()


# In[8]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[9]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[12]:


#Visualization 1

df.hist(column="Hours Worked", by="Gender")


# In[14]:


#Visualization 2

df.hist(column="Years Experience")


# In[ ]:




