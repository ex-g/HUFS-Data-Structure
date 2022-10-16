from Queue import *

def Fib():
    n = int(input("n을 입력하세요 : "))
    q = CircularQueue()
    q.enqueue(1); q.enqueue(1)
    for i in range(1, n+1):
        q.enqueue(q.items[(q.front+1)%MAX_QSIZE] + q.items[q.rear])
        print(q.dequeue(), end=' ')

Fib()

