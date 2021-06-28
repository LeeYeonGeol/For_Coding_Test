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


###########################################################################
n = int(input())

a = [[False]*n for _ in range(n)]

check_col = [False] * n
check_dig = [False] * (2*n-1)
check_dig2 = [False] * (2*n-1)

def check(row, col):
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[row-col+n-1]:
        return False
    return True

ans = 0
def calc(row):
    global ans
    if row == n:
        ans += 1
        return

    for col in range(n):
        if check(row, col):
            check_dig[row+col] = True
            check_dig2[row-col+n-1] = True
            check_col[col] = True
            a[row][col] = True
            calc(row+1)
            check_dig[row+col] = False
            check_dig2[row-col+n-1] = False
            check_col[col] = False
            a[row][col] = False

calc(0)
print(ans)