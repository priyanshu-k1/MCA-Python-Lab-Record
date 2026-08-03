"""
Program to Implement Queue Operations
"""
class Queue:
    size:int = 0
    def __init__(self,size:int):
        self.queue = []
        self.top = -1
        self.back = -1
        self.size = size
    def enqueue(self,item:int):
        if self.top < self.size:
            self.top += 1
            self.queue.append(item)
            if self.top == -1 and self.back == -1:
                self.back +=1
        else:
            print("Queue Overflow.")
    def dequeue(self):
        if self.top == -1 and self.back == -1:
            print("Queue Underflow.")
        else:
            item = self.queue[self.back]
            self.back += 1
            return item
    def display(self):
        if self.top == -1 and self.back == -1:
            print("Queue is Empty.")
        else:
            for i in range(self.back,self.top+1):
                print(self.queue[i],end=" ")
            print()

que = Queue(5)
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
print("Queue after enqueuing 3 elements:")
que.display()
que.dequeue()
print("Queue after dequeuing 1 element:")
que.display()