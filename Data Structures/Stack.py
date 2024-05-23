class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is already empty")

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty, nothing to peek at")
        return self.stack[-1]

    def isEmpty(self):
        return not self.stack 
    
    def size(self):
        return len(self.stack)
    
    def printStack(self):
        for x in self.stack:
            print(x)
    

# Initialize Stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.printStack()
print(f"Peeking at: {stack.peek()}")
print(f"Popped: {stack.pop()}")
stack.printStack()