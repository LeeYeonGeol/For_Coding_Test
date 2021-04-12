import collections
import sys
s, e = map(int, input().split())

q = collections.deque()

q.append(s)

ans = [0]*10001

while q:
    where = q.popleft()

    for i in [-1,1,5]:
        if 1 <= where+i <= 10000 and ans[where+i] == 0:
            q.append(where+i)
            ans[where+i] = ans[where]+1

print(ans[e])


