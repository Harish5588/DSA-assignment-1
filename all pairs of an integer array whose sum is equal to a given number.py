#!/usr/bin/env python
# coding: utf-8

# In[3]:


def find(array, len, sum):
    print("Pairs whose sum is : ", sum)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == sum:
                print(array[i], array[j])


array = [5, 2, 3, 4, 1, 6, 7]

sum = 7

print("Array= ", array)

find(array, len(array), sum)


# In[ ]:




