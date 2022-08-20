n=int(input())
for _ in range(n):
    a=int(input())
    arr=list(map(str,input().rstrip().split()))
    f=1
    
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            f+=1
            
    
    print(f)
