from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

cycle = []

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(start, here, level):

    if level <= 2:
        for v in graph[here]:
            if visited[v] == False:
                visited[v] = True
                dfs(start, v, level+1)
                visited[v] = False
    else:
        for v in graph[here]:
            if visited[v] == False:
                visited[v] = True
                dfs(start, v, level+1)
                visited[v] = False
            else:
                if v == start:

                    cycle.append(start)
                    return

for i in range(1, n+1):
    visited[i] = True
    dfs(i, i, 1)
    visited[i] = False

# bfs 수행
answer = [int(1e9)] * (n + 1)
q = deque()
for c in cycle:
    q.append((c, 0))
    answer[c] = 0

while q:
    node, level = q.popleft()

    for v in graph[node]:
        if answer[v] == int(1e9):
            answer[v] = level+1
            q.append((v, level+1))


print(" ".join(map(str, answer[1:])))