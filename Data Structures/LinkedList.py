
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self,data,index):
        new_node = Node(data)
        current_node = self.head
        position = 0

        if index == 0:
            self.insertAtStart(data)
            return
        
        while (current_node is not None and position+1 != index):
            current_node = current_node.next
            position += 1
        
        if current_node is not None:
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index out of range")
            
    def insertAtEnd(self, data):
        new_node = Node(data)
        current_node = self.head

        if current_node is None:
            self.head = new_node
            return
        
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node

    def updateNode(self, value, index):
        current_node = self.head
        position = 0

        if position == index:
            current_node.data = value
            return
        else:
            while current_node is not None and position != index:
                current_node = current_node.next
                position += 1

            if current_node is not None:
                current_node.data = value

            else:
                print("Index out of range")
    
    def deleteHead(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def deleteTail(self):
        current_node = self.head

        if current_node is None:
            print("List is empty")
            return
        
        if current_node.next is None:
            self.head = None
            return
        
        while current_node.next.next is not None:
            current_node = current_node.next
        
        current_node.next = None
    
    def deleteNodeAtIndex(self, index):
        current_node = self.head
        position = 0

        if index == 0:
            self.head = current_node.next
            return
        
        while current_node is not None and position+1 != index:
            current_node = current_node.next
            position += 1
        
        if current_node is not None:
            current_node.next = current_node.next.next
        else:
            print("Index out of range")
    

    def printList(self):
        current_node = self.head

        while current_node is not None:
            if current_node.next is not None:
                print(current_node.data, end=" -> ")
            else:
                print(current_node.data, end="")
            current_node = current_node.next
        print()

    def search(self, data):
        current_node = self.head
        position = 0

        while current_node is not None:
            if current_node.data == data:
                return position
            current_node = current_node.next
            position += 1
        
        return -1


# Creating a linked list
ll = LinkedList()
ll.insertAtStart(3)
ll.insertAtStart(3)
ll.insertAtStart(1)
ll.insertAtEnd(4)
ll.printList()
ll.updateNode(2, 1)
ll.printList()
value = 4
print(f"value {value} at index:  {ll.search(value)}")