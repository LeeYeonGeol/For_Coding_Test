def solution(m, n, puddles):

    graph = [[0]*(m+1) for _ in range(n+1)]
    for puddle in puddles:
        a, b = puddle
        graph[b][a] = -1

    graph[1][1] = 1
    for x in range(1, n+1):
        for y in range(1, m+1):
            if graph[x][y] != -1:
                if graph[x-1][y] >= 0:
                    graph[x][y] += graph[x-1][y]
                if graph[x][y-1] >= 0:
                    graph[x][y] += graph[x][y-1]

    return graph[n][m] % 1000000007