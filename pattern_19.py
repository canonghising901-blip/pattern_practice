rows=10
n=rows//2
gap=2
for i in range(1,n+1):
    if i==1 or i==rows:
        print("*"*rows)
    else:
        print("*"*(n-i+1),end="")
        print(" "*(gap),end="")
        print("*"*(n-i+1))
        gap=gap+2
gap1=gap-2
for i in range(n,0,-1):
    if i==1 or i==rows:
        print("*"*rows)
    else:
        print("*"*(n-i+1),end="")
        print(" "*(gap1),end="")
        print("*"*(n-i+1))
        gap1=gap1-2
