#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year 
of your fifth birthday. For example, if you were born in 1980. the list 
would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].


# In[1]:


year_list=[1994,1995,1996,1997,1998,1999]


# In[2]:


year_list


# In[ ]:


Q2)In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.


# In[3]:


year_list[2]


# In[ ]:


get_ipython().set_next_input('Q3.In the years list, which year were you the oldest');get_ipython().run_line_magic('pinfo', 'oldest')


# In[5]:


year_list[-1]


# In[8]:


year_list[5]


# In[ ]:


Q4)Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".


# In[10]:


l=['mozzarella','cindrella','salmonella']


# In[11]:


l


# In[ ]:


get_ipython().set_next_input('Q5)Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list');get_ipython().run_line_magic('pinfo', 'list')


# In[21]:


l_cap=l.copy()
l_cap[1].capitalize()


# In[ ]:


Q6)Make a surprise list with the elements "Groucho," "Chico," and "Harpo."


# In[22]:


surprise=["Groucho," "Chico,", "Harpo"]


# In[23]:


surprise


# In[ ]:


Q7)Lowercase the last element of the surprise list, reverse it, and then capitalize it.


# In[27]:


surprise[-1]=surprise[-1].lower()
surprise[-1]=surprise[-1][::-1]
surprise[-1].capitalize()


# In[ ]:


Q8)Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat,
    and walrus is morse.


# In[32]:


e2f={'dog' : 'chien','cat' : 'chat','walrus' : 'morse'}


# In[33]:


e2f


# In[ ]:


Q9) Write the French word for walrus in your three-word dictionary e2f.


# In[40]:


e2f['walrus']


# In[ ]:


Q10)Make a French-to-English dictionary called f2e from e2f. Use the items method.


# In[42]:


e2f


# In[45]:


f2e={}
for english,french in e2f.items():
    f2e[french]=english
f2e


# In[ ]:


get_ipython().set_next_input('Q11) Print the English version of the French word chien using f2e');get_ipython().run_line_magic('pinfo', 'f2e')


# In[46]:


f2e


# In[49]:


f2e['chien']


# In[ ]:


Q12) Make and print a set of English words from the keys in e2f.


# In[52]:


set(e2f.keys())


# In[ ]:


Q13)Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'.
    Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer
    to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries


# In[59]:


life={'animal':{'cats':['henri','grumpy','lucy'],'octopi':{},'emus':{}},'plants':{},'other':{}}


# In[60]:


life


# In[ ]:


Q14)Print the top-level keys of life.


# In[62]:


life.keys()


# In[ ]:


Q15)Print the keys for life['animals'].


# In[65]:


life['animal'].keys()


# In[ ]:


Q16) Print the values for life['animals']['cats']


# In[72]:


print(life['animal']['cats'])


# In[ ]:




