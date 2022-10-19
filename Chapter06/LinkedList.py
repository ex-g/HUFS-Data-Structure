List_ADT = """
데이터 : 같은 유형의 요소들의 순서 있는 모임
연산
● List()             : 비어 있는 새로운 리스트를 만든다.
● insert(pos, e)     : pos 위치에 새로운 요소 e를 삽입한다. O(n)
● delete(pos)        : pos 위치에 있는 요소를 꺼내고(삭제) 반환한다. O(n)
● isEmpty()          : 리스트가 비어있는지를 검사한다.
● getEntry(pos)      : pos 위치에 있는 요소를 반환한다. O(n)
● size()             : 리스트 안의 요소의 개수를 반환한다.
● clear()            : 리스트를 초기화한다.
● find(item)         : 리스트에서 item이 있는지 찾아 인덱스를 반환한다.
● replace(pos, item) : pos에 있는 항목을 item으로 바꾼다.
● sort()             : 리스트의 항목들을 어떤 기준으로 정렬한다.
● merge(lst)         : 다른 리스트 lst를 리스트에 추가한다.
● display()          : 리스트를 화면에 출력한다.
● append(e)          : 리스트의 맨 뒤에 새로운 항목을 추가한다.
"""

class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self): return self.head == None
    def clear(self): self.head = None
    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self, msg='LinkedList'):
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()
    def reverseDisplay(self, size, msg=''):
        node = self.head
        for _ in range(size-1):
            node = node.link
        print(msg, node.data, end=' ')
        size -= 1
        if size != 0:
            return self.reverseDisplay(size)
    def getNode(self, pos):
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None: return None
        else: return node.data
    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None: node.data = elem
    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data: return node
            node = node.link
        return None
    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

# Test Code
# s = LinkedList()
# s.display('단순연결리스트로 구현한 리스트(초기상태) : ')
# s.insert(0, 10); s.insert(0, 20); s.insert(1, 30)
# s.insert(s.size(), 40); s.insert(2, 50)
# s.display('단순연결리스트로 구현한 리스트(삽입 x 5) : ')
# s.replace(2, 90)
# s.display('단순연결리스트로 구현한 리스트(교체 x 1) : ')
# s.delete(2); s.delete(s.size() - 1); s.delete(0)
# s.display('단순연결리스트로 구현한 리스트(삭제 x 3) : ')
# s.clear()
# s.display('단순연결리스트로 구현한 리스트(정리 후) : ')

# reverseDisplay Test Code
# s = LinkedList()
# s.display("단순연결리스트로 구현한 리스트(초기상태) : ")
# s.insert(0, 'D'); s.insert(0, 'C'); s.insert(0, 'B'); s.insert(0, 'A')
# # s.display("삽입 x 5 : ")
# # s.reverseDisplay(s.size())