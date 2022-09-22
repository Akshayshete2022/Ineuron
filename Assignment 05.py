#!/usr/bin/env python
# coding: utf-8

# #        Assignment 05

# In[ ]:


get_ipython().set_next_input("Q1).What does an empty dictionary's code look like");get_ipython().run_line_magic('pinfo', 'like')


# Answer:-
# we can creat empty dictionary using dic() or {}

# In[ ]:


Q2)What is the value of a dictionary value with the key 'foo' and the value 42?


# In[7]:


{foo:42}


# In[ ]:


get_ipython().set_next_input('Q3)What is the most significant distinction between a dictionary and a list');get_ipython().run_line_magic('pinfo', 'list')


# In[ ]:


in list data stored in order and in dictionry unordered 


# In[ ]:


Q4). What happens if you try to access spam['foo'] if spam is {'bar': 100}?


# In[16]:


spam={'bar':100}


# In[18]:


spam['foo']


# In[ ]:


Q5).If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?


# In[20]:


spam={'cat'}


# In[25]:


spam.key()


# In[ ]:


Q6)If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?


# In[ ]:


Answer:-
'cat' in spam checks whether there is a 'cat' key in the dictionary,
while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.


# In[ ]:


get_ipython().set_next_input('7. What is a shortcut for the following code');get_ipython().run_line_magic('pinfo', 'code')
if 'color' not in spam:
spam['color'] = 'black'


# In[37]:


spam.setdefault('color', 'black')


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q8).How do you "pretty print" dictionary values using which module and function');get_ipython().run_line_magic('pinfo', 'function')


# In[ ]:


Answer:-
Using the pprint.pprint() we can use the pretty print dictionary.

