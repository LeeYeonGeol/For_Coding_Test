from collections import deque
n, m = map(int, input().split())

# 가벼운 거 / 무거운 거 나눠서 따지기
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph1[a].append(b)
    graph2[b].append(a)

ans = set()


for k in range(1, n+1):
    q = deque()
    visited = [False]*(n+1)
    q.append((k, 1))
    visited[k] = True
    mark = 0

    while q:
        now, level = q.popleft()
        if mark > n//2:
            ans.add(k)
            break

        for v in graph1[now]:
            if visited[v] == False:
                visited[v] = True
                q.append((v, level+1))
                mark += 1

for k in range(1, n+1):
    q = deque()
    visited = [False]*(n+1)
    q.append((k, 1))
    visited[k] = True
    mark = 0

    while q:
        now, level = q.popleft()
        if mark > n//2:
            ans.add(k)
            break

        for v in graph2[now]:
            if visited[v] == False:
                visited[v] = True
                q.append((v, level+1))
                mark += 1

print(len(ans))