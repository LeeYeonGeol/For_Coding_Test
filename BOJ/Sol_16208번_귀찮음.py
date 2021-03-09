n = int(input())

li = list(map(int, input().split()))

li.sort()
target = sum(li)
ans = 0

for i in li:
    ans += i*(target-i)
    target = target-i
print(ans)