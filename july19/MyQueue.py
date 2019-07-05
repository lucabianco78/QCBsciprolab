class MyQueue:

    def __init__(self):
        self.__data = list()

    def isEmpty(self):
        return len(self.__data) == 0

    def __len__(self):
        return len(self.__data)

    def enqueue(self, element):
        self.__data.insert(0,element)

    def dequeue(self):
        el = None
        if len(self.__data) > 0:
            el = self.__data.pop()
        return el

    def top(self):
        if len(self.__data) > 0:
            return self.__data[-1]

