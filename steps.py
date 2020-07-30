t=int(input())
while(t!=0):
    x,y = input().split(" ")
    n = int(x)
    k = int(y)
    a=[]
   
    for i in input().split(" "):
        a.append(int(i))
    s=""
    for i in a:
        if(i%k==0):
            s=s+str(1)
        else:
            s=s+str(0)
    print(s)
    t-=1