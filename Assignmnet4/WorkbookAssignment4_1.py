#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

bins = [0, 80, 100]
group_names = ['FAIL', 'PASS']

df['pass/fail'] = pd.cut(df['grade'], bins,
labels=group_names)
df


# In[ ]:




