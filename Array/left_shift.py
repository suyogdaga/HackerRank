# fast solution
from collections import deque

k,w = map(int,raw_input().strip().split(" "))
a = map(int,raw_input().strip().split(" "))
t = deque(a)

for i in range(w):
    t.rotate(-1)
t = list(t)

for i in t:
    print i,


##below solution is corrrect but takes more time
#
#k,w = map(int,raw_input().strip().split(" "))
#a = map(int,raw_input().strip().split(" "))
#b = [0]*len(a)
#
#for i in range(w):
#    for j in range(len(a)):
#        t = (j-1)%len(a)
#        b[t]= a[j]
#    a= b[:] 
