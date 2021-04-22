n = int(input())

arr = list(map(int, input().split()))

ans = -1
res = []

for i in range(n-2,-1,-1):
    if arr[i] > arr[i+1]:
        ans = i
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                sub = j
        arr[i], arr[sub] = arr[sub], arr[i]
        res += arr[:i+1]
        res += arr[i+1:][::-1]


        print(" ".join(map(str, res)))
        break
else:
    print(-1)
