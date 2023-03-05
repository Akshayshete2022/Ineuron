#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment 03
# 

# In[ ]:


get_ipython().set_next_input('1.)Write a Python Program to Check if a Number is Positive, Negative or Zero');get_ipython().run_line_magic('pinfo', 'Zero')


# In[1]:


num=float(input("Enter the number:"))
if num >0:
    print("number is positive")
elif num ==0:
    print("zero")
else:
    print("number is negative")
    


# In[ ]:


get_ipython().set_next_input('2)Write a Python Program to Check if a Number is Odd or Even');get_ipython().run_line_magic('pinfo', 'Even')


# In[1]:


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[ ]:


get_ipython().set_next_input('3)Write a Python Program to Check Leap Year');get_ipython().run_line_magic('pinfo', 'Year')


# In[2]:


year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")


# In[ ]:


get_ipython().set_next_input('4)Write a Python Program to Check Prime Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[5]:


if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")


# In[ ]:


5)Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


# In[7]:



lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:





# In[ ]:




