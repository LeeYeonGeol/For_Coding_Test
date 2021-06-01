from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# a는 시간 기록, v는 경로 기록
a = [-1]*200000
v = [-1]*200000

q = deque()

q.append(n)

a[n] = 0

while q:
    x = q.popleft()

    for nxt in [x-1, x+1, 2*x]:
        if nxt < 0 or nxt >= 200000:
            continue
        if a[nxt] == -1 and v[nxt] == -1:
            q.append(nxt)
            a[nxt] = a[x]+1
            v[nxt] = x

ans = []

print(a[k])

while(1):
    ans.append(str(k))
    k = v[k]

    if k == -1:
        break

print(" ".join(ans[::-1]))
