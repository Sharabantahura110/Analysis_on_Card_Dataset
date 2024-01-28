#!/usr/bin/env python
# coding: utf-8

# # Car DataSet
# Here, The data of different car is given with their specifications.
# The data is available as a CSV file. I have analyzed this dataset using Pandas DataFrame.

# In[1]:


import pandas as pd


# In[2]:


car = pd.read_csv(r"/Users/sharabantahura/Downloads/file.csv")


# In[3]:


car.head()


# In[4]:


car.shape


# # Question
# 
# Instruction(For data cleaning)
# Find all null values in the dataset. If there is any null value in the column, replace it with the mean of that column.

# In[5]:


car.isnull()


# In[6]:


car.isnull().sum()


# In[7]:


car.notnull().sum()


# In[23]:


car['Cylinders'].fillna(car['Cylinders'].mean())


# In[18]:


car['Cylinders'].fillna(car['Cylinders'].mean(), inplace = True)


# In[29]:


car['Make'].fillna(car['Make'].mode()[0], inplace = True)


# In[32]:


car.isnull().sum()


# # Question
# (Baesd on Value Counts)
# Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data?

# In[33]:


car['Make'].value_counts()


# # Question
# (Filtering) 
# Show all the records where Origin is Asia or Europe

# In[34]:


car[car['Origin'].isin(['Asia','Europe'])]


# # Question
# (Removing unwanted records)
# Remove all the records(rows) where Weight is above 4000

# In[35]:


car[~(car['Weight']> 4000)]


# # Question
# 
# (Applying function on a column) Increase all the values of ‘MPG_city’ column by 3.

# In[41]:


car


# In[42]:


car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)


# In[43]:


car


# In[ ]:




