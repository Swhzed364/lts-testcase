from collections import deque

class Buffer:

    def __init__(self, size: int):

        self.__size = size
        self.__buffer = deque([], maxlen=size)

    def __isFull(self):

        return len(self.__buffer) == self.__size

    def add(self, data): 

        if self.__isFull():
            self.__buffer.popleft()
            self.__buffer.append(data)
        else:
            self.__buffer.append(data)

    def get(self):
        
        return self.__buffer
    
    def clear(self):

        self.__buffer.clear()

    