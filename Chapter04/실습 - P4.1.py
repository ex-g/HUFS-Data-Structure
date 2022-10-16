from Stack import *

str = list(input())

stack = Stack()
for s in str:
    stack.push(s)

for i in range(stack.size()):
    print(stack.top.pop(), end = '')
