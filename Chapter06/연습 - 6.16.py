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
def program16():
    user = int(input("노드의 개수 : "))
    for i in range(1, user + 1):
        lst.insert(0, int(input(f"노드 #{i} 데이터 : ")))
    sum = 0
    for i in range(lst.size()):
        sum += lst.getEntry(i)
    print("연결 리스트의 데이터 합: ", sum)

program16()
