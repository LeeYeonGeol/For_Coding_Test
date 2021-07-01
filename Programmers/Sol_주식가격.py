def solution(prices):
    answer = [0]*len(prices)
    st = []
    for idx, p in enumerate(prices):
        if not st:
            st.append((idx, p))
        else:
            while st:
                if st[-1][1] > p:
                    pidx, pp = st.pop()
                    answer[pidx] = idx-pidx
                else:
                    break
            st.append((idx, p))

    n = len(prices)-1
    while st:
        idx, p = st.pop()
        answer[idx] = n-idx

    return answer