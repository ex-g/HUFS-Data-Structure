# 연습문제
# 4.1 ----------------------------------------------------------------- #
"""
(1) LIFO / (3) FILO
"""
# 4.2 ----------------------------------------------------------------- #
"""
(3) 운영체제의 작업 스케줄링
    - 이에 가장 적합한 자료구조는 큐(queue)이다.
"""
# 4.3 ----------------------------------------------------------------- #
"""
(1) 입출력이 한쪽 끝으로만 제한된 리스트이다.
(4) 배열 구조와 연결된 구조로 구현이 가능하다.
(5) 함수 호출시 복귀 주소를 저장하는 데 사용된다.
"""
# 4.4 ----------------------------------------------------------------- #
"""
(2) E, D, C, B, A
"""
# 4.5 ----------------------------------------------------------------- #
"""
10, 20
"""
# 4.6 ----------------------------------------------------------------- #
"""
(1) D, A, B, C
"""
# 4.7 ----------------------------------------------------------------- #
"""
공백상태 : 파이썬 내에서 할당한 배열에 아직 공간이 남음
포화상태 : 파이썬 내에서 할당한 배열에 공간이 꽉 차서 새 배열을 할당해야 함.
"""
# 4.8 ----------------------------------------------------------------- #
"""
삽입연산, 삭제연산의 시간복잡도 : O(1) - 후단을 스택의 상단으로 이용했기 때문
"""
# 4.9 ----------------------------------------------------------------- #
"""
▼ 아래 함수를 Stack class에 추가하면 됨.
def display(self):
    for i in range(self.size()-1, -1, -1):
        print(self.top[i])
"""
# 4.10 ----------------------------------------------------------------- #
"""
15개
"""
# 4.11 ----------------------------------------------------------------- #
"""
예외처리 생략. (시험 범위를 벗어남.)
"""
# 4.12 ----------------------------------------------------------------- #
"""
1) n이 2로 얼만큼 나눠질 수 있는지와,
2) 0이 될 때까지 2로 나눴을 때 각각의 상황에 대한 나머지 (0 or 1)를 확인함.
"""
# 4.13 ----------------------------------------------------------------- #
"""
1) 0, 3, 6, 9
2) 0, 9, 12, 18
"""
# 4.14 ----------------------------------------------------------------- #
"""
ch :  a         stack :  []
ch :  {         stack :  ['{']
ch :  b         stack :  ['{']
ch :  [         stack :  ['{', '[']
ch :  (         stack :  ['{', '[', '(']
ch :  c         stack :  ['{', '[', '(']
ch :  +         stack :  ['{', '[', '(']
ch :  d         stack :  ['{', '[', '(']
ch :  )         stack :  ['{', '[']
ch :  *         stack :  ['{', '[']
ch :  e         stack :  ['{', '[']
ch :  ]         stack :  ['{']
ch :  -         stack :  ['{']
ch :  f         stack :  ['{']
ch :  }         stack :  []
a{b[(c+d)*e]-f} ---> True
"""
# 4.15 ----------------------------------------------------------------- #
"""
A B / C *
A B C * + D E / -
X Y + W Z * V / -
U V * W * X + Y -
A B / C * D - E +
A B C + * D / E -
"""
# 4.16 ----------------------------------------------------------------- #
"""
전위식 표현 생략. (시험 범위를 벗어남.)
"""
# 4.17 ----------------------------------------------------------------- #
"""
(1) A + (B - C) * D
(2) (A + B) / (C - D) + E
(3) A + B / (C + D * E)
(4) X - (Y + Z) * (A - B)
(5) A + B - C + D * E
"""
# 4.18 ----------------------------------------------------------------- #
"""
(1) B + E
(2) (B + E) * D
(3) A - (B + E) * D
"""
# 4.19 ----------------------------------------------------------------- #
"""
미로 탐색 생략. (시험 범위에서 벗어남.)
"""