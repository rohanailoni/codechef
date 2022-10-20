test=int(input())


for _ in range(test):
    n=int(input())
    s=input()
    i=0;
    ans=0;
    while(i<n-1):
        if(s[i]==s[i+1]):
            ans+=1
        i+=1
    print(ans)
