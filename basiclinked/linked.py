#!/usr/bin/env python

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next

        return count

    def check(self, val):
        node = self.head
        while node:
            if node.val == val:
                return True
            else:
                node = node.next

        return False

    def delete(self, val):
        node = self.head
        prev = node
        while node:
            if node.val == val:
                prev.next = node.next
                if node == self.head:
                    self.head = node.next
                del node
                return True

            else:
                prev = node
                node = node.next

        return None

    def walk(self):
        node = self.head
        while node:
            print(str(node.val) + '->', end=''),
            node = node.next

        print('')

ll = LinkedList()
ll.walk()

ll.add(1)
ll.walk()

ll.add(2)
ll.walk()

ll.add(3)

ll.walk()

ll.delete(2)
ll.walk()

ll.delete(3)

ll.walk()

ll.delete(1)
ll.walk()

print(ll.check(9))
print(ll.size())

ll.add(-19)
ll.add(10)
ll.add(0)

print(ll.check(11))

print(ll.size())