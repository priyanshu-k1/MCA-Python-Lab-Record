"""
Program to Implement Stack Operations 
"""
class Stack:
    size = 0
    def __init__(self,size):
        self.stack = []
        self.size = size

    def push(self, item):
        n = len(self.stack)
        if n < size:
            self.stack.append(item)
        else:
            print("Stack overflow")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from stack.")
            return item
        else:
            print("Stack Underflow. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            item = self.stack[-1]
            print(f"Top item is {item}.")
            return item
        else:
            print("Stack is empty. No top item.")
            return None
    def is_empty(self)->bool:
        return not len(self.stack) > 0 
     
    def display(self):
        if not self.is_empty():
            print("Stack contents:", self.stack)
        else:
            print("Stack is empty.")


size = int(input("Enter the size of the stack: "))
stk = Stack(size)
for _ in range(size):
    item = input("Enter an item to push onto the stack: ")
    stk.push(item)
print("elements in the stack are:")
stk.display()
print(f"Top element in the stack: {stk.peek()}")
stk.pop()
print("After poping elements are:")
stk.display()