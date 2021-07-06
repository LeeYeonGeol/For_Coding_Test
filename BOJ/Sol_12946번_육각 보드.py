import sys
sys.setrecursionlimit(10**9)

n = int(input())

board = []

for _ in range(n):
    board.append(list(input()))

dx = [-1,-1,0,0,1,1]
dy = [0,1,-1,1,-1,0]

ans = 0

def dfs(x, y):
    global ans
    ans = max(ans, 1)

    # 다음 방향
    for k in range(6):
        nx, ny = x+ dx[k], y+ dy[k]

        if 0 <= nx < n and 0 <= ny <n and board[nx][ny] == 'X':
            if  visited[nx][ny] == 0:
                visited[nx][ny] = -visited[x][y]
                dfs(nx, ny)
                ans = max(ans, 2)
            else:
                if visited[nx][ny] == visited[x][y]:
                    ans = max(ans, 3)
                    return

visited = [[0]*n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if board[x][y] == 'X' and visited[x][y] == 0:
            visited[x][y] = 1
            dfs(x, y)


print(ans)