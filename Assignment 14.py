#!/usr/bin/env python
# coding: utf-8

# # Assignment 14

# In[ ]:


get_ipython().set_next_input('Q1). What does RGBA stand for');get_ipython().run_line_magic('pinfo', 'for')


# In[ ]:


Answer:-
    The RGBA color format is an extension of the RGB scheme with an added alpha channel that specifies the opacity of the color.
    rgba(red, green, blue, alpha)


# In[ ]:


get_ipython().set_next_input('Q2). From the Pillow module, how do you get the RGBA value of any images');get_ipython().run_line_magic('pinfo', 'images')


# In[1]:


pip install pillow


# In[ ]:


Answer:-
    To create a transparent png using Python3, the Pillow library is used. The Pillow library comes with python itself.
    


# In[ ]:


get_ipython().set_next_input('Q3. What is a box tuple, and how does it work');get_ipython().run_line_magic('pinfo', 'work')


# In[ ]:


Answer:-The box.tuple submodule provides read-only access for the tuple userdata type. It allows, for a single tuple: 
        selective retrieval of the field contents, retrieval of information about size, iteration over all the fields, and 
        conversion to a Lua table
        box.tuple.new() to Create a tuple
        box.tuple.bsize()	Get count of bytes in a tuple


# In[ ]:


get_ipython().set_next_input('Q4)Use your image and load in notebook then, How can you find out the width and height of an Image object');get_ipython().run_line_magic('pinfo', 'object')


# In[14]:


# import required module
from PIL import Image

# get image
filepath = "BBU ROOM1.jpeg"
img = Image.open(filepath)

# get width and height
width = img.width
height = img.height

# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)


# In[ ]:


get_ipython().set_next_input('Q5)What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it');get_ipython().run_line_magic('pinfo', 'it')


# In[32]:


from PIL import Image
catIm=Image.open('BBU ROOM1.jpeg')
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped1.jpeg')


# In[33]:


from PIL import Image
catIm = Image.open('BBU ROOM1.jpeg')
catCopyIm = catIm.copy()


# In[ ]:


get_ipython().set_next_input('6. After making changes to an Image object, how could you save it as an image file');get_ipython().run_line_magic('pinfo', 'file')


# In[34]:


width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('BBU ROOM.jpeg')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('BBU ROOM12.jpeg')


# In[ ]:


get_ipython().set_next_input('Q7)What module contains Pillow’s shape-drawing code');get_ipython().run_line_magic('pinfo', 'code')


# In[ ]:


Answer:-
    The 'ImageDraw' module provides simple 2D graphics support for Image Object. Generally, we use this module to create 
    new images, annotate or retouch existing images and to generate graphics on the fly for web use


# In[ ]:


Q8)Image objects do not have drawing methods. What kind of object does? How do you get this kind of object


# In[ ]:


Answer:-
    A Drawing object describes visible content, such as a shape, bitmap, video, or a line of text. Different types of drawings
    describe different types of content

