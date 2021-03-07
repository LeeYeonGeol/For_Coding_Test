def solution(d, budget):
    d.sort()
    answer = 0
    index = 0
    while(1):
        budget -= d[index]
        if budget < 0:
            break
        answer += 1
        index += 1

        if index == len(d):
            break

    return answer