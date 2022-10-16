Set_ADT = """
데이터 : 같은 유형의 유일한 요소들의 모임. 원소들은 순서는 없지만 서로 비교할 수는 있어야 함.
연산
● Set()              : 비어 있는 새로운 집합을 만든다.
● size()             : 집합의 원소의 개수를 반환한다.
● contains(e)        : 집합이 원소 e를 포함하는지 검사하고 반환함. 
● insert(e)          : 새로운 요소 e를 삽입함. 이미 e가 있다면 삽입하지 않음. O(n)
● delete(pos)        : 원소 e를 집합에서 꺼내고(삭제) 반환한다. O(n)
● equals(setB)       : setB와 같은 집합인지를 검사. 
● union(setB)        : setB와의 합집합을 만들어 반환한다. O(n^2)
● intersect(setB)    : setB와의 교집합을 만들어 반환한다. O(n^2)
● difference(setB)   : setB와의 차집합을 만들어 반환한다. O(n^2)
● display()          : 집합을 화면에 출력한다.
"""

class Set:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def display(self, msg):
        print(msg, self.items)
    def contains(self, item):
        return item in self.items
    def insert(self, elem):
        if elem not in self.items: 
            self.items.append(elem)
    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)
    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC
    def intersect(self, setB):
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC
    def difference(self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC
    def properSet(self, setB):
        if self.size() >= setB.size():
            return False
        else:
            for i in self.items:
                if i not in setB.items:
                    return False
        return True
    
# Test Code
# setA = Set()
# setA.insert("휴대폰"); setA.insert("지갑"); setA.insert("손수건")
# setA.display("Set A : ")

# setB = Set()
# setB.insert("빗"); setB.insert("파이썬 자료구조"); setB.insert("야구공"); setB.insert("지갑")
# setB.display("Set B : ")

# setC = Set()
# setC.insert("휴대폰"); setC.insert("지갑"); setC.insert("손수건"); setC.insert("향수")
# setC.display("Set C : ")
# print("A는 C의 진부분집합? : ", setA.properSet(setC))

# setB.insert("빗")
# setA.delete("손수건")
# setA.delete("발수건")
# setA.display("SetA : ")
# setB.display("SetB : ")

# setA.union(setB).display("A U B : ")
# setA.intersect(setB).display("A ^ B : ")
# setA.difference(setB).display("A - B : ")

