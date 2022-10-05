# cook your dish here
test=int(input())

for _ in range(test):
    n=int(input())
    s=input()
    i=0
    j=n-1
    ans=""
    while(j>i):
        #print(i,j)
       
        if(s[i]=="1"):
            ans=ans+s[i]
        if(s[i]=="0"):
            ans=s[i]+ans
            
        if(s[j]=="1"):
            ans=s[j]+ans
            
        
            
        if(s[j]=="0"):
            ans=ans+s[j]
        i+=1
        j-=1
    if(i==j):
        if(s[i]=="1"):
            ans+=s[i]
        else:
            
            ans=s[i]+ans
    print(ans)
