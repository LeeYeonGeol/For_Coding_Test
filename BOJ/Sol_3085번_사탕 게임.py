n = int(input())

a = []

for _ in range(n):
    a.append(list(input()))

ans = 1
def check(start_row, end_row, start_col, end_col):
    global ans
    sub = 1
    for i in range(start_row, end_row+1):
        cnt = 1
        for j in range(n-1):
            if a[i][j] == a[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            sub = max(sub, cnt)

    for i in range(start_col, end_col+1):
        cnt = 1
        for j in range(n-1):
            if a[j][i] == a[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            sub = max(sub, cnt)
    ans = max(ans, sub)

for x in range(n):
    for y in range(n):
        if x+1 < n:
            a[x][y], a[x+1][y] = a[x+1][y], a[x][y]
            check(x,x+1,y,y)
            a[x][y], a[x+1][y] = a[x+1][y], a[x][y]
        if y+1 < n:
            a[x][y], a[x][y+1] = a[x][y+1], a[x][y]
            check(x,x,y,y+1)
            a[x][y], a[x][y+1] = a[x][y+1], a[x][y]

print(ans)