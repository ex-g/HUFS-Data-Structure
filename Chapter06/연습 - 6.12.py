from LinkedCircularQueue import *

class newQueue(Node, CircularLinkedQueue):
    def __init__(self):
        self.tail = None
    def display(self):
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end ='->')
                node = node.link
            print(node.data, end='->None')
        print()

q = newQueue()
def program12():
    while True:
        user = int(input("양의 정수를 입력하세요(종료: -1): "))
        if user == -1:
            return q.display()
        else:
            q.enqueue(user)
            
program12()