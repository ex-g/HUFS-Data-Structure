from Deque import *

# Queue.py의 MAX_SIZE 값에 유의할 것!
def isPalindrom():
    str = [w.lower() for w in input("문자열을 입력하세요 : ") if w.isalpha()]
    dq = CircularDeque()
    for s in str:
        dq.addFront(s)
    while dq.size() > 1:
        if dq.deleteFront() != dq.deleteRear():
            return False
    return True

print(isPalindrom())