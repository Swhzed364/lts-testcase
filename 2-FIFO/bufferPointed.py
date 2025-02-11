class BufferPointed:

    def __init__(self, size):
        
        self.__size = size
        self.__position = 0
        self.__buffer = []

    def add(self, data):

        if self.__position < self.__size:
            self.__buffer.append(data)
            self.__position += 1
        else:
            self.__buffer.pop(0)
            self.__buffer.append(data)


    def get(self):

        return self.__buffer
    
    def clear(self):

        self.__buffer.clear()