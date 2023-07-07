#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Enter the size of array: "))
sum = 0
arr = []
for i in range(0,n):
    temp = int(input("enter the values in array: "))
    arr.append(temp)
print("Reversed array is :" , end = "")
for i in range(n-1,-1,-1):
    print(arr[i], end = " ")


# In[ ]:




