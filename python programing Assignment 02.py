#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment 02

# In[ ]:


get_ipython().set_next_input('1.Write a Python program to convert kilometers to miles');get_ipython().run_line_magic('pinfo', 'miles')


# In[7]:


kilometers=float(input('enter the kilometer value:'))
Conv=0.6211
miles=kilometers*Conv
print( '%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# In[ ]:


get_ipython().set_next_input('2.Write a Python program to convert Celsius to Fahrenheit');get_ipython().run_line_magic('pinfo', 'Fahrenheit')


# In[9]:


celsius=float(input('enter the celsius value:'))
fahrenheit=(celsius*1.8)+32
print('%0.1f fahrenheit is equal to %0.1f celsius'%(fahrenheit,celsius))


# In[ ]:


get_ipython().set_next_input('3)Write a Python program to display calendar');get_ipython().run_line_magic('pinfo', 'calendar')


# In[11]:


import calendar


# In[14]:


yy=2023
mm=1
print(calendar.month(yy,mm))


# In[ ]:


get_ipython().set_next_input('4.)Write a Python program to solve quadratic equation');get_ipython().run_line_magic('pinfo', 'equation')


# In[18]:


import cmath

a = 2
b = 4
c = 12
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# In[ ]:


get_ipython().set_next_input('5.)Write a Python program to swap two variables without temp variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[21]:


a = 11
b = 7

a, b = b, a

print(a)
print(b)


# In[ ]:




