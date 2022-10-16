Queue_ADT = """
데이터 : 선입선출(FIFO)의 접근 방법을 유지하는 항목들의 모음
연산
● Queue()    : 비어 있는 새로운 큐를 만든다.
● isEmpty()  : 큐가 비어 있으면 True를 아니면 False를 반환한다.
● enqueue(x) : 항목 x를 큐의 맨 뒤에 추가한다.
● dequeue()  : 큐의 맨 앞에 있는 항목을 꺼내 반환한다.
● peek       : 큐의 맨 앞에 있는 항목을 삭제하지 않고 반환한다.
● size()     : 큐의 모든 항목들의 개수를 반환한다.
● clear()    : 큐를 공백상태로 만든다.
"""

class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class CircularLinkedQueue:
    def __init__(self):
        self.tail = None
    def isEmpty(self): return self.tail == None
    def clear(self): self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
    def size(self):
        if self.isEmpty(): return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count
    def display(self, msg='CircularLinkedQueue : '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end =' ')
                node = node.link
            print(node.data, end=' ')
        print()
    
# Test Code
# q = CircularLinkedQueue()
# for i in range(8): q.enqueue(i)
# q.display()
# for i in range(5): q.dequeue()
# q.display()
# for i in range(8, 14): q.enqueue(i)
# q.display()
