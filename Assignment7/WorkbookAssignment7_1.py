#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
columns=['Names', 'Grades'])

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
df.plot()
displayText = "Wow!"
xloc = 0
yloc = df['Grades'].min()
xtext = 30
ytext = -5
plt.annotate(displayText,
xy=(xloc, yloc),
xytext=(xtext,ytext),
arrowprops=dict(facecolor='green',
shrink=0.05),
xycoords=('axes fraction', 'data'),
textcoords='offset points')


# In[ ]:




