#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# * 
# 'hello'
# -87.8
# - 
# / 
# +	
# 6 
# 

# Answer 
# 1)* :-Use Numeric operator as Multiplication.
# 2)'hellow':- Charactor as sring 
# 3)-87.8 :- Integer 
# 4)- :- Numeric operator as Substraction 
# 5)/ :- Numeric operator as Division 
# 6)+ :- Numeric operator as Addition
# 7)6:- Integer.
# 

# 2. What is the difference between string and variable?

# String :- 1)String is a collection and set of alphabets or characters, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation.
# 2)it is an data storage type of variable.
# 
# Vaiable :-1)the interpreter allocates memory and decides what can be stored in the reserved memory.we can store integers, decimals or characters in terms of variables.
# 2)variales storage methods in python are Numbers,list,string,tuple,Dictionary.

# Q3. Describe three different data types.

#         Data tupes are Numeric, Sequence type,Set.
# 
# 1)Numeric Data tupe :- 
# 
#        a)Integer:- Int contains positive and negative values which is whole numbers without fraction or decimal.
#        
#        b)Float:- it contains the positive,negativ,decimal,fraction which only real number withut imaginary and complex numbers.
#        
#        c)Complex Numbers:- it Contain the real and Imaginary Numbers.
#        
# 2)Sequence Type:-
#        a)String:- It is thr collection of one or more charactors with single, double, triple quote
#        
#        b)List:- Its order of collection of data using the squre brackets.
#        
#        c)tuple:- Its also order collection of data, its can not be modify ones the created.
#        
# 3)Set:-
#        a)Set is an unorederd type it can be change after creation and iterable, no duplicate element will pass.

# In[ ]:


get_ipython().set_next_input('Q4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')


# 33An Expression is an operators and operand that interpretator produces value,so there is more operators thire predences decide the which operation perform first.
# 1)Constant Operation:- These are the expression only have the constant values only.
# 
# 2)Arithmatic Operation :- An arithmatic operation is a combination of numeric value,operator ,paranthesis some time result value only is numeric type.additon substraction multipication , division.reminder,exponention.
# 
# 3)Integral Expression:-This type of that produce only integer result after all computation and type conversion.
# 
# 4)Floating Expression :- This type of expression produses the floatin type result like the fractionnal number also.
# 
# 5)Relation Expression :- This type of expression relate the both side relation operator those arithmatic expreation are evalute first and comper the as per operator.
# 
# 6)Logic Expression:-This expression result are in true and false type . 
# 
#                      1)P and Q if P and  Q are ture then its result are True
#                      2)P or Q if only one is true then the result shows ture
#                      3)Not P it returns true if condition is true

# Q. What is the difference between an expression and a statement?

# Expression Only contain the identifier and operator it include arithmatic ,boolean operators .
# statement represent an action and cammond that can execute the operators.
# 
# 

# In[ ]:


get_ipython().set_next_input('Q ) After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1


# In[9]:


bacon=22;
print(bacon+1)


# In[28]:


bacon=22


# In[30]:


bacon+1


# 7. What should the values of the following two terms be?
# 'spam' + 'spamspam'
# 'spam' * 3
# 
# Answer:-  
# 

# In[22]:


s ="spam" +"spamspam"

    


# In[23]:


s


# In[25]:


s1="spam"*3


# In[26]:


s1


# In[ ]:


get_ipython().set_next_input('Q. 8). Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')


# In python varibale must start with the letter or underscore. so that 100 is invalid. 

# In[ ]:


get_ipython().set_next_input('9. What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')


# int(),float(),str() this are function need to use .

# In[ ]:


get_ipython().set_next_input('10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten ' + 99 + ' burritos.'


# In[31]:


s= "i have eaten + 99 + burritons"


# In[32]:


s


# only string to string variable is pass not string to int 

# In[ ]:




