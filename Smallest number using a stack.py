#!/usr/bin/env python
# coding: utf-8

# In[10]:


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

    
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def get_min(self):
        if not self.min_stack:
            return None

        return self.min_stack[-1]

stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(7)
stack.push(1)
stack.push(9)

print("Smallest number:", stack.get_min()) 

stack.pop()
stack.pop()

print("Smallest number:", stack.get_min())


# In[ ]:




