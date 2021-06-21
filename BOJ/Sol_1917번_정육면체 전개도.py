from copy import deepcopy
a = []
a.append([[1,1,1,0,0], [0,0,1,1,1]])
a.append([[0,0,1,0],[1,1,1,1],[0,0,1,0]])
a.append([[0,1,0,0],[1,1,1,1],[1,0,0,0]])
a.append([[0,0,1,0],[1,1,1,1],[0,1,0,0]])
a.append([[0,0,0,1],[1,1,1,1],[1,0,0,0]])
a.append([[0,0,0,1],[1,1,1,1],[0,1,0,0]])
a.append([[1,1,0,0],[0,1,1,1],[0,0,1,0]])
a.append([[1,1,0,0],[0,1,1,1],[0,0,0,1]])
a.append([[0,0,1,0],[1,1,1,0],[0,0,1,1]])
a.append([[0,0,0,1],[1,1,1,1],[0,0,0,1]])
a.append([[1,1,0,0],[0,1,1,0],[0,0,1,1]])

graph = []
for _ in range(18):
    graph.append(list(map(int, input().split())))

ans = []

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

def cal4(graph, n, m):
    ngraph = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ngraph[i][j] = graph[j][m-1-i]
    return ngraph

na = []

# 그냥
for aa in a:
    aaa = deepcopy(aa)
    na.append(aaa)
    aaa = cal4(aaa, len(aaa), len(aaa[0]))
    na.append(aaa)
    aaa = cal4(aaa, len(aaa), len(aaa[0]))
    na.append(aaa)
    aaa = cal4(aaa, len(aaa), len(aaa[0]))
    na.append(aaa)

# 반전 후
for aa in a:
    aaa = deepcopy(aa)
    aaa = cal1(aaa, len(aaa), len(aaa[0]))
    na.append(aaa)
    aaa = cal4(aaa, len(aaa), len(aaa[0]))
    na.append(aaa)
    aaa = cal4(aaa, len(aaa), len(aaa[0]))
    na.append(aaa)
    aaa = cal4(aaa, len(aaa), len(aaa[0]))
    na.append(aaa)

for t in range(3):

    ngraph = []
    for i in range(6*t,6*(t+1)):
        if 1 in graph[i]:
            ngraph.append(graph[i])

    ngraph1 = cal4(ngraph, len(ngraph), len(ngraph[0]))
    nngraph1 = []
    for i in range(len(ngraph1)):
        if 1 in ngraph1[i]:
            nngraph1.append(ngraph1[i])

    ans = "no"

    for aa in na:
        if aa == nngraph1:
            ans = "yes"
            break

    print(ans)




