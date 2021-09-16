from collections import deque, defaultdict
import sys
n = int(input())

li = list(map(int, input().split()))

target = int(input())

graph = [[] for _ in range(n)]


root = -1
for idx, l in enumerate(li):
    if l != -1:
        graph[l].append(idx)
    else:
        root = idx

if root == target:
    print(0)
    sys.exit()

q = deque()

q.append(target)

visited1 = [False]*n

visited1[target] = True

# 노드 지우기

while q:
    v = q.popleft()
    for n_v in graph[v]:
        if visited1[n_v] == False:
            visited1[n_v] = True
            q.append(n_v)
    graph[v] = []


# 리프 노드 찾기

visited2 = [False]*n

visited2[root] = True

ans = 0

q.append(root)

while q:
    v = q.popleft()
    mark = True
    for n_v in graph[v]:
        if visited1[n_v] == False:
            visited1[n_v] = True
            q.append(n_v)
            mark = False
    if mark == True:
        ans += 1

print(ans)