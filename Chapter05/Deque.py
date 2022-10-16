from Queue import *

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

class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()
    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()
    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1
            if self.front < 0: self.front = MAX_QSIZE - 1
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1
            if self.rear < 0:self.rear = MAX_QSIZE - 1
            return item
    def getRear(self):
        return self.items[self.rear]

# Test Code
# dq = CircularDeque()
# for i in range(9):
#     if i%2 == 0: dq.addRear(i)
#     else: dq.addFront(i)
# dq.display()
# for i in range(2): dq.deleteFront()
# for i in range(3): dq.deleteRear()
# dq.display()
# for i in range(9, 14): dq.addFront(i)
# dq.display()