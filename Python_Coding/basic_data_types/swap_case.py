##Swap case
s = " HELLLO WorLD "
k = s.lower()
t = s.upper()
w = []
for i in range(len(s)):
    if s[i]==k[i] and s[i] == t[i]:
        w.append(k[i])
    elif s[i]== k[i]:
        w.append(t[i])
    else:
        w.append(k[i])

print "".join(w)