test=int(input())




for _ in range(test):
    a,b=list(map(int,input().split(" ")))
    ss=input()
    arr=[0 for i in range(a)]
    count=0
    for i in range(1,a):
        if(ss[i-1]!=ss[i]):
            count+=1
            arr[i]=count;
        else:
            arr[i]=count
    arr[0]=0
    ans=10000000000
    for i in range(a-1,-1,-1):
        if (i-(b-1))<0:
            break
        check =arr[i]-arr[i-(b-1)]
        if ss[i]=="0":
            check+=1
        ans=min(ans,check)
    print(ans)



