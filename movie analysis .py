#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


data =pd.read_csv (r"C:\Users\ASUS\Desktop\IMDB-Movie-Data.csv")


# In[5]:


data.head(10)


# In[6]:


data.tail(10)


# In[7]:


data.shape


# In[8]:


print("number of rows",data.shape[0])
print("number of columns",data.shape[1])


# In[9]:


data.info()


# In[10]:


print ("any missing value?",data.isnull().values.any())


# In[11]:


data.isnull().sum()


# In[12]:


sns.heatmap(data.isnull())


# In[13]:


per_missing = data.isnull().sum()*100/len(data)
per_missing


# In[14]:


data.dropna(axis=0)


# In[15]:


dup_data = data.duplicated().any()


# In[16]:


print ("are there any duplicate values?",dup_data)


# In[17]:


data = data.drop_duplicates()
data


# In[18]:


data.describe(include="all")


# In[19]:


data.columns


# In[20]:


data[ data[ 'Runtime (Minutes)']>=180]['Title']


# In[21]:


data.groupby('Year') ['Votes'].mean().sort_values(ascending= False)


# In[22]:


sns.barplot(x='Year',y='Votes',data=data)
plt.title("votes by year")


# In[23]:


data.columns


# In[24]:


data.groupby('Year') ['Revenue (Millions)'].mean().sort_values(ascending= False)


# In[25]:


sns.barplot(x='Year',y='Revenue (Millions)',data=data)
plt.title("Revenue by year")
plt.show()


# In[26]:


data.columns


# In[27]:


data.groupby( 'Director')['Rating'].mean().sort_values(ascending= False)


# In[28]:


data.columns


# In[29]:


top10_len = data.nlargest(10, 'Runtime (Minutes)') [['Title','Runtime (Minutes)']]\
.set_index('Title')


# In[30]:


top10_len


# In[31]:


sns.barplot(x='Runtime (Minutes)',y=top10_len.index,data=top10_len)


# In[32]:


data.columns


# In[33]:


data['Year'].value_counts()


# In[34]:


sns.countplot(x='Year',data=data)
plt.title("Number of movies per year")
plt.show()


# In[35]:


data.columns


# In[36]:


data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]['Title']


# In[37]:


data.columns


# In[38]:


top10_len = data.nlargest(10, 'Rating') [['Title', 'Rating', 'Director']]\
.set_index('Title')


# In[39]:


top10_len


# In[40]:


sns.barplot(x= 'Rating',y=top10_len.index,data=top10_len,hue= 'Director',dodge=False)
plt.legend(bbox_to_anchor=(1.05,1),loc=2)


# In[41]:


data.columns


# In[42]:


data.nlargest(10,'Revenue (Millions)')[ 'Title']


# In[43]:


top_10= data.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']].\
 set_index('Title')


# In[44]:


top_10


# In[45]:


sns.barplot(x='Revenue (Millions)',y=top_10.index,data=top_10)
plt.title("Top 10 Highest Revenue Movies titles")
plt.show()


# In[46]:


data.columns


# In[47]:


data.groupby('Year')['Rating'].mean().sort_values(ascending=False)


# In[48]:


sns.scatterplot(x='Rating',y='Revenue (Millions)',data=data)


# In[57]:


def rating(rating):
    if rating>=7.0:
         return"Excellent"
    elif rating>=6.0:
         return"Good"
    else:
         return"Average"


# In[58]:


data['Rating_cat']=data['Rating'].apply(rating)


# In[59]:


data.head()


# In[60]:


data['Genre'].dtype


# In[61]:


len(data[data[ 'Genre'].str.contains('Action',case=False)])


# In[62]:


data['Genre']


# In[63]:


list1=[]
for value in data['Genre']:
 list1.append(value.split(','))


# In[64]:


list1


# In[65]:


one_d=[]
for item in list1:
    for item1 in item:
       one_d.append(item1)


# In[66]:


one_d


# In[67]:


uni_list=[]
for item in one_d:
    if item not in uni_list:
        uni_list.append(item)


# In[68]:


uni_list


# In[69]:


one_d=[]
for item in list1:
    for item1 in item:
     one_d.append(item1)


# In[70]:


one_d


# In[ ]:




