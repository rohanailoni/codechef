# cook your dish here
test=int(input())



for _ in range(test):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    dic={}
    for i in arr:
        if i in dic:
            dic[i]+=1 
        else:
            dic[i]=1 
    got=False 
    for i in dic:
        if dic[i]%2!=0:
            got=True
            break

    if got==False:
        print("YES")
    else:
        print("NO")

