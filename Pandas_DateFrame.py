
# coding: utf-8

# In[1]:


#P.95


import pandas as pd

df = pd.DataFrame(
    [[1,10,100],[2,20,200],[3,30,300]],
    index = ['r1','r2','r3'],
    columns = ['c1','c2','c3'])
df


# In[2]:


df.loc['r2','c2']
#loc[行、列]で指定することで値を呼び出せる。


# In[3]:


df.loc['r2',:]


# In[5]:


df.loc[:,'c2']


# In[8]:


df.loc[['r1','r3'],'c2':'c3']


# In[9]:


df.iloc[1:3,[0,2]]
#行の位置を数字で指定もできる


# In[10]:


df['c2']
#[]のみで指定もできる


# In[12]:


df>10
#DataFrameも比較演算できる。


# In[13]:


#C2列の値が、10より大きいデータ
df.loc[df['c2'] >10]


# In[14]:


#C1が1より大きく、C3列が300より小さいデータ
df.loc[(df['c1']>1)&(df['c3']<300)]
#真ん中は「＆」を利用する。

