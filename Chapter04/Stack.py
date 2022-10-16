Stack_ADT = """
데이터 : 후입선출(LIFO)의 접근 방법을 유지하는 항목들의 모음
연산
● Stack()    : 비어 있는 새로운 스택을 만든다.
● isEmpty()  : 스택이 비어 있으면 True를 아니면 False를 반환한다.
● push(e)    : 항목 e를 스택의 맨 위에 추가한다. O(1)
● pop()      : 스택의 맨 위에 있는 항목을 꺼내 반환한다. O(1)
● peek       : 스택의 맨 위에 있는 항목을 삭제하지 않고 반환한다.
● size()     : 스택 내의 모든 항목들의 개수를 반환한다.
● clear()    : 스택을 공백상태로 만든다.
"""

class Stack:
    def __init__(self):
        self.top = []
    def isEmpty(self):
        return len(self.top) == 0
    def size(self):
        return len(self.top)
    def clear(self):
        self.top = []
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def __str__(self):
        return str(self.top)

# Test Code
# odd = Stack()
# even = Stack()
# for i in range(10):
#     if i%2 == 0:
#         even.push(i)
#     else:
#         odd.push(i)
# print('스택 even push 5회 : ', even)
# print('스택 odd push 5회 : ', odd)
# print('스택 even peek : ', even.peek())
# print('스택 odd peek : ', odd.peek())
# for _ in range(2):
#     even.pop()
# for _ in range(3):
#     odd.pop()
# print('스택 even pop 2회 : ', even)
# print('스택 odd pop 3회 : ', odd)