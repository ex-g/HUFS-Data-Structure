from LinkedList import *

class newList(Node, LinkedList):
    def __init__(self):
        self.head = None
    def reverseDisplay(self, size):
        node = self.head
        for _ in range(size-1):
            node = node.link
        print(node.data, end='')
        size -= 1
        if size != 0:
            print("->", end='')
            return self.reverseDisplay(size)
        
lst = newList()
def program17():
    n = int(input("노드의 개수 : "))
    for i in range(1, n + 1):
        lst.insert(0, int(input(f"노드 #{i} 데이터 : ")))
    user = int(input("탐색할 값을 입력하시오: "))
    cnt = 0
    for i in range(lst.size()):
        if lst.getEntry(i) == user:
            cnt += 1
    print(f"{user}는 연결리스트에서 {cnt}번 나타납니다.")

program17()
