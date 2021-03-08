def solution(dartResult):
    score = 0
    answer = []
    sub = ""
    case = True
    for x in dartResult:
        print(sub)
        if case == False and x.isdigit() == True:
            answer.append(sub)
            sub = ""

        if ord(x) in [35,42,68,83,84]:
            if ord(x) == 83:
                pass
            elif ord(x) == 68:
                sub = str(int(sub)**2)
            elif ord(x) == 84:
                sub = str(int(sub)**3)
            elif ord(x) == 42:
                if not answer:
                    sub = str(int(sub)*2)
                else:
                    sub = str(int(sub)*2)
                    answer[-1] = str(int(answer[-1])*2)
            else:
                sub = str(-int(sub))
        else:
            sub += str(x)

        case = x.isdigit()
    result = 0
    for i in answer:
        result += int(i)
    result += int(sub)
    return result