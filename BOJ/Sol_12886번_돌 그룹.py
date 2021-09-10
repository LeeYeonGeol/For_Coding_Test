from collections import deque, defaultdict
import sys
a, b, c = map(int, input().split())

q = deque()
q.append([a, b, c])
visited = defaultdict(bool)

while q:
    na, nb, nc = q.popleft()
    if na == nb == nc:
        print(1)
        sys.exit()

    sub = sorted([na,nb,nc])
    # 0, 1
    if sub[0] == sub[1] or 2*sub[0] == sub[1]:
        pass
    else:
        n_sub = sorted([2*sub[0], sub[1]-sub[0],sub[2]])
        if not visited[tuple(n_sub)]:
            visited[tuple(n_sub)] = True
            q.append(n_sub)
    # 0, 2
    if sub[0] == sub[2] or 2*sub[0] == sub[2]:
        pass
    else:
        n_sub = sorted([2*sub[0], sub[2]-sub[0],sub[1]])

        if not visited[tuple(n_sub)]:
            visited[tuple(n_sub)] = True
            q.append(n_sub)
    # 1, 2
    if sub[1] == sub[2] or 2*sub[1] == sub[2]:
        pass
    else:
        n_sub = sorted([2*sub[1], sub[2]-sub[1],sub[0]])
        if not visited[tuple(n_sub)]:
            visited[tuple(n_sub)] = True
            q.append(n_sub)
print(0)