#!/usr/bin/env python
# coding: utf-8

# In[5]:


def is_operator(char):
    operators = ['+', '-', '*', '/']
    return char in operators

def postfix_to_prefix(expression):
    stack = []

    for char in expression:
        if is_operator(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expression = char + operand1 + operand2
            stack.append(new_expression)
        else:
            stack.append(char)

    return stack.pop()


postfix_expression = "2 3 4 * +"
prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix expression:", prefix_expression)


# In[ ]:




