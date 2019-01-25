num=int(input())
p=int(input())
l1=[]
for j in range(n):
    b=int(input())
    l1.append(b)
for k in range(q):
    d=0
    v=int(input())
    w=int(input())
    for i in range(u,v):
        d=d+int(l1[i])
    print(d)
