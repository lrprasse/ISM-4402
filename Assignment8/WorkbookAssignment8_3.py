#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
dataframe = pd.read_csv("datasets/gradedata.csv")
dataframe
plt.scatter(dataframe.grade, dataframe['hours'])
plt.xlabel('Grade')
plt.ylabel('Hours Studying')


# In[ ]:




