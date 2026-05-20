import sys
CAPACITY=5
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, ele):
        self.stack.append(ele)
        print(ele, "is pushed")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty (Underflow)")
        else:
            ele = self.stack.pop()
            print(ele, "is popped")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element is:", self.stack[-1])

    def traverse(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements (Top to Bottom):")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])


class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5

    def isFull(self):
        if self.rear==self.CAPACITY-1:
            return True
        else: 
            return False

    def insert(self,ele):
        if self.isFull():
            print("queue is full")
        else:
            self.rear=self.rear+1
            self.queue.append(ele)
            print("ele is inserted")


    def traverse(self):
        if self.isEmpty():
            print("queue is Empty")
        else:
            for i in range(self.rear+1):
                print(self.queue[i])


    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False

    def delete(self):
        pass
        
    
    def peek(self):
        if self.isEmpty():
            print("queue is Empty")
        else:            
            print(self.queue[self.rear])

    

if __name__ == '__main__':
    obj1=Queue()
    obj2=Stack()
    n = int(input("Enter number of elements: "))
    for i in range(n):
        ele=int(input("enter element"))
        obj1.insert(ele)

    for x in range(n):
        ele=obj1.delete()
        obj2.push(ele)

    for x in range(n):
         ele=obj2.pop()
         obj1.insert(ele)

    obj1.traverse()
    