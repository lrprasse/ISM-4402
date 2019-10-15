#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


import statsmodels.formula.api as sm
result = sm.ols(
    formula='grade ~ age + exercise + hours',
    data=df).fit()
result.summary()


# In[3]:


import statsmodels.formula.api as sm
result = sm.ols(
    formula='grade ~ exercise + hours',
    data=df).fit()
result.summary()


# In[8]:


import numpy as np
df['gennum']= np.where(df['gender'] == 'female', 1,0)
df


# In[9]:


import statsmodels.formula.api as sm
result = sm.ols(
    formula='grade ~ exercise + hours + gennum',
    data=df).fit()
result.summary()


# In[ ]:


# With the addition of gender, the r-squared value rose from 66.4% to 66.5%.
# Even though the r-square value increased, it did so very minisculely. Also,
# gender is shown to have a p value of 7.7%. Since this is higher than 5%, I
# am going to conclude that gender did not seriously improve the regression.

