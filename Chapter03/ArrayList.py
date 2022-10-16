List_ADT = """
데이터 : 같은 유형의 요소들의 순서 있는 모임
연산
● List()             : 비어 있는 새로운 리스트를 만든다.
● insert(pos, e)     : pos 위치에 새로운 요소 e를 삽입한다. O(n)
● delete(pos)        : pos 위치에 있는 요소를 꺼내고(삭제) 반환한다. O(n)
● isEmpty()          : 리스트가 비어있는지를 검사한다.
● getEntry(pos)      : pos 위치에 있는 요소를 반환한다. O(1)
● size()             : 리스트 안의 요소의 개수를 반환한다.
● clear()            : 리스트를 초기화한다.
● find(item)         : 리스트에서 item이 있는지 찾아 인덱스를 반환한다.
● replace(pos, item) : pos에 있는 항목을 item으로 바꾼다.
● sort()             : 리스트의 항목들을 어떤 기준으로 정렬한다.
● merge(lst)         : 다른 리스트 lst를 리스트에 추가한다.
● display()          : 리스트를 화면에 출력한다.
● append(e)          : 리스트의 맨 뒤에 새로운 항목을 추가한다.
"""

class ArrayList:
    def __init__(self):
        self.items = []
    def insert(self, pos, elem):
        self.items.insert(pos, elem)
    def delete(self, pos):
        return self.items.pop(pos)
    def isEmpty(self):
        return self.size() == 0
    def getEntry(self, pos):
        return self.items[pos]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def find(self, item):
        return self.items.index(item)
    def replace(self, pos, elem):
        self.items[pos] = elem
    def sort(self):
        self.items.sort()
    def merge(self, lst):
        self.items.extend(lst)
    def display(self, msg="ArrayList"):
        print(msg, self.size(), self.items)

# Test Code
# s = ArrayList()
# s.display("Python List로 구현한 List Test")
# s.insert(0, 10); s.insert(0, 20); s.insert(1, 30)
# s.insert(s.size(), 40); s.insert(2, 50)
# s.display("insert x 5 : ")
# s.sort()
# s.display("after sort : ")
# s.replace(2, 90)
# s.display("replace x 1 : ")
# s.delete(2); s.delete(s.size()-1); s.delete(0)
# s.display("delete x 3 : ")
# lst = [1, 2, 3]
# s.merge(lst)
# s.display('merge + 3 : ')
# s.clear()
# s.display("after clear : ")