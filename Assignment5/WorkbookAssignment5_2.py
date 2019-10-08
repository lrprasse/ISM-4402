#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]

DataSet = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=DataSet,
                 columns=['Names','Grades','BS Degrees','MS Degrees','PhD Degrees'])
df

df.count()
df['Grades'].mean()
df['MS Degrees'].sum()
df['BS Degrees'].mode()
df['Grades'].std()
df.var()


# In[ ]:





# In[ ]:




