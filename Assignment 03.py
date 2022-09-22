#!/usr/bin/env python
# coding: utf-8

# Assignment03

# In[ ]:


get_ipython().set_next_input('Q1.) Why are functions advantageous to have in your programs');get_ipython().run_line_magic('pinfo', 'programs')


# Answer:-
# it makes the program easier,shorter to read and easier to update 

# Q2). When does the code in a function run: when it's specified or when it's called?

# In[ ]:


Answer:-
Code in the function run when function is called not when the function is defined


# In[ ]:


get_ipython().set_next_input('Q3). What statement creates a function');get_ipython().run_line_magic('pinfo', 'function')


# Function can be defined as named group og instruction that accomplish a specific task when it is invoked. once defined , a function can be called repeatedly from diffrent places of the program without wirting the all codes.

# In[ ]:


get_ipython().set_next_input('Q4). What is the difference between a function and a function call');get_ipython().run_line_magic('pinfo', 'call')


# Answer:-
# Function:-      A function consist of the def statement and the code in its def clause
# Function call:- A function call is what is the prgram execution into the functiom and
#                 the function call evaluates th the fuction return value

# In[ ]:


get_ipython().set_next_input('5. How many global scopes are there in a Python program? How many local scopes');get_ipython().run_line_magic('pinfo', 'scopes')


# In[ ]:


Answer:-
There is one global scope, and a local is crated whenever a function is called its created 


# In[ ]:


get_ipython().set_next_input('Q)6. What happens to variables in a local scope when the function call returns');get_ipython().run_line_magic('pinfo', 'returns')


# In[ ]:


Answer:-
    when function rturn,the local scope destoryed and all variable in it are forgotten


# In[ ]:


get_ipython().set_next_input('Q7). What is the concept of a return value? Is it possible to have a return value in an expression');get_ipython().run_line_magic('pinfo', 'expression')


# In[ ]:


Answer:-
A return value is the value that a function call evalueats to.
like any value a return value can be used as part of an expression


# In[ ]:


get_ipython().set_next_input('Q8) If a function does not have a return statement, what is the return value of a call to that function');get_ipython().run_line_magic('pinfo', 'function')


# In[ ]:


Answer:-
there is no any return  statement for a function and none the return values


# In[ ]:


get_ipython().set_next_input('Q9) How do you make a function variable refer to the global variable');get_ipython().run_line_magic('pinfo', 'variable')

Answer:-
global statement will force in variable in a function to refer to global variable
# In[ ]:


get_ipython().set_next_input('Q10). What is the data type of None');get_ipython().run_line_magic('pinfo', 'None')


# In[ ]:


Answer:-
    1)None is a special data type with single value.
    it is used to signify the absence of value in a situation none supports no special
    operation and it is niether same as false nor 0. used as none.type 


# In[ ]:


get_ipython().set_next_input('Q11) What does the sentence import are all your pets name deric do');get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q12) If you had a bacon() feature in a spam module, what would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')


# In[ ]:


after the importing it called as Spam.bacon()


# In[ ]:


get_ipython().set_next_input('Q13) What can you do to save a programme from crashing if it encounters an error');get_ipython().run_line_magic('pinfo', 'error')


# In[ ]:


Answer:-
We use the try and except to handle exceptions.contorl passed to the except blcok skipping the code in between


# In[ ]:


get_ipython().set_next_input('Q14). What is the purpose of the try clause? What is the purpose of the except clause');get_ipython().run_line_magic('pinfo', 'clause')


# In[ ]:


Try and except are used to handle the error in our python program
1)try is used for check the code errors.the code inside the try block will execute when there is no error in the program.
2)Whereas the code inside the except block will execute whenever the program encounters some error in the preceding try block.


# In[ ]:




