graph = [[], [], [], []]

for _ in range(5):
    sub = list(input().split())
    for k in range(4):
        graph[k].append(list(sub[k]))

ans = []

db = []

db.append([list('###'), list('#.#'), list('#.#'), list('#.#'), list('###')])
db.append([list('..#'), list('..#'), list('..#'), list('..#'), list('..#')])
db.append([list('###'), list('..#'), list('###'), list('#..'), list('###')])
db.append([list('###'), list('..#'), list('###'), list('..#'), list('###')])
db.append([list('#.#'), list('#.#'), list('###'), list('..#'), list('..#')])
db.append([list('###'), list('#..'), list('###'), list('..#'), list('###')])
db.append([list('###'), list('#..'), list('###'), list('#.#'), list('###')])
db.append([list('###'), list('..#'), list('..#'), list('..#'), list('..#')])
db.append([list('###'), list('#.#'), list('###'), list('#.#'), list('###')])
db.append([list('###'), list('#.#'), list('###'), list('..#'), list('###')])

for gg in graph:
    # 비교
    for k in range(10):
        mark = True
        for x in range(5):
            for y in range(3):
                if gg[x][y] == '#' and gg[x][y] != db[k][x][y]:
                    mark = False
                    break
            if mark == False:
                break
        if mark == True:
            ans.append(k)
            break

print(str(ans[0])+str(ans[1])+":"+str(ans[2])+str(ans[3]))
