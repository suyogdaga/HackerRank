m = [0]
s = []
for i in xrange(int(raw_input())):
    q = map(int, raw_input().split())
    if q[0] == 1:
        if q[1] >= m[-1]: m.append(q[1])
        s.append(q[1])
    elif q[0] == 2:
        if m[-1] == s.pop(): m.pop()
    elif q[0] == 3:
        print m[-1]
