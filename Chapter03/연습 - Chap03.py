from ArrayList import *
from Set import *
"""
모듈을 직접 실행하면 해당 파일의 이름이 달라지므로 [상대 경로]가 기준 위치를 알 수 없게 되어 경로를 찾지 못한다.
> 파이썬에서 메인 모듈(직접 실행하는 파일)은 절대 경로를 사용해야 한다.
https://daco2020.tistory.com/62
"""

# 연습문제
# 3.1 ----------------------------------------------------------------- #
"""
공통점 : data를 다룸.
차이점 : 리스트는 항목들 사이에 순서가 있고, 집합은 없음.
"""

# 3.2 ----------------------------------------------------------------- #
lst = ArrayList()
lst.insert(0, 10); lst.insert(1, 20); lst.insert(0, 30); lst.insert(2, 40)
lst.insert(lst.size(), 50)
# lst.display()

# 3.3 ----------------------------------------------------------------- #
lst.insert(1, 60); lst.replace(2, 70); lst.delete(2)
# lst.display()

# 3.4 ----------------------------------------------------------------- #
"""
삭제 연산 : 여분의 공간과 상관 없이 그냥 맨 뒤의 원소를 삭제하면 됨
삽입 연산 : 여분의 공간이 없으면, 내부적으로 새로운 배열 할당 후 기존 항목들을 모두 복사해야 함. 이때는 최소 O(n)의 시간이 소요됨.
"""

# 3.5 ----------------------------------------------------------------- #
"""
def maxFind(lst):
    if lst:
        max = lst[0]
        for i in range(1, len(lst)):
            if max < lst[i]:
                max = lst[i]
        return max
    else:
        return None
"""
def maxFind(lst):
    return max(lst)

# print("max : ", maxFind(lst.items))

# 3.6 ----------------------------------------------------------------- #
"""
def maxminFind(lst):
    if lst:
        max = lst[0]
        min = lst[0]
        for i in range(1, len(lst)):
            if max < lst[i]:
                max = lst[i]
            if min > lst[i]:
                min = lst[i]
        return (max, min)
    else:
        return None, None
"""
def maxminFind(lst):
    return max(lst), min(lst)

# max, min = maxminFind(lst.items)
# print("max : ", max, "\nmin : ", min)

# 3.7 ----------------------------------------------------------------- #
def sameValue():
    lst1 = list(map(int, input("첫 번째 리스트 : ").split()))
    lst2 = list(map(int, input("두 번째 리스트 : ").split()))
    for i in lst1:
        for j in lst2:
            if i == j:
                return True
    return False

# print(sameValue())

# 3.8 ----------------------------------------------------------------- #
'''
p.238 참고
'''
def listMerge(lst, lst2):
    newSet = Set()
    a = 0
    b = 0
    while a < len(lst) and b < len(lst2):
        valueA = lst[a]
        valueB = lst2[b]
        if valueA < valueB:
            newSet.items.append(valueA)
            a += 1
        elif valueA > valueB:
            newSet.items.append(valueB)
            b += 1
        else:
            newSet.items.append(valueA)
            a += 1
            b += 1
    while a < len(lst):
        newSet.items.append(lst[a])
        a += 1
    while b < len(lst2):
        newSet.items.append(lst2[b])
        b += 1
    return newSet.items

# lst = [1, 3, 5]
# lst2 = [2, 4, 6, 8, 10]
# print("merged list : ", listMerge(lst, lst2))

# 3.9 ----------------------------------------------------------------- #
"""
▼ 실제 Set 클래스에 추가한 코드
def properSet(self, setB):
        if self.size() >= setB.size():
            return False
        else:
            for i in self.items:
                if i not in setB.items:
                    return False
        return True
"""
def properSubset(setA, setB):
    if len(setA) >= len(setB):
        return False
    else:
        for i in setA:
            if i not in setB:
                return False
    return True

'''case 1 : setA < setB - True반환'''
# setA = (1, 2, 3)
# setB = (1, 2, 3, 4)
'''case 2 : setA = setB : False반환'''
# setA = (1, 2, 3)
# setB = (1, 2, 3)
'''case 3 : setA > setB - False반환'''
# setA = (4, 5, 6, 7)
# setB = (4, 5, 6)

# print(properSubset(setA, setB))