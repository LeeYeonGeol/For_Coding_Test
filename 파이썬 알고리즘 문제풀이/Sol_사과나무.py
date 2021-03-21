n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
res = 0

s = e = n//2

for i in range(n):
    res += sum(a[i][s:e+1])
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)





