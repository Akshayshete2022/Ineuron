#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment 04
# 

# In[ ]:


get_ipython().set_next_input('1)Write a Python Program to Find the Factorial of a Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[4]:


num = int(input("Enter a number: "))

factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[ ]:


get_ipython().set_next_input('2)Write a Python Program to Display the multiplication Table');get_ipython().run_line_magic('pinfo', 'Table')


# In[6]:


num = int(input("Display multiplication table of? "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# In[8]:


num=int(input("display multiplication table of "))
for i in range(1,12):
    print(num,'x',i,'=',num*i)


# In[ ]:


get_ipython().set_next_input('3)Write a Python Program to Print the Fibonacci sequence');get_ipython().run_line_magic('pinfo', 'sequence')


# In[9]:


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# In[ ]:


get_ipython().set_next_input('4)Write a Python Program to Check Armstrong Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[ ]:



num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[ ]:


get_ipython().set_next_input('5)Write a Python Program to Find Armstrong Number in an Interval');get_ipython().run_line_magic('pinfo', 'Interval')


# In[10]:


lower = 100
upper = 2000

for num in range(lower, upper + 1):
   order = len(str(num))
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


# In[ ]:


get_ipython().set_next_input('6)Write a Python Program to Find the Sum of Natural Numbers');get_ipython().run_line_magic('pinfo', 'Numbers')


# In[1]:


num = 20
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# In[ ]:





# In[ ]:




