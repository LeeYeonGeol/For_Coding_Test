n, m, r = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def cal1(graph, n, m):
    ngraph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ngraph[i][j] = graph[n-1-i][j]
    return ngraph

def cal2(graph, n, m):
    ngraph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ngraph[i][j] = graph[i][m-1-j]
    return ngraph

def cal3(graph, n, m):
    ngraph = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ngraph[i][j] = graph[n-1-j][i]
    return ngraph

def cal4(graph, n, m):
    ngraph = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ngraph[i][j] = graph[j][m-1-i]
    return ngraph

def cal5(graph, n, m):
    ngraph = [[0]*m for _ in range(n)]

    # 4 -> 1
    for i in range(n//2):
        for j in range(m//2):
            ngraph[i][j] = graph[i+(n//2)][j]

    # 1 -> 2
    for i in range(n//2):
        for j in range(m//2, m):
            ngraph[i][j] = graph[i][j-(m//2)]

    # 2 -> 3
    for i in range(n//2, n):
        for j in range(m//2, m):
            ngraph[i][j] = graph[i-(n//2)][j]

    # 3 -> 4
    for i in range(n//2, n):
        for j in range(m//2):
            ngraph[i][j] = graph[i][j+(m//2)]

    return ngraph

def cal6(graph, n, m):

    ngraph = [[0]*m for _ in range(n)]

    # 2 -> 1
    for i in range(n//2):
        for j in range(m//2):
            ngraph[i][j] = graph[i][j+(m//2)]
    # 3 -> 2
    for i in range(n//2):
        for j in range(m//2, m):
            ngraph[i][j] = graph[i+(n//2)][j]
    # 4 -> 3
    for i in range(n//2, n):
        for j in range(m//2, m):
            ngraph[i][j] = graph[i][j-(m//2)]
    # 1 -> 4
    for i in range(n//2, n):
        for j in range(m//2):
            ngraph[i][j] = graph[i-(n//2)][j]
    return ngraph

yeonsan = list(map(int ,input().split()))

for i in yeonsan:
    n = len(graph)
    m = len(graph[0])
    if i == 1:
        graph = cal1(graph, n, m)
    elif i == 2:
        graph = cal2(graph, n, m)
    elif i == 3:
        graph = cal3(graph, n, m)
    elif i == 4:
        graph = cal4(graph, n, m)
    elif i == 5:
        graph = cal5(graph, n, m)
    else:
        graph = cal6(graph, n, m)

# 답 출력
for g in graph:
    print(" ".join(list(map(str,g))))