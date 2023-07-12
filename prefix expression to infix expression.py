#!/usr/bin/env python
# coding: utf-8

# In[6]:


def prefixToInfix(prefix):  
    symbols = []  
 
    l = len(prefix) - 1  
    while l >= 0:  
        if not Operator(prefix[l]):  
               
             
            symbols.append(prefix[l])  
            l -= 1  
        else:  
             
            string = "(" + symbols.pop() + prefix[l] + symbols.pop() + ")"  
            symbols.append(string)  
            l -= 1  
       
    return symbols.pop()  
  
def Operator(symbols):  
    if symbols == "*" or symbols == "+" or symbols == "-" or symbols == "/" or symbols == "^" or symbols == "(" or symbols == ")":  
        return True  
    else:  
        return False  
  
string = "*+P/QR-/STU"  
print("The infix string is: ", prefixToInfix(string))  


# In[ ]:




