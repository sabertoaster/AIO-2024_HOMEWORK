import numpy as np


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyStack:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.head = None
        self.curr_len = 0  # Add length variable

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.curr_len == self.capacity

    def push(self, value):
        node = Node(value, self.head)
        self.head = node
        self.curr_len += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        node = self.head
        self.head = self.head.next
        self.curr_len -= 1
        return node.val

    def top(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.head.val


if __name__ == '__main__':
    stack1 = MyStack(capacity=5)

    stack1.push(1)

    stack1.push(2)

    print(stack1.is_full())

    print(stack1.top())

    print(stack1.pop())

    print(stack1.top())

    print(stack1.pop())

    print(stack1.is_empty())
