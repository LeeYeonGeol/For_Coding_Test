from collections import deque

n = int(input())

r1, c1, r2, c2 = map(int, input().split())

q = deque()

q.append((r1, c1, 0))

visit = [[False]*n for _ in range(n)]
visit[r1][c1] = True

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

move = False
while q:
    r, c, cnt = q.popleft()
    if r == r2 and c == c2:
        move = True
        print(cnt)
        break
    for i in range(6):
        nr = r + dx[i]
        nc = c + dy[i]
        if nr < 0 or nc < 0 or nr >= n or nc >= n:
            continue
        if visit[nr][nc] == False:
            visit[nr][nc] = True
            q.append((nr,nc,cnt+1))

if move == False:
    print(-1)