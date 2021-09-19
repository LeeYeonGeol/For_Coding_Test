import copy

t = int(input())

for _ in range(t):
    ans = 0
    tmp = list(map(int, input().split()))
    case = tmp[0]
    student = tmp[1:]
    nstudent = []
    for idx, s in enumerate(student):
        if not nstudent:
            nstudent.append(s)
        else:
            for idx2, tall in enumerate(nstudent):
                if tall > s:
                    ans += idx-idx2
                    nstudent.insert(idx2,s)
                    break
            else:
                nstudent.append(s)

    print(case, ans)


