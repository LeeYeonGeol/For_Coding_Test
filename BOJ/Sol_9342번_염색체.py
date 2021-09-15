import re
t = int(input())

p = re.compile('[A-F]?[A]+[F]+[C]+[A-F]?')
for _ in range(t):

    s = input()

    m = re.match(p, s)

    if m != None:
        if m.group() == s:
            print("Infected!")
        else:
            print("Good")
    else:
        print("Good")
