n=int(raw_input())
InputStrList=[]
for i in range(n):
    InputStrList.append(raw_input())
    
q=int(raw_input())
for i in range(q):
    InputStr=raw_input()
    Count=0
    for j in range(len(InputStrList)):
        if InputStr == InputStrList[j]:
            Count+=1
    print(Count)