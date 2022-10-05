 
 
def maxSubArraySum(a, size):
 
    max_so_far = -99999999999 - 1
    max_ending_here = 0
 
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
test=int(input())


for _ in range(test):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    m=int(input())
    B=list(map(int,input().split(" ")))

    # top to end
    max_top=-99999999999-1
    pre=arr[0]
    for i in range(1,n):
        max_top=max(max_top,pre+arr[i])
        pre=pre+arr[i]
    #end to top
    max_end=-99999999999-1
    pre=arr[n-1]
    for i in range(n-2,0,-1):
        max_end=max(max_end,pre+arr[i])
        pre=pre+arr[i]
    a=max(max_top,max_end)
    for i in B:
        if(i>0):
            a+=i
    print("ans",max(maxSubArraySum(arr,n),a))
    # print(max_top,max_end,maxSubArraySum(arr,n))

    

