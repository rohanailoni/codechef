test=int(input())


for _ in range(test):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    stack=[]
    ans=0
    for i in range(n):
        if len(stack)==0:
            stack.append(arr[i])
        else:
            if arr[i]!=stack[-1]:
                ans+=1
                stack.pop()
            else:
                stack.append(arr[i])
    while len(stack)>=2:
        temp=stack[-1]
        stack.pop()
        if temp==stack[-1]:
            stack.pop()
            stack.append(0)
        else:
            ans+=1
            stack.pop()
    print("ans",ans)
