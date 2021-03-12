n, m = map(int, input().split())

ans1 = 1
for i in range(n,n-m,-1):
    ans1 *= i

ans2 = 1
for i in range(1, m + 1):
    ans2 *= i
print((ans1//ans2))