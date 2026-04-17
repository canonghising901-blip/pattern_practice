rows=10
n=rows//2+1
gap=rows

for i in range(1,n+1):
    print("*"*i,end="")
    print(" "*gap,end="")
    print("*"*i)
    gap=gap-2
gap1=gap+4
for i in range(n-1,0,-1):
    print("*"*i,end="")
    print(" "*gap1,end="")
    print("*"*i)
    gap1=gap1+2