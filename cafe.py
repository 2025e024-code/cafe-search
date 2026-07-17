#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px


# In[2]:


df = pd.read_csv("cafe.csv")


# In[3]:


df.head()


# In[4]:


df.columns


# In[5]:


df = df[[
    "Title",
    "crating_val",
    "Number",
    "Avg_price1",
    "Title_URL"
]]

df.head()


# In[6]:


df.columns = [
    "店名",
    "評価",
    "口コミ数",
    "予算",
    "URL"
]

df.head()


# In[7]:


df.iloc[0]


# In[8]:


df.info()


# In[9]:


df.sort_values("評価", ascending=False).head(10)


# In[10]:


fig = px.bar(
    df.sort_values("評価", ascending=False).head(10),
    x="店名",
    y="評価",
    title="評価が高いカフェ TOP10"
)

fig.show()


# In[11]:


fig = px.scatter(
    df,
    x="口コミ数",
    y="評価",
    hover_name="店名",
    title="口コミ数と評価の関係"
)

fig.show()


# In[ ]:




