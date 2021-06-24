from collections import deque
import sys

s, t = map(int, input().split())

if s == t:
    print(0)
    sys.exit()

ans = ""

q = deque()

q.append((s, ""))

MAX = 1000000000

visited = set([s])

while q:
    x, cal = q.popleft()

    if x == t:
        print(cal)
        sys.exit()

    # 4가지 연산 수행
    # 곱하기
    nx = x**2
    if 0 <= nx <= MAX and nx not in visited:
        visited.add(nx)
        q.append((nx, cal+"*"))
    # 더하기
    nx = 2*x
    if 0 <= nx <= MAX and nx not in visited:
        visited.add(nx)
        q.append((nx, cal+"+"))
    # 빼기
    nx = 0
    if 0 <= nx <= MAX and nx not in visited:
        visited.add(nx)
        q.append((nx, cal+"-"))
    # 나누기
    if x != 0:
        nx = 1
        if 0 <= nx <= MAX and nx not in visited:
            visited.add(nx)
            q.append((nx, cal+"/"))

print(-1)