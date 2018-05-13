
# coding: utf-8

# In[1]:


#P.92

import pandas as pd

ser = pd.Series([1,2,3], index = ['a','b','c'])
ser


# In[2]:


pd.Series([1,2,3])
#indexを利用しないVerだと自動で０，１，２が付与される


# In[3]:


ser.loc['b']


# In[4]:


ser['b']
#locを利用しなくてもOK


# In[5]:


ser.loc['b':'c']
#スライスすることもできる


# In[6]:


ser.loc[['a','c']]
#[]が一つだとエラーになる
#[[]]が二つ必要→リスト化させる


# In[7]:


ser.loc['a','c']


# In[9]:


ser.iloc[1]


# In[11]:


ser.iloc[1:3]
#位置をスライスしたVer


# In[12]:


ser.loc[[True,False,True]]
#Trueのみ表示される


# In[13]:


ser !=2
#Seriesに対して比較演算をすることで、真偽値が返る。


# In[16]:


ser.loc[ser != 2]

