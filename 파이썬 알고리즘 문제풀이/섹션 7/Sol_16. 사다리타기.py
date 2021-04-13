import collections

graph = []

for _ in range(10):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    #print(x, y)
    if x == 0:
        print(y)
        return
    else:
        if y+1 <= 9 and graph[x][y+1] == 1:
            ny = y+1
            q = collections.deque()
            q.append(y+1)
            while(q):
                ny = q.popleft()
                if ny == 9:
                    break
                if graph[x][ny+1] == 1:
                     q.append(ny+1)
            dfs(x-1, ny)
        elif 0 <= y-1 and graph[x][y-1] == 1:
            ny = y-1
            q = collections.deque()
            q.append(y-1)
            while(q):
                if ny == 0:
                    break
                ny = q.popleft()
                if graph[x][ny-1] == 1:
                     q.append(ny-1)
            dfs(x-1, ny)
        else:
            dfs(x-1, y)

dfs(9, graph[9].index(2))