import sys

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
            # Reverse iterate through the list
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])

if __name__ == '__main__':
    obj = Stack()
    while True:
        print("\n1.Push\n2.Pop\n3.Peek\n4.Traverse\n0.Exit")

        try:
            ch = int(input("Select any choice: "))

            if ch == 1:
                ele = int(input("Enter element: "))
                obj.push(ele)
            elif ch == 2:
                obj.pop()
            elif ch == 3:
                obj.peek()
            elif ch == 4:
                obj.traverse()
            elif ch == 0:
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number.")