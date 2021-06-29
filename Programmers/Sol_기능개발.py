def solution(progresses, speeds):
    n = len(speeds)
    answer = []
    start = 0

    while 1:
        # 작업
        for i in range(n):
            progresses[i] += speeds[i]

        st = []
        while 1:
            if progresses[start] < 100:
                break
            else:
                st.append(start)
                start += 1
            if start == n:
                break
        if st:
            answer.append(len(st))
        if start == n:
            break


    return answer