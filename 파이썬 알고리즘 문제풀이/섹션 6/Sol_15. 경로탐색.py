n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

ans = 0

#n, m = 5, 9
#graph = [[], [2, 3, 4], [1, 3, 5], [4], [2, 5], []]

def dfs(v, arr):
    global ans
    if v == n:
        ans += 1
        return
    else:
        for i in graph[v]:
            if not i in arr:
                dfs(i, arr+[i])
dfs(1, [1])
print(ans)