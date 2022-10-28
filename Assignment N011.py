#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1) Create an assert statement that throws an AssertionError if the variable spam is a negative integer.


# In[ ]:


Answer:-


# In[ ]:


assert 1<10,


# In[9]:


x = 10
assert x > 0
print('x is a positive number.')


# In[7]:


x=1
assert x>5,"x is positive "


# In[ ]:


Q2)Write an assert statement that triggers an AssertionError 
if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different 
(that is, 'hello' and 'HELLO' are considered the same, and 'goodbye' and 'GOODBYE' are also considered the same).


# In[20]:


assert eggs.lower()!= bacon.lower(), 'variable considered as same!'


# In[19]:


assert eggs.lower()!= bacon.lower(), 'The eggs and bacon variables are the same!'


# In[ ]:


Q3)Create an assert statement that throws an AssertionError every time.


# In[ ]:


Answer:- Assertion is a programming concept used while writing a code where the user declares
a condition to be true using assert statement prior to running the module. If the condition is True,
the control simply moves to the next line of code. 
In case if it is False the program stops running and returns AssertionError Exception.


# In[3]:


x=10
assert x<0 
print("x is positive")


# In[ ]:


Q4). What are the two lines that must be present in your software in order to call logging.debug()?


# In[ ]:


Answer:-
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
get_ipython().run_line_magic('(levelname)s', "- %(message)s'")


# In[14]:


import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')


# If you’ve ever put a print() statement in your code to output some variable’s value while your program is running, 
# you’ve used a form of logging to debug your code. Logging is a great way to understand what’s happening in your program 
# and in what order it’s happening. Python’s logging module makes it easy to create a record of custom messages that you write. 
# These log messages will describe when the program execution has reached the logging function call and list any variables you 
# have specified at that point in time. On the other hand, a missing log message indicates a part of the code was skipped and 
# never executed

# In[ ]:


Q5). What are the two lines that your program must have in order to have 
get_ipython().set_next_input('logging.debug() send a logging message to a file named programLog.txt');get_ipython().run_line_magic('pinfo', 'programLog.txt')


# In[16]:


import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')


# Writing the logging messages to a file will keep your screen clear and store the messages so you can read them after 
# running the program. You can open this text file in any text editor, such as Notepad or TextEdi

# In[ ]:


get_ipython().set_next_input('Q6). What are the five levels of logging');get_ipython().run_line_magic('pinfo', 'logging')


# In[ ]:


Answer:-1)Debug 2)Info 3)Warning 4)Error5)critical


# In[ ]:


get_ipython().set_next_input('Q7). What line of code would you add to your software to disable all logging messages');get_ipython().run_line_magic('pinfo', 'messages')


# In[ ]:


Answer:- logging.disable(logging.CRITICAL)


# In[ ]:


get_ipython().set_next_input('8)Why is using logging messages better than using print() to display the same message');get_ipython().run_line_magic('pinfo', 'message')


#  Answer:- While logging messages are helpful, they can clutter your screen and make it hard to read the program’s output.
# Writing the logging messages to a file will keep yourscreen clear and store the messages so you can
# read them after  running the program. You can open this text file in any text editor, such as Notepad or TextEdit.

# In[ ]:


get_ipython().set_next_input('Q9). What are the differences between the Step Over, Step In, and Step Out buttons in the debugger');get_ipython().run_line_magic('pinfo', 'debugger')


# In[ ]:


Anwer:- 
    1)Step Over:-Clicking the Step Over button will execute the next line of code, similar to the Step In button. However,
    if the next line of code is a function call, the Step Over button will “step over” the code in the function.
    The function’s code will be executed at full speed, and the debugger will pause as soon as the function call returns. 
    For example, if the next line of code calls a spam() function but you don’t really care about code inside this function, 
    you can click Step Over to execute the code in the function at normal speed, and then pause when the function returns.
    For this reason, using the Over button is more common than using the Step In button.
    2)Step In:-Clicking the Step In button will cause the debugger to execute the next line of code and then pause again. 
    If    the next line of code is a function call, the debugger will “step into” that function and jump to the first line of 
    code of that function.
    3)Strp Out:-Clicking the Step Out button will cause the debugger to execute lines of code at full speed until it returns 
    from the current function. If you have stepped into a function call with the Step In button and now simply want to keep 
    executing instructions until you get back out, click the Out button to “step out” of the current function call


# In[ ]:


Q10).After you click Continue, when will the debugger stop ?


# In[ ]:


Answer:-
    Clicking the Continue button will cause the program to execute normally until it terminates or reaches a breakpoint.


# In[ ]:


get_ipython().set_next_input('Q11) What is the concept of a breakpoint');get_ipython().run_line_magic('pinfo', 'breakpoint')


# In[ ]:


Answer:- breakpoint can be set on a specific line of code and forces the debugger to pause whenever the program 
         execution reaches that line


# In[ ]:





# In[ ]:




