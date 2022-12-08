#!/usr/bin/env python
# coding: utf-8

# # Assignment 15

# In[ ]:


Q1)How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of seconds
in a minute (60) by the number of minutes in an hour (also 60).
sol. 60 


# In[ ]:


Answer:-
   1) we can say that the interactive shell is between the user and the operating system 
    (e.g. Linux, Unix, Windows or others). Instead of an operating system an interpreter can be used for a programming 
    language like Python as well. The Python interpreter can be used from an interactive shell.


# In[16]:


seconds=60
minuteshour=60
print(seconds *minuteshour)


# In[22]:


60*60


# In[ ]:


2. Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.


# In[24]:


print('second_per_houre = seconds*minuteshour')


# In[ ]:


Q3)How many seconds do you think there are in a day? Make use of the variables seconds per hour and minutes per hour.


# In[ ]:


Answer:-


# In[6]:


def seconds_per_hour(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds
print(seconds_per_hour(1))      


# In[4]:


def minutes_per_hour(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return minutes
print(minutes_per_hour(1)) 


# In[ ]:


4. Calculate seconds per day again, but this time save the result in a variable called seconds_per_day


# In[1]:


def seconds_per_day(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds
print(seconds_per_day(1)) 


# In[ ]:


5.Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.


# In[21]:


60*60


# In[25]:


seconds_per_hour = 3600


# In[32]:


seconds_per_hour*24


# In[38]:


seconds_per_day=seconds_per_hour*24
seconds_per_day


# In[40]:


seconds_per_day/seconds_per_hour


# In[ ]:


Q6.)Divide seconds_per_day by seconds_per_hour, using integer (//) division. 
Did this number agree with the floating-point value from the previous question, aside from the final .0?


# In[41]:


seconds_per_day//seconds_per_hour


# In[ ]:


Q7)Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next()
method: 2, 3, 5, 7, 11, ...


# In[44]:


def genPrimes():
    
    primes = [ 2, 3, 5, 7, 11 ]
    
    def isPrimeNumber(n):
        if n in primes:
            return True
        
        for elem in primes:
            if n % elem == 0:
                return False
                
        primes.append(n)
        return True
    num = 1
    while True:
        num += 1
        if isPrimeNumber(num):
            next = num
            yield next
            num = next
primeNumber = genPrimes()

for i in range(189):
    print(primeNumber.__next__())


# In[ ]:




