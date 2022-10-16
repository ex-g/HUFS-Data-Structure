PriorityQueue_ADT = """
데이터 : 우선순위를 가진 요소들의 모음
연산
● PriorityQueue()    : 비어 있는 우선순위 큐를 만든다.
● isEmpty()  : 우선순위 큐가 공백상태인지를 검사한다. 
● enqueue(e) : 우선순위를 가진 항목 e를 추가한다. O(1)
● dequeue()  : 가장 우선순위가 높은 항목을 꺼내서 반환한다. O(n)
● peek       : 가장 우선순위가 높은 요소를 삭제하지 않고 반환한다. O(n)
● size()     : 우선순위 큐의 모든 항목들의 개수를 반환한다.
● clear()    : 우선순위 큐를 공백상태로 만든다.
"""

class PriorityQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def size(self): return len(self.items)
    def clear(self): self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def findMaxIndex(self):
        if self.isEmpty(): return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            return highest
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]

# Test Code
# q = PriorityQueue()
# q.enqueue(34)
# q.enqueue(18)
# q.enqueue(27)
# q.enqueue(45)
# q.enqueue(15)
# print("PQueue : ", q.items)
# while not q.isEmpty() : 
#     print("Max Priority = ", q.dequeue())