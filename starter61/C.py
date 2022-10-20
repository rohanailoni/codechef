from collections import OrderedDict
test=int(input())

def lcs(a,b,m,n):
    dp=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

for _ in range(test):
    n=int(input())
    A=input()
    B=input()
    # print(lcs(A,B[::-1],n,n))
    dic={}
    for i in range(n):
        if A[i] not in dic:
            dic[A[i]]=1
        else:
            dic[A[i]]+=1
    # dic=OrderedDict(sorted(dic.items()))
    mp={}
    for i in range(n):
        if B[i] not in mp:
            mp[B[i]]=1
        else:
            mp[B[i]]+=1
    # mp=OrderedDict(sorted(mp.items()))
    # ans=0
    # x=0
    # y=0
    # for i in range(n):
    #     if dic[A[i]]!=dic[list(dic.keys())[-1]]:
    #         x=dic[A[i]]
    #     if mp[B[i]]!=mp[list(mp.keys())[-1]]:
    #         y=mp[B[i]]
    #     ans=max(ans,min(x,y))
    # print(ans)
    res=[0]
    for key in dic.keys():
        if key in mp.keys():
            res.append(min(dic[key],mp[key]))
    print(max(res))



