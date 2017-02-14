# parsed input
t =(raw_input().split(' '))
N = int(t[0])
Q = int(t[1])

lastAns = 0
seqList = [[] for i in range(N)]

for i in range(Q):
    q, x, y = map(int, raw_input().strip().split(" "))
    seq = ((x ^ lastAns) % N)
    if (q == 1):
        seqList[seq].append(y)
    else: # q == 2
        lastAns = seqList[seq][y % len(seqList[seq])]
        print(lastAns)
        

#k = [[] for i in range(Q)] # i think this is error
#for i in range(Q):
#    k[i] = (raw_input().split(" "))
#    k[i] = map(int,k[i])
#
#for i in range(Q):
#    if (k[i][0]==1):
#        seq =((k[i][1]^lastAns)%N)
#        seqList[seq].append(k[i][2])
#    else:
#        seq =((k[i][1]^lastAns)%N)
#        lastAns= seqList[seq][k[i][2]]
#        print lastAns

