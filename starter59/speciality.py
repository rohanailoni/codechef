test=int(input())

for _ in range(test):
    arr=list(map(int,input().split(" ")))
    max_a=-1;
    for i in arr:
        max_a=max(max_a,i)
    if(arr[0]==max_a):
        print("Setter")
    elif(arr[1]==max_a):
        print("Tester")
    elif(arr[2]==max_a):
        print("Editorialist")
