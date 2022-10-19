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
def program14():
    user = int(input("노드의 개수 : "))
    for i in range(1, user + 1):
        lst.insert(0, int(input(f"노드 #{i} 데이터 : ")))
    lst.insert(0, int(input("끝에 추가할 데이터: ")))
    print("생성된 연결리스트: ", end='')
    lst.reverseDisplay(lst.size())

program14()
