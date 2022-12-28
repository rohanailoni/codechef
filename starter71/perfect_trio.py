# cook your dish here
test=int(input())



for _ in range(test):
    a,b,c=list(map(int,input().split(" ")))
    if a==b+c:
        print("yes")
    elif b==a+c:
        print("yes")
    elif c==a+b:
        print("yes")
    else:
        print("NO")
    
