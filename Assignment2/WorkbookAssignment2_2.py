#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine

# Connect to sqlite db
db_file = r'datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
                       .format(db_file))
sql = 'SELECT * FROM scores'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df

