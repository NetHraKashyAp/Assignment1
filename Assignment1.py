#!/usr/bin/env python
# coding: utf-8

# ### Q1. Write a python program that takes two numbers as the inputs such as X and Yand print the result of X^Y(Xto the power of Y).

# In[3]:


result=1
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
for i in range(y):
    result *= x
print(result)


# ### Q2. Write a program to print the numbers in the list which are divisible by 3.

# In[2]:


li=[]
lower=int(input("Enter lower limt: "))
upper=int(input("Enter upper limit: "))
for i in range(lower,upper+1):
    if(i%3==0):
        li.append(i)
print(li)

