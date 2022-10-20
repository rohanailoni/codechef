test=int(input())


for _ in range(test):
    n=int(input())
    s=input()
    s=[i for i in s]
    if s[0]=='0':
        for i in range(2*n):
            if s[i]=="1":
                s[i]="0"
            else:
                s[i]="1"

    arr=[]
    cnt=0
    flag=0
    p=0
    for i in range(2*n):
        if s[i]=="0":
            arr.append(i)
        if s[i]!=s[2*n-i-1]:
            flag=1
            break
    if flag==1:
        print(1)
        print(2*n)
        continue
    else:
        if len(arr)==0:
            print("-1")
        else:
            cnt=2*n-1-arr[-1]
            for i in range(len(arr)-1,0,-1):
                if arr[i]-arr[i-1]-1!=cnt:
                    flag=1
                    print(2)
                    print(arr[i-1]+1," ",2*n-1-arr[i-1])
                    break
            if flag==0:
                print(2)
                print(arr[len(arr)-2]+2+" "+2*n-2*arr[len(arr)-2])


