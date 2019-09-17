#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import glob

call_data = pd.DataFrame()
for f in glob.glob("datasets/weekly_call_data/weekdata_*.xlsx"):
    df = pd.read_excel(f)
    call_data = call_data.append(df,ignore_index=True)
call_data

