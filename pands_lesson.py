
# coding: utf-8

# In[7]:


#P.85
import os 

base_url = 'http://raw.githubusercontent.com/practical-jupyter/sample-data/master/anime/'
anime_csv=os.path.join(base_url,'anime.csv')

print(anime_csv)


# In[8]:


#86
import pandas as pd

anime_csv = os.path.join(base_url, 'anime.csv')
pd.read_csv(anime_csv).head()
#head()はデフォルトで5コ表示する


# In[10]:


anime_master_csv = os.path.join(base_url,'anime_master.csv')
pd.read_csv(anime_master_csv).head()


# In[12]:


anime_split_genre_csv = os.path.join(base_url,'anime_split_genre.csv')
pd.read_csv(anime_split_genre_csv).head()


# In[15]:


anime_genre_top10_csv = os.path.join(base_url,'anime_genre_top10.csv')
pd.read_csv(anime_genre_top10_csv).head()


# In[17]:


anime_genre_top10_pivoted_csv = os.path.join(base_url,'anime_genre_top10_pivoted.csv')
pd.read_csv(anime_genre_top10_pivoted_csv).head()


# In[18]:


anime_stock_price_csv = os.path.join(base_url,'anime_stock_price.csv')
pd.read_csv(anime_stock_price_csv).head()


# In[19]:


a = pd.read_csv(anime_stock_price_csv).head()


# In[20]:


a.Date


# In[22]:


for i in a.Date:
    print(i) 


# In[26]:


anime_stock_returns_csv = os.path.join(base_url,'anime_stock_returns.csv')
pd.read_csv(anime_stock_returns_csv,index_col = 0, parse_dates =['Date']).head()


# In[28]:


t4816_csv = os.path.join(base_url,'4816.csv')
pd.read_csv(t4816_csv, index_col = 0, parse_dates=['Date']).head()

