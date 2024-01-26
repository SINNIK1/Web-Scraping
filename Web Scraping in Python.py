#!/usr/bin/env python
# coding: utf-8

# In[11]:


from bs4 import BeautifulSoup
import requests


# In[12]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text , 'html')


# In[13]:


print(soup)


# In[14]:


soup.find_all('table')[1]


# In[15]:


soup.find('table' , class_= "wikitable sortable")


# In[16]:


table = soup.find_all('table')[1]


# In[17]:


print(table)


# In[18]:


soup.find_all('th')


# In[19]:


world_titles = table.find_all('th')


# In[20]:


world_titles


# In[21]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[22]:


import pandas as pd


# In[23]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[24]:


column_data = table.find_all('tr')


# In[28]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[29]:


df


# In[32]:


df.to_csv(r'C:\Users\k9811\OneDrive\Desktop\Result\companies.csv' , index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




