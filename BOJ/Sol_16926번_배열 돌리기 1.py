import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt = (min(len(graph), len(graph[0]))) // 2

def rotate(graph):
    ngraph = [[0]*m for _ in range(n)]

    for i in range(cnt):
        n1 = (i, i)
        n2 = (n-1-i,i)
        n3 = (n-1-i,m-1-i)
        n4 = (i,m-1-i)

        # n1 -> n2
        x, y = n1
        nx, ny = n2
        for k in range(x, nx):
            ngraph[k+1][y] = graph[k][y]

        # n2 -> n3
        x, y = n2
        nx, ny = n3
        for k in range(y, ny):
            ngraph[x][k+1] = graph[x][k]

        # n3 -> n4
        x, y = n3
        nx, ny = n4
        for k in range(x, nx, -1):
            ngraph[k-1][y] = graph[k][y]

        # n4 -> n1
        x, y = n4
        nx, ny = n1
        for k in range(y, ny, -1):
            ngraph[x][k-1] = graph[x][k]
    return ngraph

for _ in range(r):
    graph = rotate(graph)

for g in graph:
    print(" ".join(list(map(str,g))))
