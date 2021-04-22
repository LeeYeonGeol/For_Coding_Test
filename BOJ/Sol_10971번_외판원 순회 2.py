import sys
import itertools
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

ans = int(1e9)

visited = [False]*n
def dfs(level, a,csum):
    global ans
    if csum > ans:
        return
    if level == n and graph[a[-1]][a[0]]:
        ans = min(ans, csum+graph[a[-1]][a[0]])
        return
    else:
        for i in range(n):
            if visited[i] == False:
                if not a:
                    visited[i] = True
                    dfs(level+1, a+[i], csum)
                    visited[i] = False
                else:
                    if graph[a[-1]][i] > 0:
                        visited[i] = True
                        dfs(level+1, a+[i], csum+graph[a[-1]][i])
                        visited[i] = False

dfs(0,[],0)
print(ans)