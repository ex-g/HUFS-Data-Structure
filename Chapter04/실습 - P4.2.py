from Stack import *

def isPalindrom():
    str = [w.lower() for w in input("문자열을 입력하세요 : ") if w.isalpha()]
    judge = True
    if len(str)%2 == 1:
        judge = False
    
    stack = Stack()
    for _ in range(0, len(str) // 2):
        stack.push(str[0])
        str.pop(0)

    if not judge:
        str.pop(0)

    for _ in range(len(str)):
            if str.pop(0) != stack.pop():
                return False
    return True

print(isPalindrom())