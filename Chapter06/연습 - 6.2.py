from LinkedList import *

class newList(Node, LinkedList):
    def __init__(self):
        self.head = None
        self.cnt = 0
    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node
        self.cnt += 1
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link
        self.cnt -= 1
    def size(self):
        return self.cnt

# Test Code
lst = newList()
lst.insert(0, 10); lst.insert(0, 20); lst.insert(0, 30)
print(lst.size())
lst.delete(0); lst.delete(0)
print(lst.size())
