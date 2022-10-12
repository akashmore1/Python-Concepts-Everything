class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Sll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return self

        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1
        return self


s1 = Sll()
s1.push(4)
print(s1)
