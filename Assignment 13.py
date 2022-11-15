#!/usr/bin/env python
# coding: utf-8

# # Assignment 13

# In[ ]:


get_ipython().set_next_input('Q1). What advantages do Excel spreadsheets have over CSV spreadsheets');get_ipython().run_line_magic('pinfo', 'spreadsheets')


# In[ ]:


Answer:-
Excel allows them to do the data storage, processing, analyzing, and exporting in the required manner. Moreover,
it is a highly structured and organized file format, specifically developed for the tabular data and to correlate the details
from the various independent tables.
CSV is a text file format where comma-separated values store the whole data accordingly.


# In[ ]:


get_ipython().set_next_input('Q2)What do you pass to csv.reader() and csv.writer() to create reader and writer objects');get_ipython().run_line_magic('pinfo', 'objects')


# In[ ]:


#To read a CSV file in Python, we can use the csv.reader() function. Suppose we have a csv file named people.csv

import csv
with open('skiritng-qty.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
#To write to a CSV file in Python, we can use the csv.writer() function

with open('skirting-qty2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])


# In[ ]:


get_ipython().set_next_input('3. What modes do File objects for reader and writer objects need to be opened in');get_ipython().run_line_magic('pinfo', 'in')


# In[ ]:


Answer:-
   1) In order to open a file for reading or writing purposes, we must use the built-in open() function.
   2)The open() function uses two arguments. First is the name of the file and second is for what purpose we want to open it 
    get_ipython().set_next_input('    i.e.for reading or writing');get_ipython().run_line_magic('pinfo', 'writing')
   3)File_obj = open(“filename”, “mode”)


# In[ ]:


get_ipython().set_next_input('4. What method takes a list argument and writes it to a CSV file');get_ipython().run_line_magic('pinfo', 'file')


# In[ ]:


Answer:-
      A CSV file is a bounded text format which uses a comma to separate values.
      The most common method to write data from a list to CSV file is the writerow() method of writer and DictWriter class. 
    


# In[3]:


import csv
data = [['Geeks'], [4], ['geeks !']]
 
# opening the csv file in 'w+' mode
file = open('skirting-qty1.csv', 'w+', newline ='')
 
# writing the data into the file
with file:   
    write = csv.writer(file)
    write.writerows(data)


# In[ ]:


get_ipython().set_next_input('5. What do the keyword arguments delimiter and line terminator do');get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


Answer:-The delimiter is the character that appears between cells on a row. By default, the delimiter for a CSV file is a comma. 
         The line terminator is the character that comes at the end of a row. By default, the line terminator is a newline


# In[ ]:


get_ipython().set_next_input('6). What function takes a string of JSON data and returns a Python data structure');get_ipython().run_line_magic('pinfo', 'structure')


# In[ ]:


Answer:-
    json.load()


# In[ ]:


get_ipython().set_next_input('Q7). What function takes a Python data structure and returns a string of JSON data');get_ipython().run_line_magic('pinfo', 'data')


# In[ ]:


Answer:-
    json.dumps()


# In[ ]:




