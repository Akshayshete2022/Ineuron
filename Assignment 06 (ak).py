#!/usr/bin/env python
# coding: utf-8

# # Assignment 06

# In[ ]:


get_ipython().set_next_input('1. What are escape characters, and how do you use them');get_ipython().run_line_magic('pinfo', 'them')


# In[ ]:


1)The programmers refer to the "backslash (\)" character as an escape character. 
In other words, it has a special meaning when we use it inside the strings.
2)\v It prints the text next to it in a newline after a tab space. Additionally.
3)\b It removes the character before \b. Moreover.
4)


# In[10]:


print("\"akshay\"")


# In[11]:


print(""Akshay"")


# In[12]:


print('akshay')


# In[ ]:


get_ipython().set_next_input('Q2). What do the escape characters n and t stand for');get_ipython().run_line_magic('pinfo', 'for')


# In[ ]:


Answer:-
\n for the new line 
\t for the hosrizantal tab


# In[ ]:


get_ipython().set_next_input('Q3).What is the way to include backslash characters in a string');get_ipython().run_line_magic('pinfo', 'string')


# In[13]:


s = 'Hey, whats up?'
print(s)


# In[14]:


s = 'Hey, what's up?'
print(s)


# In[15]:


s = 'Hey, what\'s up?'
print(s)


# In[17]:


print("Multiline stringsc can be created using escape sequences.")


# In[18]:


print("Multiline strings\ncan be created\nusing escape sequences.")


# In[ ]:


Q4).The string "Howl's Moving Castle" is a correct value.
get_ipython().set_next_input("Why isn't the single quote character in the word Howl's not escaped a problem");get_ipython().run_line_magic('pinfo', 'problem')


# In[20]:


s= "Howl's Moving Castle"
print(s)


# In[21]:


s1='Howl's Moving Castle'


# beacue the we alredy used in one quote in how's charactors

# In[ ]:


get_ipython().set_next_input("Q5). How do you write a string of newlines if you don't want to use the n character");get_ipython().run_line_magic('pinfo', 'character')


# In[ ]:


By the using the multi line using we can  add the new line in string 


# In[ ]:


get_ipython().set_next_input('Q6). What are the values of the given expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]


# In[23]:


'Hello, world!'[1]


# In[24]:


'Hello, world!'[0:5]


# In[25]:


'Hello, world!'[:5]


# In[26]:


'Hello, world!'[3:]


# In[ ]:


get_ipython().set_next_input('Q7). What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()


# In[27]:


'Hello'.upper()


# In[28]:


'Hello'.upper().isupper()


# In[29]:


'Hello'.upper().lower()


# In[ ]:


get_ipython().set_next_input('Q8). What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Remember, remember, the fifth of July.'.split()
'-'.join('There can only one.'.split())


# In[30]:


'Remember, remember, the fifth of July.'.split()


# In[31]:


'-'.join('There can only one.'.split())


# In[32]:


'There can only one.'.split()


# In[37]:


'**'.join('There can only one.')


# In[ ]:


get_ipython().set_next_input('Q9). What are the methods for right-justifying, left-justifying, and centering a string');get_ipython().run_line_magic('pinfo', 'string')


# In[ ]:


The rjust(), ljust(), and center() string methods, respectively


# In[39]:


s= 'I am the Best'


# In[40]:


s


# In[47]:


print (s.center(50),"*")


# In[48]:


print (s.center(50,'*'),"*")


# In[49]:


print (s.ljust(50,'*'),"*")


# In[50]:


print (s.rjust(50,'*'),"*")


# In[ ]:


get_ipython().set_next_input('Q10). What is the best way to remove whitespace characters from the start or end');get_ipython().run_line_magic('pinfo', 'end')


# In[ ]:


Answer:-
The lstrip() and rstrip() methods remove whitespace from the left and right ends of a string, respectively.


# In[54]:


s='    I am the Best    '
print (s)


# In[55]:


s.lstrip()


# In[56]:


s.rstrip()


# In[57]:


s.strip()


# In[ ]:




