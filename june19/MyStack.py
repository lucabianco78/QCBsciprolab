"""
NAME:
SURNAME:
Matricola: 

partB_2.py
"""
from collections import deque


class MyStack:

    def __init__(self):
        self.__data = list()

    def isEmpty(self):
        return len(self.__data) == 0

    def __len__(self):
        return len(self.__data)

    def push(self, element):
        """adds an element on top of the stack"""
        self.__data.append(element)

    def pop(self):
        """removes one element from the stack and returns it"""
        if len(self.__data) > 0:
            ret = self.__data.pop()
            return ret
        else:
            return None

    def peek(self):
        if len(self.__data) > 0:
            return self.__data[-1]
        else:
            return None
        
    
