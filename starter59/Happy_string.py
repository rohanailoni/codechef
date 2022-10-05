# cook your dish here
test=int(input())
def check(s):
    arr=['a','e','i','o','u']
    for i in s:
        if i not in arr:
            return False
    return True
            
for _ in range(test):
    s=input()
    i=0;
    j=1;
    n=len(s)
    yay=False
    while(i<n and j<n+1):
        #print(s[i:j],i,j)
        if(check(s[i:j])):
            if(j-i>2):
                print("Happy")
                yay=True
                break
            else:
                j+=1
        else:
            i=j
            j+=1
    if(yay==False):
        print("Sad")
        
    
    
                
            
            
    
    
