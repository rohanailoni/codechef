test=int(input())

class Pair:
    def __init__(self,a,b):
        self.a=a;
        self.b=b;
for _ in range(test):
    n=int(input())
    a=[0]
    a=a+list(map(int,input().split(" ")))
    b=[0 for i in range(200001)]

    if n==1:
        print(1)
        continue
    else:
        k=[]
        for i in range(2,n+1):
            b[i]=a[i]<a[i-1]
        k.append(Pair(b[2],1))
        for i in range(3,n+1):
            if b[i]==k[len(k)-1].a:
                k[len(k)-1].b+=1
            else:
                k.append(Pair(b[i],1))
        k.append(Pair(0,0))
        ans=0
        for i in range(len(k)-1):
            ans+=k[i].b*((k[i].b+1)//2)
        for i in range(len(k)-1):
            if k[i].a==1:
                ans+=k[i].b*k[i+1].b
        print(ans+n)

        



