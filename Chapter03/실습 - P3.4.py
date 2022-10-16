Polynomial_ADT = """
데이터 : 하나 이상의 항으로 이루어진 수학적 표현.
연산
● Polynomial() : 비어있는 다항식을 새로 하나 만든다.
● degree() : 다항식의 차수를 반환한다.
● evaluate(scalar) : 미지수에 scalar를 넣어 계산한 결과를 반환한다.
● add(rhs) : 현재 다항식과 다항식 rhs를 더한 새로운 다항식을 만들어 반환한다.
● subtract(rhs) : 현재 다항식에서 다항식 rhs를 뺀 새로운 다항식을 만들어 반환한다.
● multiply(rhs) : 현재 다항식과 다항식 rhs를 곱한 새로운 다항식을 만들어 반환한다.
● display() : 현재 다항식을 화면에 보기 좋게 출력한다.
"""

class Polynomial:
    def __init__(self):
        self.items = []
    def append(self, item):
        self.items.append(item)
    def read_poly(self):
        a = int(input("다항식의 최고 차수를 입력하세요 : "))
        for i in range(a, -1, -1):
            self.items.append(int(input(f"\tx^{i}의 계수 : ")))
        self.items = self.items[::-1]
    def degree(self):
        return len(self.items)
    def evaluate(self, scalar):
        sum = 0
        for i in range(len(self.items)):
            sum += self.items[i]*scalar**i
        return sum
    def display(self, msg=''):
        lst = []
        for i in range(len(self.items)):
            if i != 0:
                lst.append(f"{float(self.items[i])} x^{i}")
            else:
                lst.append(f"{float(self.items[i])}")
        lst = lst[::-1]
        lst = ' '.join(['+ '+w if (w != lst[0] and w[0] != '-') else w for w in lst])
        return ' '.join([msg, lst])
    def add(self, rhs):
        lst = Polynomial()
        a = 0
        b = 0
        while a < len(self.items) and b < len(rhs.items):
            lst.append(self.items[a] + rhs.items[b])
            a += 1
            b += 1
        while a < len(self.items):
            lst.append(self.items[a])
            a += 1
        while b < len(rhs.items):
            lst.append(rhs.items[b])
            b += 1
        return lst.display()

"""
subtract(rhs), multiply(rhs) 생략, 
Test Code 다른 점 있음
"""
# Test Code
# a = Polynomial()
# b = Polynomial()
# c = Polynomial()

# a.read_poly()
# b.read_poly()
# print(a.display("A(x) = "))
# print(b.display("B(x) = "))
# print("C(x) = ", a.add(b))
# print("\nA(2) = ", a.evaluate(2))