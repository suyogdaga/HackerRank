## finding the percentage : floating point and dictionary of lists 
student_marks = {}
n = int(raw_input())
for i in range(n):
    s = raw_input().split()
    name = s[0]
    marks = s[1:]
    student_marks[name]=map(float,marks)
query = raw_input()

if student_marks.has_key(query):
    k = student_marks[query]
    print "%.2f" % float(sum(k)/len(k))
