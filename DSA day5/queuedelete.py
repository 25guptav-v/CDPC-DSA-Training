import sys

class Queue:
    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = 0
        self.CAPACITY = 5

    def isFull(self):
        if self.rear == self.CAPACITY - 1:
            return True
        else: 
            return False

    def insert(self, ele):
        if self.isFull():
            print("queue is full")
        else:
            self.rear = self.rear + 1
            self.queue.append(ele)
            print("ele is inserted")

    def traverse(self):
        if self.isEmpty():
            print("queue is Empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])

    def isEmpty(self):
        if self.rear < self.front:
            return True
        else:
            return False

    def delete(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            ele = self.queue[self.front]
            print(f"Deleted element: {ele}")
            self.front += 1

    def peek(self):
        if self.isEmpty():
            print("queue is Empty")
        else:            
            # Peek looks at the front of the queue
            print(self.queue[self.front])

if __name__ == '__main__':
    obj = Queue()
    while True:
        print("\n1. insert")
        print("2. delete")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        try:
            ch = int(input("select any choice: "))
            if ch == 1:
                ele = int(input("Enter data: "))
                obj.insert(ele)
            elif ch == 2:
                obj.delete()
            elif ch == 3:
                obj.peek()
            elif ch == 4:
                obj.traverse()
            elif ch == 0:
                sys.exit(0)
        except ValueError:
            print("Invalid input! Please enter a number.")