# Stack.py

NULL = None

class _Node:

    def __init__(self, data):
    
        self.previous = NULL
        self.data = data
        
    def getData(self):
        return (self.data)
    def getPrevious(self):
        return (self.previous)
    def setData(self, newData):
        self.data = newData
    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class Stack:

    def __init__(self, list):
        
        self._Length = 0
        self.node1 = _Node(NULL)
        for i in list:
            self.push(i)



    def __len__(self):
        return self._Length

    def push(self, data):

        self._Length = self._Length +1
        temp = self.node1
        newNode = _Node(data)
        self.node1 = newNode
        self.node1.setPrevious(temp)
    

    def pop(self):

        if self._Length == 0:
            return(None)
        temp = self.node1
        self.node1 = temp.getPrevious()
        self._Length = self._Length - 1
        return temp.getData()
            
            
    def peek(self):
        return(self.node1.getData())







        
