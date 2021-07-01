from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for ed in edge:
        a, b = ed
        graph[a].append(b)
        graph[b].append(a)

    visited = [False]*(n+1)
    q = deque()
    q.append(1)
    visited[1] = True

    ans = 0
    while q:
        n = len(q)
        for _ in range(n):
            v = q.popleft()
            for i in graph[v]:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)

    return n