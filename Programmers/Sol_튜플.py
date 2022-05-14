def solution(s):
    answer = []
    visited = [False]*100001

    new_list = []
    sub_list = []
    strin = ""

    for ch in s[1:-1]:
        if ch == "{":
            sub_list = []
        elif ch == "}":
            if strin:
                sub_list.append(int(strin))
                strin = ""
            new_list.append(sub_list)
            sub_list = []
        else:
            if ch == ",":
                if strin:
                    sub_list.append(int(strin))
                    strin = ""
            else:
                strin += ch

    new_list.sort(key = lambda x : len(x))

    for li in new_list:
        for element in li:
            if visited[element] == False:
                answer.append(element)
                visited[element] = True

    return answer