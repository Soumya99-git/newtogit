t = int(input())
d=[]
while(t!=0):
    
    n = int(input())
    a = []
    while(n!=0):
        b = []
        for i in input().split():
            b.append(int(i))
        n=n-1
        a.append(b)
    d.append(a)
    t = t-1

#calculation of sum

for j in d:
    
    c = 0
    m = 0
    
    for i in j:

        s1 = 0
        s2 = 0
        while(i[0]!=0):
            s1=s1+int(i[0]%10)
            i[0] = int(i[0]/10)

        while(i[1]!=0):
            s2=s2+int(i[1]%10)
            i[1] = int(i[1]/10)
       
        if s1>s2:
            c=c+1
        elif s2>s1:
            m=m+1
        else:
            c=c+1
            m=m+1
        
    if c>m:
        print("0"+" "+str(c))
    elif m>c:
        print("1"+" "+str(m))
    else:
        print("2"+" "+str(m))
        