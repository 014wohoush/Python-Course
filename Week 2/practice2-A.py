#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number =float(input("Enter the number you want to print all prime number within: "))
if number >1:
    for x in range (2,int(number)):
            for i in range (2,int(x/2)):
                if x%i==0:
                    break
            else:
                print(x, end=",")

