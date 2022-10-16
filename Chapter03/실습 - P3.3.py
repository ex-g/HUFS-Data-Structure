from Set import *
from ArrayList import *

class newSet(Set):
    def __init__(self):
        self.items = []
    """
    (1) in 연산자 사용하지 않고 contains() 구현
    """
    def contains(self, items):
        for i in range(self.size()):
            if self.items[i] == items:
                return True
        return False
    """
    (2) in 연산자와 remove()를 사용하지 않는 delete()연산,
    그리고 그를 위한 pop() 연산
    """
    def pop(self):
        if self.items:
            self.pop()
    def delete(self, elem):
        if self.contains(elem):
            lst = ArrayList()
            for i in range(self.size()):
                if self.items[i] != elem:
                    lst.insert(0, elem)
                else:
                    return self.pop()
    """
    (3) in 연산자를 사용하지 않는 insert(), union(), intersect(), difference() 연산
    """
    def insert(self, elem):
        if not self.contains(elem):
            self.items.append(elem)
    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items:
            if not self.contains(elem):
                setC.items.append(elem)
        return setC
    def intersect(self, setB):
        setC = Set()
        for elem in setB.items:
            if not self.contains(elem):
                setC.items.append(elem)
        return setC
    def difference(self, setB):
        setC = Set()
        for elem in self.items:
            if not setB.contains(elem):
                setC.items.append(elem)
        return setC
    """
    (4) 연산자 중복을 이용한 difference() 함수 / 모르겠음
    """
    def __sub__(self, setB):
        return self.items - setB.items
    """
    (5) isSubsetOf(otherSet) 연산
    """
    def isSubsetOf(self, setB):
        if self.size() == setB.size():
            return False
        else:
            for i in self.items:
                if i not in setB.items:
                    return False
        return True

# A = Set()
# B = Set()
# A.insert(1); A.insert(2); A.insert(3)
# B.insert(4); B.insert(5); B.insert(6)
# print(A.items, B.items)