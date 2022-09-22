#!/usr/bin/env python
# coding: utf-8

# # Assignment 07

# In[ ]:


get_ipython().set_next_input('Q1). What is the name of the feature responsible for generating Regex objects');get_ipython().run_line_magic('pinfo', 'objects')


# In[ ]:


Answer:-
       The re.compile() function returns Regex objects.


# In[ ]:


get_ipython().set_next_input('Q2).Why do raw strings often appear in Regex objects');get_ipython().run_line_magic('pinfo', 'objects')


# In[ ]:


Amswer:-
    Raw strings are used so that backslashes do not have to be escaped.


# In[ ]:


get_ipython().set_next_input('Q3).What is the return value of the search() method');get_ipython().run_line_magic('pinfo', 'method')


# In[ ]:


Answer:-
     The re.compile() function returns Regex objects.


# In[ ]:


get_ipython().set_next_input('Q4).From a Match item, how do you get the actual strings that match the pattern');get_ipython().run_line_magic('pinfo', 'pattern')


# In[ ]:


Answer:-
    The group() method returns strings of the matched text.


# In[ ]:


5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover? Group 2? Group 1?


# In[2]:


r'(\d\d\d)-(\d\d\d-\d\d\d\d)'


# In[ ]:


Q6).In standard expression syntax, parentheses and intervals have distinct meanings.
get_ipython().set_next_input('How can you tell a regex that you want it to fit real parentheses and periods');get_ipython().run_line_magic('pinfo', 'periods')


# Answer:-
#     Periods and parentheses can be escaped with a backslash: \., \(, and \).

# In[ ]:


get_ipython().set_next_input('Q7).The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options');get_ipython().run_line_magic('pinfo', 'options')


# In[ ]:


Answer:-
If the regex has no groups, a list of strings is returned. If the regex has groups, a list of tuples of strings is returned.


# In[ ]:


get_ipython().set_next_input('Q8).In standard expressions, what does the | character mean');get_ipython().run_line_magic('pinfo', 'mean')


# In[ ]:


Answer:-
    The | character signifies matching "either, or" between two groups.


# In[ ]:


get_ipython().set_next_input('Q9).In regular expressions, what does the character stand for');get_ipython().run_line_magic('pinfo', 'for')


# In[ ]:


Answer:-
the ? character can either mean "match zero or one of the preceding group" or be used to signify nongreedy matching


# In[ ]:


get_ipython().set_next_input('Q10).In regular expressions, what is the difference between the + and * characters');get_ipython().run_line_magic('pinfo', 'characters')


# In[ ]:


Answer:-
    The + matches one or more. The * matches zero or more.


# In[ ]:


get_ipython().set_next_input('Q11).What is the difference between {4} and {4,5} in regular expression');get_ipython().run_line_magic('pinfo', 'expression')


# In[ ]:





# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q12). What do you mean by the \\d, \\w, and \\s shorthand character classes signify in regular expressions');get_ipython().run_line_magic('pinfo', 'expressions')


# In[ ]:


this expression explain the space charactor and singl charactor space .it is a digit, word, or space character, respectively.


# In[ ]:


get_ipython().set_next_input('Q13).What do means by \\D, \\W, and \\S shorthand character classes signify in regular expressions');get_ipython().run_line_magic('pinfo', 'expressions')


# In[ ]:


The \D, \W, and \S shorthand character classes match a single character 
that is not a digit, word, or space character, respectively.


# In[ ]:


get_ipython().set_next_input('Q14). What is the difference between .*? and .*');get_ipython().run_line_magic('psearch', '*')


# In[ ]:


Answer:-
(.*?) matches any character (.) any number of times (*), as few times as possible to make the regex match (?). 
You'll get a match on any string, but you'll only capture a blank string because of the question mark. 
This feature is much more useful when you have a more complicated regex.
Here, the parser doesn't have to capture anything at all to get a match: 
the asterisk allows any number of characters in the capturing group,
while the question mark makes the parser save as many as possible from the input text for later, 
resulting in nothing being captured.

(.*)? captures a group zero or one times (?). That group consists of a run of any length (*) of any character (.).
This also will match anything, but it will capture the first line, since the dot matches anything except a newline.


# In[ ]:


get_ipython().set_next_input('Q15). What is the syntax for matching both numbers and lowercase letters with a character class');get_ipython().run_line_magic('pinfo', 'class')


# In[30]:


import re


# In[8]:


vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')


# In[9]:


import re


# In[10]:


consonantRegex = re.compile(r'[aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')


# In[11]:


consonantRegex


# In[12]:


vowelRegex


# In[17]:


consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')


# (^) this is an negative charactor its maching with every charactor except the vowels 

# In[ ]:


get_ipython().set_next_input('Q16). What is the procedure for making a normal expression in regax case insensitive');get_ipython().run_line_magic('pinfo', 'insensitive')


# In[ ]:


re.IGNORECASE : This flag allows for case-insensitive matching of the Regular Expression with
the given string i.e. expressions like [A-Z] will match lowercase letters, too. 
Generally, It’s passed as an optional argument to re.compile().


# In[ ]:


Q17).What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?


# In[ ]:


Answer:-
modify the behavior of dot (.) character to match the newline character apart from other characters.


# In[ ]:


get_ipython().set_next_input("Q18).If numReg = re.compile(r'\\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return");get_ipython().run_line_magic('pinfo', 'return')


# In[ ]:


Answer:-
    X drummers, X pipers, five rings, X hens


# In[25]:


import re


# In[1]:


import re


# In[3]:


numRegex = re.compile(r'\d+')
numRegex.sub('X', '11 drummers 10 pipers five rings 4 hen.')


# In[ ]:


get_ipython().set_next_input('Q19). What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do');get_ipython().run_line_magic('pinfo', 'do')


# Answer:-
#     To ignore whitespace and comments inside the regular expression string.

# In[4]:


re.compile()


# In[12]:


import re


# In[15]:


vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex = re.VERBOSE(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')


# In[ ]:


20. How would you write a regex that match a number with comma for every three digits? It must match the given following:
'42'
'1,234'
'6,368,745'
but not the following:
'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)


# In[18]:


s=('42''1,234,''6,368,745')


# numCommas.search= re.compile(r'['42''1,234,''6,368,745']')
# numCommas.search('12,34,567')

# Answer not found we tried best.
# 

# In[ ]:


Q21). How would you write a regex that matches the full name of someone whose last name is Watanabe? 
You can assume that the first name that comes before it will always be one word that begins with a capital letter.
The regex must match the following:
'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following:
'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized


# In[ ]:





# In[ ]:


22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol;
the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs;
and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:
'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'


# In[24]:


senRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).', re.I|re.DOTALL)

senRegex.findall('''Alice eats apples.'

'Bob pets cats.'

'Carol throws baseballs.'

'Alice throws Apples.'

'BOB EATS CATS.'

but not the following:

'Robocop eats apples.'

'ALICE THROWS FOOTBALLS.'

'Carol eats 7 cats.''')


# In[25]:


senRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).', re.I|re.DOTALL)

senRegex.findall('''Alice eats apples.''Bob pets cats.''Carol throws baseballs.''Alice throws Apples.''BOB EATS CATS.'

but not the following:

'Robocop eats apples.'

'ALICE THROWS FOOTBALLS.'

'Carol eats 7 cats.''')


# In[ ]:




