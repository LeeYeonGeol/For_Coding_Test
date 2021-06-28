import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

a = []

for i in range(9):
    a.append(list(map(int, input().split())))

c1 = [[False]*10 for _ in range(9)]
c2 = [[False]*10 for _ in range(9)]
c3 = [[False]*10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if a[i][j] != 0:
            c1[i][a[i][j]] = True
            c2[j][a[i][j]] = True
            c3[3*(i//3)+(j//3)][a[i][j]] = True

def go(z):
    if z == 81:
        for aa in a:
            print(" ".join(list(map(str, aa))))
        sys.exit()

    x = z//9
    y = z%9

    if a[x][y] != 0:
        go(z+1)
    else:
        for i in range(1, 10):
            if c1[x][i] == False and c2[y][i] == False and c3[3*(x//3)+(y//3)][i] == False:
                c1[x][i] = c2[y][i] = c3[3*(x//3)+(y//3)][i] = True
                a[x][y] = i
                go(z+1)
                a[x][y] = 0
                c1[x][i] = c2[y][i] = c3[3*(x//3)+(y//3)][i] = False
go(0)