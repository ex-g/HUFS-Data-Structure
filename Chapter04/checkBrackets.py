from Stack import *

"""
4.3 스택의 응용 : 괄호 검사 (p.134)
"""
def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or\
                   (ch == "]" and left != "[") or\
                   (ch == ")" and left != "("):
                   return False
        print("ch : ", ch, "\tstack : ", stack)

    return stack.isEmpty()

# Test Code
# str = ( "{A[(i+1)] = 0}", "if( (i==0)&&(j==0 )", "A[ (i+1] ) = 0;" )
# for s in str:
#     m = checkBrackets(s)
#     print(s, "--->", m)
