import sys
n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

a = []
visited = [False]*n

def dfs(level, a):
    if level == 4:
        print(1)
        sys.exit()
    else:
        for i in graph[a[-1]]:
            if visited[i] == False:
                visited[i] = True
                a.append(i)
                dfs(level+1, a)
                a.pop()
                visited[i] = False

for i in range(n):
    a.append(i)
    visited[i] = True
    dfs(0, a)
    visited[i] = False
    a = []

print(0)