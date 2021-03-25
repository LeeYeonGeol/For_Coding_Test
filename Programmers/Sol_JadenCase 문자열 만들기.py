def solution(s):
    answer = []
    for i in s:
        if not answer:
            answer.append(i.upper())
        else:
            if answer[-1] == ' ':
                answer.append(i.upper())
            else:
                answer.append(i.lower())
    return "".join(answer)