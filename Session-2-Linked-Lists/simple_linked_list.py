class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def value(self):
        return self.value

    def next(self):
        return self.next


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values is not None:
            for value in reversed(values):
                self.push(value)

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def head(self):
        return self.head.value() if self.head else None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            raise EmptyListException("Nothing to pop from a list")
        popped_value = self.head.value()
        self.head = self.head.next()
        return popped_value

    def reversed(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next()
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


class EmptyListException(Exception):
    pass
