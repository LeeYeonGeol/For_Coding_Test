def solution(s):

    st = []
    for i in s:
        if not st:
            st.append(i)
        else:
            if st[-1] == i:
                st.pop()
            else:
                st.append(i)
    if st:
        return 0
    else:
        return 1