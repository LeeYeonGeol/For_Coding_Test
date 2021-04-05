n = int(input())

result = 0

arr = [0]*n

def recursive(x):
    global result

    for j in range(x-1):
        if arr[j] == arr[x-1]  or abs(arr[j]-arr[x-1]) == abs(x-1-j):
            return

    if x >= n:
        result += 1
        return
    else:
        for i in range(n):
            arr[x] = i
            recursive(x+1)

recursive(0)

print(result)