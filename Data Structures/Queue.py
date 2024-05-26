
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            print("Queue is already empty")
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty, nothing to peek at")
        return self.queue[0]
    
    def isEmpty(self):
        return not self.queue
    
    def size(self):
        return len(self.queue)

    def printQueue(self):
        for item in self.queue:
            print(item, end=' ')
        print()
        

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.printQueue()  # Output: 1 2 3
print(queue.dequeue())  # Output: 1
queue.printQueue()  # Output: 2 3
print(queue.peek())  # Output: 2