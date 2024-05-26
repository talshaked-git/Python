class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = Node(root_value)
        else:
            self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None: # if tree is empty, new root is formed
            self.root = new_node
            return

        # traverse the tree to find new location for value by starting from the root
        current = self.root
        while current is not None:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right
            else:
                return


    def search(self, value):
        # Method to search for a value in the binary tree
        pass

    def delete(self, value):
        # Method to delete a value from the binary tree
        pass

    def in_order_traversal(self):
        # Method to perform in-order traversal
        pass

    def pre_order_traversal(self):
        # Method to perform pre-order traversal
        pass

    def post_order_traversal(self):
        # Method to perform post-order traversal
        pass
