#!/usr/bin/env python
# coding: utf-8

# # Assignment 17

# In[ ]:


Q1. Assign the value 7 to the variable guess_me. Then, write the conditional tests 
(if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and
'just right' if equal to 7


# In[2]:


guess_me=7
if guess_me<7:
    print('too low')
elif guess_me>7:
    print('too high')
else:
    print('just right')


# In[ ]:


Q2). Assign the value 7 to the variable guess_me and the value 1 to the variable start.
Write a while loop that compares start with guess_me. Print too low if start is less than guess me. 
If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and 
exit the loop. Increment start at the end of the loop.


# In[1]:


guess_me=7
start=1
while True:
    if guess_me<start:
        print('too low')
    elif guess_me==start:
        print('found it!')
        break
    elif guess_me>start:
        print('oops')
        break
    start+=1


# In[2]:


guess_me=7
start=1
while True:
    if start<guess_me:
        print('too low')
    elif guess_me==start:
        print('found it!')
        break
    elif start>guess_me:
        print('oops')
        break
    start+=1


# In[ ]:


Q3)Print the following values of the list [3, 2, 1, 0] using a for loop.


# In[4]:


i=[3, 2, 1, 0]
for value in i:
    print(value)


# In[ ]:


Q4).Use a list comprehension to make a list of the even numbers in range(10)


# In[23]:


l1=[0,1,2,3,4,5,6,7,8,9,10]
for num in l1:
    if num %2 ==0:
        print(num,end='  ')


# In[24]:


list=[number for number in range(10)if number %2==0]
list


# In[ ]:


Q5)Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys,
and use the square of each key as its value.


# In[31]:


square={key:key*key for key in range(10)}
square


# In[ ]:


Q6)Construct the set odd from the odd numbers in the range using a set comprehension (10).


# In[35]:


odd=(number for number in range(10) if number%2==1)
odd


# In[37]:


odd={number for number in range(10) if number%2==1}
odd


# In[ ]:


Q7). Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). 
Iterate through this by using a for loop.


# In[38]:


for thing in ('Got %s' % number for number in range(10)):
    print(thing)


# In[ ]:


Q8)Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].


# In[39]:


def good():
    return['Harry', 'Ron', 'Hermione']
good()


# In[ ]:


Q9)Define a generator function called get_odds that returns the odd numbers from range(10).
Use a for loop to find and print the third value returned.


# In[40]:


def get_odds():
    for number in range(1, 10, 2):
        yield number
count = 1
for number in get_odds():
    if count == 3:
        print("The third odd number is", number)
        break
    count += 1


# In[ ]:


Q10)Define an exception called OopsException. Raise this exception to see what happens. 
Then write the code to catch this exception and print 'Caught an oops'.


# In[41]:


try:
    raise OopsException
except OopsException:
    print('Caught an oops')


# In[42]:


class OopsException(Exception):
    pass
raise OopsException()


# In[43]:


try:
    raise OopsException
except OopsException:
    print('Caught an oops')


# In[ ]:


Q11).Use zip() to make a dictionary called movies that pairs these lists: 
    titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].


# In[3]:


titles=['creature of habit','crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies=dict(zip(titles,plots))
movies


# In[ ]:





# In[ ]:




