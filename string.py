x=int(input())
b=[]
while(x!=0):
    n = int(input())
    a=[]
    for i in input().split(" "):
        a.append(int(i))
    b.append(a)
    x = x-1

for i in b:
    sum = 0
    for j in range(len(i)-1):
        if(i[j]>i[j+1]):
            sum = sum+(i[j]-i[j+1]-1) 
        else:
            sum = sum+(i[j+1]-i[j]-1)
    print(sum)

print("New Git")