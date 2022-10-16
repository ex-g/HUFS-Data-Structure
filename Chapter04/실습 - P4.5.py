from infix2Postfix import *

infix = [w for w in input("수식을 입력하세요(띄어쓰기로 구분): ").split() if w.isnumeric() or w in ('+', '-', '*', '/')]
postfix = Infix2Postfix(infix)
# print(postfix)
result = evalPostfix(postfix)
print(result)

# Test Code (터미널에 입력)
# ( 10 / 5 ) * 2