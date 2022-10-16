from ArrayList import *

class newArrayLlist(ArrayList):
    def __init__(self):
        self.items = []
    """
    (1) append 함수 추가 및 insert 함수 재정의
    """
    def append(self, elem):
        self.items.append(elem)
    def insert(self, pos, elem):
        temp = []
        for _ in range(pos, self.size()):
            temp.append(self.items.pop())
        self.items.append(elem)
        for _ in range(len(temp)):
            self.items.append(temp.pop())
    """
    (2) pop 함수 추가 및 delete 함수 재정의
    """
    def pop(self):
        if self.items:
            self.items.pop(-1)
    def delete(self, pos):
        temp = []
        for i in range(pos+1, self.size()):
            temp.append(self.items.pop())
        self.items.pop()
        for i in range(len(temp)):
            self.items.append(temp.pop())
    """
    (3) find 연산 재정의
    """
    def find(self, pos):
        temp = []
        for _ in range(pos, self.size()):
            temp.append(self.items.pop())
        idx = temp[-1]
        for _ in range(len(temp)):
            self.items.append(temp.pop())
        return idx    
    """
    (4) extend 연산 재정의
    """
    def merge(self, lst):
        for i in lst.items:
            self.items.insert(self.size(), i)
        return lst

# lst = newArrayLlist()
# lst.insert(0, 1)
# lst.insert(1, 2)
# lst.insert(2, 3)
# lst.insert(1, 4)
# lst.display("lst1 insert x 4 : ")
# lst.delete(1)
# lst.display("delete x 1 : ")
# print("find x 1 : ", lst.find(1))

# lst2 = newArrayLlist()
# lst2.insert(0, 100)
# lst2.insert(0, 99)
# lst2.insert(0, 98)
# lst2.display("\nlst2 insert x 3 : ")
# lst.merge(lst2)
# lst.display("lst1 + lst2 merge : ")