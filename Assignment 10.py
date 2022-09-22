#!/usr/bin/env python
# coding: utf-8

# # Assignment 10

# In[ ]:


1. How do you distinguish between shutil.copy() and shutil.copytree()?


# Answer:- While shutil. copy() will copy a single file, shutil. copytree() will copy an entire folder and every folder and file contained in it.

# In[ ]:


get_ipython().set_next_input('2. What function is used to rename files');get_ipython().run_line_magic('pinfo2', 'files')


# In[ ]:


Anwer:- import os
os.rename(source,destination)
Source:- file name  and destination:- The name which would replace the current name of file/directory.


# In[ ]:


get_ipython().set_next_input('3. What is the difference between the delete functions in the send2trash and shutil modules');get_ipython().run_line_magic('pinfo', 'modules')


# Answer:- 
#     The send2trash functions will move a file or folder to the recycle bin,
#     while shutil functions will permanently delete files and folders.

# In[ ]:


4.ZipFile objects have a close() method just like File objects’ close() method. 
get_ipython().set_next_input('What ZipFile method is equivalent to File objects’ open() method');get_ipython().run_line_magic('pinfo', 'method')


# Answer:- from zipfile import Zipfile
# with ZipFile(file_name, 'r') as zip: -> this code will open specified zipfile for us. we can use zip objext to preform oother operation the ziplife. like zip.read()

# In[ ]:


5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.


# In[ ]:


Answer:-


# In[2]:



import os, shutil

def selectiveCopy(source, extensions, destFolder):
    folder = os.path.abspath(source)
    destFolder = os.path.abspath(destFolder)
    print('Looking in', source, 'for files with extensions of', ', '.join(extensions))
    for foldername, subfolders, filenames in os.walk(source):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.mp4', '.pdf','.jpg']
source = "D:\\files\\Mr wandre"
destFolder = "D:\\files\\Mr wandre"
selectiveCopy(source, extensions, destFolder)


# In[4]:


import os


# In[ ]:





# In[ ]:




