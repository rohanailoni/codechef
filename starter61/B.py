test=int(input())

for _ in range(test):
    a,b,c=list(map(int,input().split(" ")))
    if (a+b)%2!=0:
        print("YES")
        continue
    if (b+c)%2!=0:
        print("YES")
        continue
    if (c+a)%2!=0:
        print("YES")
        continue
    print("NO")

