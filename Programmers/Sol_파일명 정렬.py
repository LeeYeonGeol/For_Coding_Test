def solution(files):
    answer = []
    sub_list = []
    for file in files:
        idx1, idx2 = -1, -1
        for idx, f in enumerate(file):
            if idx1 == -1:
                if f.isdigit():
                    idx1 = idx
            if idx1 != -1 and idx2 == -1:
                if not f.isdigit():
                    idx2 = idx
        if idx2 == -1:
            idx2 = len(file)

        sub_list.append([file[:idx1].lower(), int(file[idx1:idx2]), file[idx2:], file])

    sub_list.sort(key = lambda x : (x[0], x[1]))

    for sub in sub_list:
        answer.append(sub[-1])

    return answer