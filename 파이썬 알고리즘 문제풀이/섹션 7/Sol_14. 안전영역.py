import sys
sys.setrecursionlimit(10**9)

n = int(input())

arr = []
end = 0
for _ in range(n):
    sub = list(map(int, input().split()))
    arr.append(sub)
    end = max(end, max(sub))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(a, b, i):
    for k in range(4):
        nx = a + dx[k]
        ny = b + dy[k]
        if 0<= nx < n and 0<= ny < n:
            if arr[nx][ny] > i and visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny, i)
ans = 0
for i in range(end+1):
    visited = [[False]* n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] > i and visited[x][y] == False:
                cnt += 1
                visited[x][y] = True
                dfs(x, y, i)
    ans = max(cnt, ans)
print(ans)


