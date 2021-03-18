def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)
    s = 0
    e = n-1
    while(s <= e):
        if people[s]+people[e] > limit:
            e -= 1
        else:
            s += 1
            e -= 1
        answer += 1

    return answer