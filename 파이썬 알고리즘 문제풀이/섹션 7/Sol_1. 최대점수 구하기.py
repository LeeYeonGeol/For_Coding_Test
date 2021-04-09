n, m = map(int, input().split())

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

score = 0
def dfs(start, csum, time):
    global score
    if time > m:
        return

    score = max(score, csum)

    for i in range(start, n):
        dfs(i+1, csum+arr[i][0], time+arr[i][1])

dfs(0, 0, 0)
print(score)
