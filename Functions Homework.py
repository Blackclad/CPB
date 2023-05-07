#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Write a function that computes the volume of a sphere given its radius
def vol(rad):
    return (rad**3 * (4/3) * 3.14)


# In[24]:


vol(2)


# In[35]:


# Write a function that checks whether a number is in a given range (inclusive of high and low) - Boolean
def ran_bool(num,low,high):
    if low < num < high:
        return True
    else:
        return False


# In[37]:


ran_bool(5,1,10)


# In[149]:


# Write a function that checks whether a number is in given range (inclusive of high and low)
def ran_check(num,low,high):
    if low < num < high:
        print(f'{num} is in range of {low} and {high}')


# In[150]:


ran_check(5,2,7)


# In[207]:


# Write a function that accepts a string and calculates the nummber of upper and lower case letters
def up_low(s):
    
    upper_count = 0
    lower_count = 0
    
    for letter in s:
        if letter.isupper():
            upper_count = upper_count + 1
        elif letter.islower():
            lower_count = lower_count + 1
    
    print(f'No. of Upper case characters : {upper_count}')
    print(f'No. of Lower case characters : {lower_count}')
   


# In[208]:


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# In[246]:


# Write a function that takes a list and returns a new list with unique elements of the first list
def unique_list(lst):
    ulst = []
    for num in lst:
        if num not in ulst:
            ulst.append(num)
    return ulst
    


# In[247]:


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# In[261]:


# Write a function to multiply all numbers in a list
def multiply(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


# In[262]:


multiply([1,2,3,-4])


# In[272]:


# Write a function that checks whether a word or phrase is a palindrome or not
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


# In[273]:


palindrome('helleh')


# In[453]:


# Write a function to check whether a string is pangram or not.
import string

def ispangram(str1):
    
    alphabet = string.ascii_lowercase
    str1 = str1.lower().replace(' ','')
   
    reference = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters = []
    uletters = []
        
    for letter in str1:
        if letter in alphabet:
            letters.append(letter)
        else:
            pass
   
    for letter in letters:
        if letter not in uletters:
            uletters.append(letter)
        else:
            pass
    
    uletters.sort()
    if uletters == reference:
        return True
    else:
        return False


# In[454]:


ispangram("The quick brown fox jumps over the lazy dog")


# In[ ]:





# In[ ]:





# In[ ]:




