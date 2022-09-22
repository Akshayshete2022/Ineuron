#!/usr/bin/env python
# coding: utf-8

# # Assignment 04

# In[ ]:


Q1) What exactly is []?


# In[ ]:


[] it is list which contains the mutable collection now its empty


# In[ ]:


2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? 
(Assume [2, 4, 6, 8, 10] are in spam.)


# In[2]:


spam=[2, 4, 6, 8, 10]


# In[3]:


spam[2]='hello'


# In[4]:


spam


# Q3,4,5)Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

# Q3) What is the value of spam[int(int('3' * 2) / 11)]?

# In[4]:


spam=['a','b','c','d']
spam[int(int('3' * 2) / 11)]


# Q4). What is the value of spam[-1]?

# In[2]:


spam[-1]


# Q5). What is the value of spam[2]?

# In[3]:


spam[2]


# Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.

# In[ ]:


Q6. What is the value of bacon.index('cat')?


# In[7]:


bacon=[3.14, 'cat',11, 'cat,' 'True']


# In[8]:


bacon


# In[9]:


bacon.index('cat')


# In[ ]:


get_ipython().set_next_input('Q7). How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')


# In[10]:


bacon.append(99)


# In[11]:


bacon


# In[ ]:


get_ipython().set_next_input("Q8). How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')


# In[12]:


bacon.remove('cat')


# In[13]:


bacon


# Q9). What are the list concatenation and list replication operators?

# In[ ]:


Answer:-
''+'' is the concatenation operator and ''*'' is replication operators


# Q10). What is difference between the list methods append() and insert()?

# Answer:-
# s.append(*)is,* to add in end of the list,
# s.insert(*)is ,* to insert in the list.

# Q11). What are the two methods for removing items from a list?

#  Answer:-
#  by the using s.pop() and s.remove()

# In[ ]:


Q12.) Describe how list values and string values are identical.


# In[ ]:


1)Lists are similar to strings, which are ordered collections of characters
2)it can be usd for in and not operator


# In[ ]:


get_ipython().set_next_input("Q13.) What's the difference between tuples and lists");get_ipython().run_line_magic('pinfo', 'lists')


# In[ ]:


Answer:-
list:- list is mutable and use by [ ]
Tuples :- tuple is immutable use by ()


# In[ ]:


Q14). How do you type a tuple value that only contains the integer 42?


# In[16]:


tuple=(42)


# In[17]:


tuple


# In[ ]:


get_ipython().set_next_input("Q15). How do you get a list value's tuple form? How do you get a tuple value's list form");get_ipython().run_line_magic('pinfo', 'form')


# In[36]:


l1=(1,2)


# In[37]:


l1


# In[39]:


l=list(l1)


# In[40]:


l


# In[ ]:


get_ipython().set_next_input('Q16.) Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain');get_ipython().run_line_magic('pinfo', 'contain')


# In[ ]:


Answer:-
They contain references to list values


# In[ ]:


Q17). How do you distinguish between copy.copy() and copy.deepcopy()?


# In[59]:


copy=[1,2,3]


# In[60]:


copy.copy()


# In[ ]:


s=[1,2,3,]
copy.deepcopy(s)
this function is copy the list into list 
this function copy the deep 


# In[ ]:




