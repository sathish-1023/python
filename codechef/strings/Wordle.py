t=int(input())
for  _  in range(t):
    a=input()
    b=input()
    r=''
    for i in range(len(a)):
        if a[i]==b[i]:
            r+='G'
        else:
            r+='B'
    r=''.join(r)
    print(r)
