Deque_ADT = """
데이터 : 전단과 후단을 통한 접근을 허용하는 항목들의 모음
연산
● Deque()       : 비어 있는 새로운 덱을 만든다.
● isEmpty()     : 덱이 비어 있으면 True를 아니면 False를 반환한다.
● addFront(x)   : 항목 x를 덱의 맨 앞에 추가한다. O(1)
● deleteFront() : 맨 앞에 있는 항목을 꺼내 반환한다. O(1)
● getFront()    : 맨 앞의 항목을 꺼내지 않고 반환한다. O(1)
● addRear(x)    : 항목 x를 덱의 맨 뒤에 추가한다. O(1)
● deleteRear()  : 맨 뒤의 있는 항목을 꺼내 반환한다. O(1)
● getRear()     : 맨 뒤의 항목을 꺼내지 않고 반환한다. O(1)
● isFull        : 덱이 가득 차 있으면 True를 아니면 False를 반환한다.
● size()        : 덱의 모든 항목들의 개수를 반환한다.
● clear()       : 덱을 공백상태로 만든다.
"""

class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self): return self.front == None
    def clear(self): self.front = self.rear = None
    def size(self):
        node = self.front
        count = 0
        while not node == None:
            node = node.next
            count += 1
        return count
    def display(self, msg='DoublyLinkedDeque : '):
        print(msg, end='')
        node = self.front
        while not node == None:
            print(node.data, end=' ')
            node = node.next
        print()
    def addFront(self, item):
        node = DNode(item, None, self.front)
        if (self.isEmpty()):
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node
    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if (self.isEmpty()):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data
    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data

# Test Code
# dq = DoublyLinkedDeque()
# for i in range(9):
#     if i%2 == 0: dq.addRear(i)
#     else: dq.addFront(i)
# dq.display()
# for i in range(2): dq.deleteFront()
# for i in range(3): dq.deleteRear()
# dq.display()
# for i in range(9, 14): dq.addFront(i)
# dq.display()