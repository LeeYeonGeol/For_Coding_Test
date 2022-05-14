def solution(m, musicinfos):
    answer = []

    db = {"C": "C", "C#": "Z", "D": "D", "D#": "X", "E": "E", "F": "F", "F#": "W", "G": "G", "G#": "V", "A": "A", "A#": "P", "B": "B", "E#": "R"}

    m_list = []
    strin = ""
    for char in m:
        if char.isalpha():
            if strin:
                m_list.append(db[strin])
            strin = ""
            strin += char
        else:
            strin += char
    if strin:
        m_list.append(db[strin])

    new_m = "".join(m_list)

    for info in musicinfos:
        start, end, song, code = info.split(",")

        a, b = start.split(":")
        start_time = 60*int(a)+int(b)
        a, b = end.split(":")
        end_time = 60*int(a)+int(b)
        time = end_time-start_time

        code_list = []
        strin = ""
        for char in code:
            if char.isalpha():
                if strin:
                    code_list.append(db[strin])
                strin = ""
                strin += char
            else:
                strin += char
        if strin:
            code_list.append(db[strin])

        len_code = len(code_list)

        code_list_2 = code_list*(time//len_code)+code_list[:time%len_code]

        real_code = "".join(code_list_2)


        if new_m in real_code:
            answer.append([time, start_time,song])


    if not answer:
        return "(None)"
    else:
        answer.sort(key=lambda x : (-x[0], x[1]))
        return answer[0][-1]