s = input()

ans = 0

st = []

for idx, i in enumerate(s):

    if st and i == ")" and st[-1][0] == "(":
        ns, nidx = st.pop()

        if nidx == idx - 1:
            ans += len(st)
        else:
            ans += 1
    else:
        st.append((i, idx))

print(ans)


