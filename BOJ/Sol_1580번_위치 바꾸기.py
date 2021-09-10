from collections import deque, defaultdict
import copy
import sys
n, m = map(int, input().split())

graph = []

a = [0, 0]
b = [0, 0]
for x in range(n):
    sub = list(input())
    graph.append(sub)
    for y in range(m):
        if sub[y] == 'A':
            a[0], a[1] = x, y
        elif sub[y] == 'B':
            b[0], b[1] = x, y

visited = defaultdict(bool)
visited[(tuple(a), tuple(b))] = True

q = deque()
q.append((a, b, 0))

dx = [0,1,0,-1,1,-1,-1,1]
dy = [1,0,-1,0,1,-1,1,-1]

target_A = copy.deepcopy(b)
target_B = copy.deepcopy(a)

while q:
    A, B, level = q.popleft()

    # AB 둘다 움직이기
    for k in range(8):
        NA = [A[0]+dx[k], A[1]+dy[k]]
        for p in range(8):
            NB = [B[0]+dx[p], B[1]+dy[p]]
            # 벗어나면 안됨
            if 0 <= NA[0] < n and 0 <= NA[1] < m and 0 <= NB[0] < n and 0 <= NB[1] < m:
                # X도 가면 안됨
                if graph[NA[0]][NA[1]] != 'X' and graph[NB[0]][NB[1]] != 'X':
                    # 교차도 안됨
                    if not (NA == B and NB == A) and not (NA == NB):
                        if not visited[(tuple(NA), tuple(NB))]:
                            visited[(tuple(NA), tuple(NB))] = True
                            if NA == target_A and NB == target_B:
                                print(level+1)
                                sys.exit()
                            q.append((NA, NB, level+1))
    # A만 움직이기
    for k in range(8):
        NA = [A[0]+dx[k], A[1]+dy[k]]
        NB = B
        # 벗어나면 안됨
        if 0 <= NA[0] < n and 0 <= NA[1] < m and 0 <= NB[0] < n and 0 <= NB[1] < m:
            # X도 가면 안됨
            if graph[NA[0]][NA[1]] != 'X' and graph[NB[0]][NB[1]] != 'X':
                # 교차도 안됨
                if not (NA == B and NB == A) and not (NA == NB):
                    if not visited[(tuple(NA), tuple(NB))]:
                        visited[(tuple(NA), tuple(NB))] = True
                        if NA == target_A and NB == target_B:
                            print(level+1)
                            sys.exit()
                        q.append((NA, NB, level+1))
    # B만 움직이기
    for k in range(8):
        NA = A
        NB = [B[0]+dx[k], B[1]+dy[k]]
        # 벗어나면 안됨
        if 0 <= NA[0] < n and 0 <= NA[1] < m and 0 <= NB[0] < n and 0 <= NB[1] < m:
            # X도 가면 안됨
            if graph[NA[0]][NA[1]] != 'X' and graph[NB[0]][NB[1]] != 'X':
                # 교차도 안됨
                if not (NA == B and NB == A) and not (NA == NB):
                    if not visited[(tuple(NA), tuple(NB))]:
                        visited[(tuple(NA), tuple(NB))] = True
                        if NA == target_A and NB == target_B:
                            print(level+1)
                            sys.exit()
                        q.append((NA, NB, level+1))
print(-1)