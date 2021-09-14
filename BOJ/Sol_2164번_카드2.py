from collections import deque

n = int(input())

q = deque()

for k in range(1, n+1):
    q.append(k)

while 1:
    if len(q) == 1:
        break
    q.popleft()

    q.append(q.popleft())


print(q[0])