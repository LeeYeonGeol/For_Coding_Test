from collections import deque
import sys

n, k, m = map(int, input().split())

graph = [[] for _ in range(n+m+1)]

for i in range(1, m+1):
    sub = list(map(int, input().split()))
    graph[n+i] = sub
    for s in sub:
        graph[s].append(n+i)

q = deque()

nvisited = [False] * (n+m+1)

q.append((1, nvisited,1))

nvisited[1] = True

while q:
    subway, visited, level = q.popleft()
    if subway == n:
        print(level)
        sys.exit()

    for s in graph[subway]:
        if visited[s] == False:
            visited[s] = True
            if s > n:
                q.append((s, visited, level))
            else:
                q.append((s, visited, level+1))

print(-1)