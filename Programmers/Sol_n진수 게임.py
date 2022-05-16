def solution(n, t, m, p):
    answer = ""

    def convert(n, k):
        T = "0123456789ABCDEF"
        q, r = divmod(n, k)
        if q == 0:
            return T[r]
        else:
            return convert(q, k) + T[r]

    cnt = 0
    length = m*t
    sub_answer = ""

    while 1:
        sub_answer += str(convert(cnt, n))
        cnt += 1
        if len(sub_answer) > length:
            break

    idx = p-1

    while 1:
        answer += sub_answer[idx]
        idx += m
        t -= 1

        if t == 0:
            break

    return answer