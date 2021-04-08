n = int(input())

ans = ""

def recursive(x):
    global ans

    if x == 0:
        return
    else:
        recursive(x//2)
        ans += str(x%2)

recursive(n)
print(ans)


