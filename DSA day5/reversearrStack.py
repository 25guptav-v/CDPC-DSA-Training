import sys

class Stack:
    def __init__(self):
        # We use a dynamic list so there's no fixed capacity
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

def reverse_array(arr):
    s = Stack()

    for element in arr:
        s.push(element)

    reversed_arr = []
    while not s.isEmpty():
        reversed_arr.append(s.pop())

    return reversed_arr

if __name__ == '__main__':
    obj = Stack()
    arr = [122, 342, 563, 8794, 895]
    reversed_arr = reverse_array(arr)
    print(reversed_arr)
