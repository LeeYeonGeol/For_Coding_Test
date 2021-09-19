n = int(input())

graph = [['.']*n for _ in range(n)]

robot = list(input())

db = dict()
db['R'] = [0, 1]
db['D'] = [1, 0]
db['L'] = [0,-1]
db['U'] = [-1,0]

# 시작 위치는 (0, 0)
x, y = 0, 0

for direction in robot:
    nx, ny = x + db[direction][0], y + db[direction][1]
    if 0 <= nx < n and 0 <= ny < n:
        # 선 긋기
        # 가로
        if direction == 'R' or direction =='L':
            for xx, yy in [(x, y), (nx, ny)]:
                if graph[xx][yy] == '|':
                    graph[xx][yy] = '+'
                elif graph[xx][yy] == '.':
                    graph[xx][yy] = '-'
        # 세로
        if direction == 'D' or direction =='U':
            for xx, yy in [(x, y), (nx, ny)]:
                if graph[xx][yy] == '-':
                    graph[xx][yy] = '+'
                elif graph[xx][yy] == '.':
                    graph[xx][yy] = '|'
        x, y = nx, ny

for g in graph:
    print("".join(g))