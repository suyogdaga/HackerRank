#length,case = map(int,raw_input().strip().split(" "))
#
#a = [0]*length
#
#for i in range(case):
#    start, end,value =map(int,raw_input().split(" "))
#    for i in range(start-1,end,1):
#        a[i]+=value
#
#print max(a)

n, m = [int(x) for x in input().split(' ')]
arr = [0]*n
for i in range(m):
    a, b, k = [int(x) for x in input().split(' ')]
    arr[a-1] += k
    if b < n:
        arr[b] -= k

x = 0
biggest = 0
for i in range(n):
    x = x + arr[i]
    if x > biggest:
        biggest = x

print(biggest)