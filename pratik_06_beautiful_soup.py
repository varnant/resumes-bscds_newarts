#!/usr/bin/env python
# coding: utf-8

# In[35]:





# In[42]:


get_ipython().system('pip install mysql-connector-python')




# In[43]:


import requests

from bs4 import BeautifulSoup

import mysql.connector


# In[51]:


def save():
    snm=input("Enter url:")
    response=requests.get(snm)
    soup=  BeautifulSoup (response.text, 'html.parser')
    title= soup.title.string if soup.title else "No title found"
    print(title)
    conn=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password="2121",
    database='websites')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE website titles (site_name VARCHAR(100), title varchar(100)' )
    cursor.execute("INSERT INTO website_titles (site_name, title) VALUES (%s, %s)", (site_name, title))

    conn.commit()
    conn.close()

save()   


# In[ ]:




