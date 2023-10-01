# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:25:56 2023

@author: ASUS
"""

class Stack:
    
    def __init__(self):
        self.stack = []
        
    #o(1) running time
    def is_empty(self):
        return self.stack == []
    
    # o(1) running time
    def push(self,data):
        self.stack.append(data)
        
    # o(1) because we manipulate the last item
    
    def pop(self):
        
        if self.size_stack <1:
            return None
        
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    #o(1) constant running time
    
    def peek(self):
        return self.stack[-1]
    
    #o(1)
    def size_stack(self):
        return len(self.stack)
    
            