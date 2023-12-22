#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np


# In[31]:


import pandas as pd


# In[32]:


import seaborn as sns


# In[33]:


import matplotlib.pyplot as plt


# In[34]:


df = pd.read_csv('wpopulation.csv')


# In[35]:


df


# In[36]:


# shape check
df.shape


# In[37]:


df.info()


# In[38]:


df.describe()


# In[39]:


df.isna().sum()


# In[42]:


# Assuming 'data' is your DataFrame
missing_values = df.isnull().sum()
print(missing_values)


# In[43]:


# Drop unuseful columns
df.drop(columns=['Country Code','Indicator Name'],inplace=True)


# In[ ]:


df.sample()


# In[44]:


# filter data for total population
total_population_df=df[df['Indicator Code']=='SP.POP.TOTL']
total_population_df


# In[45]:


# sort data based on total population for 2022
total_population_sort = total_population_df.sort_values(by='2022',ascending=False)
total_population_sort


# Top 10 countries with the highest population for 2022

# In[46]:


# get top 10 countries with the highest population for 2022
top_ten_countries = total_population_sort.head(10)
print("Top Ten Counteies Of Total Population:-")
print(top_ten_countries)


# In[47]:


# Data visualization
def add_value_labels(ax,spacing=10):
    for rect in ax.patches:
        x=rect.get_x()+rect.get_width()/2
        y=rect.get_height()-3
        
        va='bottom' if y>=0 else 'top'
        label= '()'.format(y) 
        y_shift = spacing * (1 if y >= 0 else -1)
        ax.annotate(label,(x,y),xytext=(0,y_shift),textcoords="offset points",ha='center',va=va)


# In[48]:


#DATA VISUALIZATION


# In[49]:


# creat a bar plot
plt.figure(figsize=(20,13))
plt.rcParams['axes.facecolor']=="green"

plt.subplot(2,2,1)
plot=sns.barplot(x='2022',y="Country Name",data=top_ten_countries,palette="coolwarm")
plt.title("Top Ten countries Of Total Population (2022)")
plt.xlabel("Total population")
plt.ylabel("country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2000',y="Country Name",data=top_ten_countries,palette="coolwarm")
plt.title("Top Ten countries Of Total Population in 2000")
plt.xlabel("Total population")
plt.ylabel("country")
add_value_labels(plot)

plt.tight_layout()


# In[50]:


# creat a bar plot
plt.figure(figsize=(20,13))
plt.rcParams['axes.facecolor']=="black"

plt.subplot(2,2,1)
plot=sns.barplot(x='1999',y="Country Name",data=top_ten_countries,palette="coolwarm")
plt.title("Top Ten countries Of Total Population (1999)")
plt.xlabel("Total population")
plt.ylabel("country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='1989',y="Country Name",data=top_ten_countries,palette="coolwarm")
plt.title("Top Ten countries Of Total Population in 1989")
plt.xlabel("Total population")
plt.ylabel("country")
add_value_labels(plot)

plt.tight_layout()


# In[51]:


# creat a bar plot
plt.figure(figsize=(20,13))
plt.rcParams['axes.facecolor']=="black"

plt.subplot(2,2,1)
plot=sns.barplot(x='1960',y="Country Name",data=top_ten_countries,palette="coolwarm")
plt.title("Top Ten countries Of Total Population (1999)")
plt.xlabel("Total population")
plt.ylabel("country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2022',y="Country Name",data=top_ten_countries,palette="coolwarm")
plt.title("Top Ten countries Of Total Population in 1989")
plt.xlabel("Total population")
plt.ylabel("country")
add_value_labels(plot)

plt.tight_layout()


# In[52]:


# sort data based on total population for 2022
total_population_sort_bt = total_population_df.sort_values(by='2022',ascending=True)
total_population_sort_bt


# In[53]:


top_ten_bt_countries = total_population_sort_bt.head(10)
print("Top Ten Bottom Counteies Of Total Population:-")
print(top_ten_bt_countries)


# In[54]:


plt.figure(figsize=(20,13))
plt.rcParams['axes.facecolor']=="black"

plt.subplot(2,2,1)
plot=sns.barplot(x='2022',y="Country Name",data=top_ten_bt_countries,palette="coolwarm")
plt.title("Top Ten Bottom countries Of Total Population (2022)")
plt.xlabel("Total population")
plt.ylabel("country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2000',y="Country Name",data=top_ten_bt_countries,palette="coolwarm")
plt.title("Top Ten Bottom countries Of Total Population in 2000")
plt.xlabel("Total population")
plt.ylabel("country")
add_value_labels(plot)

plt.tight_layout()


# In[ ]:





# In[ ]:




