# 2D array Hackerrank
a = []

# input list vectors as matrix
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    a.append(arr_temp)

values = []

# checck for the midddle element, and calculate accordingly
for i in range(1,5):
    for j in range(1,5):
        k = a[i][j]+a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1]
        values.append(k)
        
print max(values)
