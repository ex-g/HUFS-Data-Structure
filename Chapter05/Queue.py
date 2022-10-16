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

MAX_QSIZE = 12
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1) % MAX_QSIZE
    def clear(self): self.front = self.rear
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % MAX_QSIZE]
    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print("[front : %s, rear : %d] ==> "%(self.front, self.rear), out)
        # Q. 포맷팅 시 front는 %s인데 왜 rear는 %d인가?

# Test Code
# q = CircularQueue()
# for i in range(8): q.enqueue(i)
# q.display()
# for i in range(5): q.dequeue()
# q.display()
# for i in range(8, 14): q.enqueue(i)
# q.display()