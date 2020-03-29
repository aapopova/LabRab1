#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('D:\casc-resto.csv', sep = ';', decimal=',')


# In[2]:


print(df.head())


# In[32]:


print(df.info())


# In[4]:


df.RKDate = df.RKDate = pd.to_datetime(df.RKDate) 


# In[75]:


df["visithappen"]= df['RKDate'].between('2017-07-01','2017-12-31', inclusive=True)
#df.loc[df['dates'].between('2017-07-01','2017-12-31', inclusive=True)]
print(df.head())


# In[76]:


startdata = pd.to_datetime('2017-07-01')
df['Recency'] = df['RKDate'] - startdata
print(df.head())
#kоличество дней до последнего визита клиента перед зафиксированной датой 2017-07-01


# In[84]:


dflastvisit = df['CustomerID'].unique()
df['RKDate'].max()
print(dflastvisit)

itertools.groupby(by=df['RKDate'].max())


# In[38]:


# Create the empty set: baby_names_2011
df1 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
    if row[0] == '2011':
        # Add the fourth column to the set
        df1.add(row[3])

# Find the difference between 2011 and 2014: differences
differences = df1.difference(baby_names_2014)

# Print the differences
print(differences)


# In[ ]:





# In[ ]:





# In[ ]:




