"""Program to Implement Linked List Operations."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.next is None:
            self.next = new_node
        else:
            current = self.next
            while current.next:
                current = current.next
            current.next = new_node
    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.next
        self.next = new_node
    def display(self):
        current = self.next
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

head = Node(None)
head.insertAtEnd(10)
head.insertAtEnd(20)
head.insertAtBeginning(5)
head.display()
    