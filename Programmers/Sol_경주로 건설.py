import sys
sys.setrecursionlimit(10**9)

answer = int(1e9)
def solution(board):
    global answer
    n = len(board)

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    visited = [[False]*n for _ in range(n)]

    nprice = [[int(1e9)]*n for _ in range(n)]
    nprice[0][0] = 0

    def dfs(x,y,px,py,cost):
        global answer

        if cost > nprice[x][y]:
            return
        else:
            nprice[x][y] = cost

        if x == n-1 and y == n-1:
            answer = min(answer, cost)
            return
        if answer <= cost:
            return

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                if x == 0 and y == 0:
                    dfs(nx, ny, x, y, cost+100)
                else:
                    # 직선
                    if (px == x == nx) or (py == y == ny):
                        dfs(nx, ny, x, y, cost+100)
                    else:
                        dfs(nx, ny, x, y, cost+600)
                visited[nx][ny] = False

    visited[0][0] = True
    dfs(0, 0, 0, 0 ,0)

    return answer