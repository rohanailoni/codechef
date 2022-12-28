# cook your dish here

test=int(input())


for _ in range(test):
    n=int(input())
    c1=list(map(int,input().split(" ")))
    c2=list(map(int,input().split(" ")))
    ans=0
    max1=0
    for i in range(n):
        if c1[i]!=0 and c2[i]!=0:
            ans+=1 
            
        else:
            
            ans=0
        max1=max(max1,ans)
    
    print(max1)
        
    

