# cook your dish here
test=int(input())

for _ in range(test):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    max=-10**5;
    index=-1;
    for i in range(n):
        if(arr[i]>max):
            index=i
            max=arr[i]
    if(index==0):
        print(-1)
        continue
    
    arr1=arr[:index]
    arr2=arr[index:]
    print(len(arr1))
    print(" ".join(map(str,arr1)))
    print(len(arr2))
    print(" ".join(map(str,arr2)))

    
            
    
        
