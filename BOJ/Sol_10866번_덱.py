from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

q = deque()

for _ in range(n):
    li = list(input().split())
    if li[0] == 'push_front':
        q.appendleft(int(li[1]))
    elif li[0] == 'push_back':
        q.append(int(li[1]))
    elif li[0] == 'pop_front':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif li[0] == 'pop_back':
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif li[0] == 'size':
        print(len(q))
    elif li[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif li[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif li[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
