k = int(input())

target = list(map(int, input().split()))

ans1 = int(1e9)
ans2 = []
ans3 = []
arr = []
for _ in range(k):
    arr.append(list(map(int, input().split())))

def dfs(level, price, n1, n2, n3, n4, st):
    global ans1

    if level > k:
        return

    if price > ans1:
        return

    if n1 >= target[0] and n2 >= target[1] and n3 >= target[2] and n4 >= target[3]:
        ans1 = price
        ans3.append([price, ans2[:]])
        return

    for i in range(st, k):
        ans2.append(i+1)
        dfs(level+1, price+arr[i][4], n1+arr[i][0], n2+arr[i][1], n3+arr[i][2], n4+arr[i][3], i+1)
        ans2.pop()

dfs(0,0, 0, 0, 0, 0, 0)

if not ans3:
    print(-1)
else:
    ans3.sort(key = lambda x : (x[0], x[1]))
    print(ans3[0][0])
    print(" ".join(map(str,ans3[0][1])))