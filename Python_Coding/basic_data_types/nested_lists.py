l =[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    l.append([name,score])


k = set(l[x][1] for x in range(len(l)))
k = list(k)
k.sort()

students = [x[0] for x in l  if x[1] == k[1]]
students.sort()

for s in students:
    print s


