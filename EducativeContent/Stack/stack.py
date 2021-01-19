class Stack:
    def __init__(self):
        self.head=[]

    def appendToStack(self,data):
        self.head.append(data)

    def deleteFromStack(self):
        if self.head:
            return self.head.pop()

    def peekStack(self):
        if not self.isEmptyStack():
            return self.head[-1]
        return None

    def getStack(self):
        return self.head

    def printStack(self):
        for val in self.head:
            print(val)

    def isEmptyStack(self):
        return self.head==[]