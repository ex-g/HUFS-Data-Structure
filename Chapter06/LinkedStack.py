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

class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None
    def isEmpty(self): return self.top == None
    def clear(self): self.top = None
    def push(self, item):
        n = Node(item, self.top)
        self.top = n
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
    def peek(self):
        if not self.isEmpty():
            return self.top.data
    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self, msg='LinkedStack'):
        print(msg, end='')
        node = self.top
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

# Test Code
# odd = LinkedStack()
# even = LinkedStack()
# for i in range(10):
#     if i%2 == 0:
#         even.push(i)
#     else:
#         odd.push(i)
# even.display('스택 even push 5회 : ')
# odd.display('스택 odd push 5회 : ')
# print('스택 even peek : ', even.peek())
# print('스택 odd peek : ', odd.peek())
# for _ in range(2):
#     even.pop()
# for _ in range(3):
#     odd.pop()
# even.display('스택 even pop 2회 : ')
# odd.display('스택 odd pop 2회 : ')