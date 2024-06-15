import numpy as np


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.head = None
        self.rear = None
        self.curr_len = 0  # Add length variable

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.curr_len == self.capacity

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.rear = node
            self.head = node
            self.curr_len += 1
            return
        self.rear.next = node
        self.rear = node
        self.curr_len += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        node = self.head
        self.head = self.head.next
        self.curr_len -= 1

        if self.head is None:
            self.rear = None

        return node.val

    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.val


if __name__ == '__main__':
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.is_full())

    print(queue1.front())

    print(queue1.dequeue())

    print(queue1.front())

    print(queue1.dequeue())

    print(queue1.is_empty())
