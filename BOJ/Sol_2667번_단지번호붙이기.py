graph = []
n = int(input())

for i in range(n):
    graph.append(list(map(int,input().rstrip())))

cnt = 0
def dfs(x,y):
    global cnt
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

ans = 0
ans2 = []
for i in range(n):
    for j in range(n):
        if dfs(i,j) != 0:
            ans2.append(cnt)
            ans += 1
        cnt = 0

print(ans)
ans2.sort()

for i in ans2:
    print(i)