import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
"""
부모폴더의 절대경로를 참조 path에 추가
https://seongkyun.github.io/others/2019/04/29/python_import/
"""

from Chapter04.Stack import *

stack1 = Stack()
stack2 = Stack()

def stackQueue(request, item = None):
    global stack1, stack2
    if request == 'push':
        stack1.push(item)
    elif request == 'pop':
        if not stack2.top:
            for i in stack1.top:
                stack2.push(i)
            stack1.clear()
        stack2.pop()

    return stack1.top, stack2.top

# Test Code
# stackQueue('push', 5)
# stackQueue('push', 6)
# stackQueue('push', 7)
# print(stack1.top, stack2.top)
# stackQueue('pop')
# stackQueue('pop')
# stackQueue('push', 8)
# print(stack1.top, stack2.top)