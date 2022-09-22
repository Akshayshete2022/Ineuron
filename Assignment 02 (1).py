#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('Q)1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')


# True and false it can be written as 'T' for True and 'F' for False

# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')


# and,or,not these are the different types of boolean operators

# In[ ]:


3. Make a list of each Boolean operator's truth tables 
(i.e. every possible combination of Boolean values for the operator and what it evaluate ).


# In[ ]:


Answer:- 
'T' and 'T' is 'T'
'T' and 'F' is 'F'
'F'and 'T' is 'F'
'F'and 'F'is 'F'
'T'or 'T' is 'T'
'T'or 'F'is 'T'
'F'or 'T'is'T'
'F'or 'F'is 'F'
not 'T'is 'F'
not 'F'is 'T'


# In[ ]:


get_ipython().set_next_input('Q4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
  


# In[ ]:


Answer:-

(5 > 4) and (3 == 5)  is 'False'
not (5 > 4)           is 'False'
(5 > 4) or (3 == 5)   is 'True'
not((5 > 4) or (3 == 5)) is 'True'
(True and True) and (True == False) is 'False'
(not False) or (not True) is  'True'


# In[ ]:


get_ipython().set_next_input('Q5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')


# In[ ]:


Answer:-
less than (<)
less than or equal to(<=)
gretar than(>)
gretar than equal to (>=)
Eqaul to (==)
Not equal to(!=)
this are the comparison operators use for int and string 


# In[ ]:


get_ipython().set_next_input('6. How do you tell the difference between the equal to and assignment operators');get_ipython().run_line_magic('pinfo', 'operators')
Describe a condition and when you would use one.


# In[ ]:


= 
Its is an assiagnment operator
it is use as assigning the value.
1=x : invalid couse constant term can not on left side
    
==
It is an Comparison operator.
it is used for comparing the operators 
it will return 1 if both are equal or 0


# In[1]:


a=10


# In[2]:


a


# In[3]:


5==5


# In[ ]:


Q7). Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')


# In[5]:


spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, 
prints Howdy if 2 is stored in spam, 
and prints Greetings! if anything else is stored in spam.


# In[9]:


spam=input("enter the number ")
if spam=="1":
    print ("hellow")
elif spam=="2":
    print ("howdy")
else:
    print("Greetings!")


# In[ ]:


get_ipython().set_next_input('Q9)If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')


# In[ ]:


Answer:-
it only stop by external intervision by pressing the CTRL+ C.


# In[ ]:


get_ipython().set_next_input('Q10). How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')


# Break statement :-1) its stop the loop .
#                   2)when the break statement is executed the starement after the content of the loop are executed.
#         
# Continue Statement :- 1) It Instruct a loop to continue to the next iteration
#                       2)Continue statement dose not halt a loop.

# In[ ]:


Q)11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?


# In[10]:


for i in range(10):
    print (i,end=" ")
print()


# In[11]:


for i in range(0,10):
    print (i,end=" ")
print()


# In[12]:


for i in range(0,10,1):
    print (i,end=" ")
print()


# In[ ]:


1)Range is by defoult of unit place iteration and start from 0
2)by defoult its unit place iteration.
3)we set the conditions


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. 
Then write an equivalent program that prints the numbers 1 to 10 using a while loop.


# In[16]:


for i in range (1,11):
    print(i, end=" ")


# In[1]:


i=1
while (i<=10):
    print(i)
    i=i+1
    
    


# In[ ]:


get_ipython().set_next_input('Q13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')


# In[ ]:


Answer:-
spam.bacon()

