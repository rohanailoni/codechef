test=int(input())




for _ in range(test):
    n=int(input())
    org=input()
    rev=org[::-1]
    dp=[[0 for i in range(n+1)] for j in range(n+1)]
    max1=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if org[i-1]==rev[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
            
    for i in range(1,n):
        o=i 
        r=n-i
        max1=max(max1,dp[o][r])
    print(max1)
        
    


