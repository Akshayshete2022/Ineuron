#!/usr/bin/env python
# coding: utf-8

# # Assignment 08

# In[ ]:


get_ipython().set_next_input('Q1).Is the Python Standard Library included with PyInputPlus');get_ipython().run_line_magic('pinfo', 'PyInputPlus')


# In[ ]:


Answer:-
    PyInputPlus is not a part of the Python Standard Library,for installation use Pip function 


# In[ ]:


get_ipython().set_next_input('Q2. Why is PyInputPlus commonly imported with import pyinputplus as pypi');get_ipython().run_line_magic('pinfo', 'pypi')


# In[ ]:


Answer:-
    The as pyip code in the import statement saves us from typing pyinputplus each time
    we want to call a PyInputPlus function. Instead we can use the shorter pyip name


# In[ ]:





# In[ ]:


Q3. How do you distinguish between inputInt() and inputFloat()?


# In[ ]:


Answer:-
     inputInt()  :  Accepts only integer value, and returns int value
    inputFloat() : Accepts integer/floating point value and returns float value.


# In[ ]:





# In[ ]:


Q4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?


# In[ ]:


Answer:-
    In the inputint function we can set the min = 0 and max =99 to ensure user enters number between 0 and 99


# In[ ]:


get_ipython().set_next_input('Q5. What is transferred to the keyword arguments allowRegexes and blockRegexes');get_ipython().run_line_magic('pinfo', 'blockRegexes')


# In[ ]:


Answer:-
    We can also use regular expressions to specify whether an input is allowed or not. The allowRegexes and 
    blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus
    function will accept or reject as valid input.


# In[ ]:


get_ipython().set_next_input('Q6. If a blank input is entered three times, what does inputStr(limit=3) do');get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


Answer:-
    it will throw RetryLimitException exception.


# In[ ]:


get_ipython().set_next_input("Q7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do");get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


Answer:-
    When you use limit keyword arguments and also pass a default keyword argument,
   the function returns the default value instead of raising an exception


# In[ ]:





# In[ ]:




