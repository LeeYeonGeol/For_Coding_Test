from collections import deque
def solution(board):
    n = len(board)-1
    answer = 0
    visited = set()


    # (0, 0), (0, 1)에서 시작
    visited.add(((0,0),(0,1)))
    visited.add(((0,1),(0,0)))

    q = deque()
    q.append(((0,0),(0,1),0))
    while q:

        s1, s2, cnt = q.popleft()

        if s1 == (n,n) or s2 == (n,n):
            return cnt

        x1, y1 = s1
        x2, y2 = s2

        de = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # 평행 이동
        for d in de:
            dx, dy = d
            nx1, ny1 = x1+dx, y1+dy
            nx2, ny2 = x2+dx, y2+dy
            if 0 <= nx1 <= n and 0 <= ny1 <= n and 0 <= nx2 <= n and 0 <= ny2 <= n:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0 and not ((nx1, ny1), (nx2, ny2)) in visited:
                    visited.add(((nx1, ny1), (nx2, ny2)))
                    visited.add(((nx2, ny2), (nx1, ny1)))
                    q.append(((nx1, ny1), (nx2, ny2), cnt+1))

        # 90도 회전
        if x1 == x2:
            for k in [-1, 1]:
                nx1 = x1 + k
                nx2 = x2 + k
                if 0 <= nx1 <= n and 0 <= nx2 <= n and board[nx1][y1] == 0 and board[nx2][y2] == 0:
                    if not ((nx1, y1), (x1, y1)) in visited:
                        visited.add(((nx1, y1), (x1, y1)))
                        visited.add(((x1, y1), (nx1, y1)))
                        q.append(((nx1, y1), (x1, y1), cnt + 1))
                    if not ((nx2, y2), (x2, y2)) in visited:
                        visited.add(((nx2, y2), (x2, y2)))
                        visited.add(((x2, y2), (nx2, y2)))
                        q.append(((nx2, y2), (x2, y2), cnt + 1))

        if y1 == y2:
            for k in [-1, 1]:
                ny1 = y1 + k
                ny2 = y2 + k
                if 0 <= ny1 <= n and 0 <= ny2 <= n and board[x1][ny1] == 0 and board[x2][ny2] == 0:
                    if not ((x1, ny1), (x1, y1)) in visited:
                        visited.add(((x1, ny1), (x1, y1)))
                        visited.add(((x1, y1), (x1, ny1)))
                        q.append(((x1, ny1), (x1, y1), cnt + 1))
                    if not ((x2, ny2), (x2, y2)) in visited:
                        visited.add(((x2, ny2), (x2, y2)))
                        visited.add(((x2, y2), (x2, ny2)))
                        q.append(((x2, ny2), (x2, y2), cnt + 1))