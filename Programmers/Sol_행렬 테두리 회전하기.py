def solution(rows, columns, queries):
    answer = []

    graph = [[0]*columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = cnt
            cnt += 1
    for query in queries:
        x1, y1, x2, y2 = query
        n1, n2 = x2-x1, y2-y1
        x, y = x1-1, y1-1
        nx, ny = 0, 0

        value = int(1e9)
        for _ in range(n1):
            graph[x][y+1], graph[x][y] = graph[x][y], graph[x][y+1]
            y += 1

        for _ in range(n2):
            graph[x+1][y], graph[x][y] = graph[x][y], graph[x+1][y]
            x += 1


        for _ in range(n1):
            graph[x][y-1], graph[x][y] = graph[x][y], graph[x][y-1]
            y -= 1

        for _ in range(n2):
            graph[x-1][y], graph[x][y] = graph[x][y], graph[x-1][y]
            x -= 1

        answer.append(value)

    return answer