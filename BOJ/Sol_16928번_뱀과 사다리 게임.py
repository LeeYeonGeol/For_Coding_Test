from collections import deque
import sys
input = sys.stdin.readline

# n = 사다리 수, m = 뱀의 수
n, m = map(int, input().split())

graph = [0]*101
visited = [False]*101

for _ in range(n+m):
    a, b = map(int, input().split())
    graph[a] = b

q = deque()
q.append((1, 0))
visited[1] = True

while q:
    where, cnt = q.popleft()

    if where == 100:
        print(cnt)
        break

    for i in range(1, 7):
        nwhere = where + i
        if 1 <= nwhere <= 100:
            if graph[nwhere] == 0 and visited[nwhere] == False:
                visited[nwhere] = True
                q.append((nwhere, cnt+1))
            elif graph[nwhere] != 0 and visited[graph[nwhere]] == False:
                q.append((graph[nwhere], cnt+1))