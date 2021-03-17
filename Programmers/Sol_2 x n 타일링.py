def solution(n):
    ans = 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 2
        c = 0
        for i in range(3, n+1):
            c = a + b
            a, b = b, c

    return c % 1000000007