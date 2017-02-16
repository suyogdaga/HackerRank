# largest rectangle or max rectangle from histogram
max_area = 0
k = int(raw_input())
h = map(int,raw_input().strip().split(" "))

for i in xrange(k):
    cnt = 0
    for j in xrange(i,-1,-1): # left side
        if h[j]>=h[i]:
            cnt +=1
        else:
            break
    for k in xrange(i+1,len(h)): # right side with respect to element
        if h[k]>=h[i]:
            cnt +=1
        else:
            break
    area = h[i]*cnt
    if (area>max_area):
        max_area = area
print max_area
            