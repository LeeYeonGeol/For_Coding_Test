import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]

    edges = []
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        edges.append((a, b))

    visited = [False] * (v+1)
    mark = [0] * (v+1)

    ans = "YES"

    def dfs(i):
        for j in graph[i]:
            if visited[j] == False:
                visited[j] = True
                mark[j] = -mark[i]
                dfs(j)
    # 정점별로 dfs 실행
    for i in range(1, v+1):
        if visited[i] == False:
            visited[i] = True
            mark[i] = 1
            dfs(i)

    for edge in edges:
        if mark[edge[0]] == mark[edge[1]]:
            ans = "NO"
            break
    print(ans)