from collections import defaultdict
def solution(rows, columns, queries):
    answer = []
    graph = [[0]*columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = cnt
            cnt += 1

    for a1, b1, a2, b2 in queries:

        db = defaultdict(list)
        x1, y1 = a1-1, b1-1
        x2, y2 = a2-1, b2-1
        x, y = x1, y1
        sub_answer = 1e9
        # 가로 (위)
        for _ in range(y2-y1):
            db[graph[x][y]] += [x,y+1]
            sub_answer = min(sub_answer, graph[x][y])
            y += 1

        # 세로 (오른)
        for _ in range(x2-x1):
            db[graph[x][y]] += [x+1,y]
            sub_answer = min(sub_answer, graph[x][y])
            x += 1

        # 가로 (아래)
        for _ in range(y2-y1):
            db[graph[x][y]] += [x,y-1]
            sub_answer = min(sub_answer, graph[x][y])
            y -= 1

        # 세로 (왼)
        for _ in range(x2-x1):
            db[graph[x][y]] += [x-1,y]
            sub_answer = min(sub_answer, graph[x][y])
            x -= 1
        for value in db:
            nx, ny = db[value]
            graph[nx][ny] = value
        answer.append(sub_answer)
    return answer