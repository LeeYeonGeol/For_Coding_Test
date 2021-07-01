from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    visited = [[-1]*m for _ in range(n)]

    q = deque()

    q.append((0, 0))
    visited[0][0] = 1

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


    return visited[n-1][m-1]