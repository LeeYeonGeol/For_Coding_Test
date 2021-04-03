a, b = map(int, input().split())

st = []
s = str(a)

for i in s:
    while st and st[-1] < i and b > 0:
        st.pop()
        b -= 1
    st.append(i)

if b != 0:
    st = st[:-b]

print("".join(st))