#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.


# In[1]:


test1 = 'This is a test of the emergency text system'
len(test1)


# In[2]:


with open('test1.txt', 'wt') as outfile:
    outfile.write(test1)


# In[3]:


outfile.close()


# In[ ]:


2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?


# In[4]:


with open('test.txt', 'rt') as infile:
    test2 = infile.read()
len(test2)


# In[5]:


test1 == test2


# In[ ]:


3.Create a CSV file called books.csv by using these lines:
title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992


# In[6]:


text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open('books.csv', 'wt') as outfile:
    outfile.write(text)


# In[ ]:


4. Use the sqlite3 module to create a SQLite database called books.db, 
and a table called books with these fields: title (text), author (text), and year (integer).


# In[3]:


import sqlite3
db = sqlite3.connect('books.db')
curs = db.cursor()
curs.execute('''create table book (title text, author text, year int)''')


# In[4]:


db.commit()


# In[ ]:


5. Read books.csv and insert its data into the book table.


# In[5]:


import csv
import sqlite3
ins_str = 'insert into book values(?, ?, ?)'
with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))


# In[6]:


db.commit()


# In[ ]:


6. Select and print the title column from the book table in alphabetical order.


# In[7]:


sql = 'select title from book order by title asc'
for row in db.execute(sql):
    print(row)


# In[13]:


for row in db.execute(sql):
    print(row[0])


# In[ ]:


7. From the book table, select and print all columns in the order of publication.


# In[14]:


for row in db.execute('select * from book order by year'):
    print(row)


# In[16]:


for row in db.execute('select * from book order by year'):
    print(*row, sep=', ')


# In[ ]:


8.)Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6


# In[17]:


import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = 'select title from book order by title asc'
rows = conn.execute(sql)
for row in rows:
    print(row)


# In[ ]:


9.)Install the Redis server and the Python redis library (pip install redis) on your computer. 
Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.


# In[8]:


pip install redis


# In[9]:


import redis
conn = redis.Redis()
conn.delete('test')


# In[10]:


conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})


# In[ ]:


conn.hgetall('test')


# In[ ]:


10. Increment the count field of test and print it.


# In[11]:


conn.hincrby('test', 'count', 3)


# In[12]:


conn.hget('test', 'count')


# In[ ]:




