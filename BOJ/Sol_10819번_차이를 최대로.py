import itertools

n = int(input())

arr = list(map(int, input().split()))

cnt = list(itertools.permutations(arr,n))

ans = 0

for k in cnt:
    sub = 0
    for i in range(n-1):
        sub += abs(k[i]-k[i+1])
    ans = max(ans, sub)

print(ans)