s, n = map(int, input().split())

n = str(n)
m = 2*s+3

ans = [[" "]*((s+2)*(len(n))+(len(n)-1)) for _ in range(m)]

st = 0
for i in n:
    if i == '1':
        st += s+1
        for j in range(1, 1+s):
            ans[j][st] = "|"
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 2
    elif i == '2':
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 1
        for _ in range(s):
            ans[0][st], ans[(m-1)//2][st], ans[m-1][st] = "-", "-", "-"
            st += 1

        for j in range(1, 1+s):
            ans[j][st] = "|"
        st += 2
    elif i == '3':
        st += 1
        for _ in range(s):
            ans[0][st], ans[(m-1)//2][st], ans[m-1][st] = "-", "-", "-"
            st += 1

        for j in range(1, 1+s):
            ans[j][st] = "|"
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 2
    elif i == '4':
        for j in range(1, 1+s):
            ans[j][st] = "|"
        st += 1
        for _ in range(s):
            ans[(m-1)//2][st]= "-"
            st += 1
        for j in range(1, 1+s):
            ans[j][st] = "|"
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 2
    elif i == '5':
        for j in range(1, 1+s):
            ans[j][st] = "|"
        st += 1
        for _ in range(s):
            ans[0][st], ans[(m-1)//2][st], ans[m-1][st] = "-", "-", "-"
            st += 1
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 2
    elif i == '6':
        for j in range(1, 1+s):
            ans[j][st] = "|"
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 1
        for _ in range(s):
            ans[0][st], ans[(m-1)//2][st], ans[m-1][st] = "-", "-", "-"
            st += 1
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 2
    elif i == '7':
        st += 1
        for _ in range(s):
            ans[0][st] = "-"
            st += 1
        for j in range(1, 1+s):
            ans[j][st] = "|"
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 2
    elif i == '8':
        for j in range(1, 1+s):
            ans[j][st] = "|"
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 1
        for _ in range(s):
            ans[0][st], ans[(m-1)//2][st], ans[m-1][st] = "-", "-", "-"
            st += 1
        for j in range(1, 1+s):
            ans[j][st] = "|"
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 2
    elif i == '9':
        for j in range(1, 1+s):
            ans[j][st] = "|"
        st += 1
        for _ in range(s):
            ans[0][st], ans[(m-1)//2][st], ans[m-1][st] = "-", "-", "-"
            st += 1
        for j in range(1, 1+s):
            ans[j][st] = "|"
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 2
    else:
        for j in range(1, 1+s):
            ans[j][st] = "|"
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 1
        for _ in range(s):
            ans[0][st], ans[m-1][st] = "-", "-"
            st += 1
        for j in range(1, 1+s):
            ans[j][st] = "|"
        for j in range(2+s, m-1):
            ans[j][st] = "|"
        st += 2
for a in ans:
    print("".join(a))