n=4

for i in range(2*n-1):
    for j in range(2*n-1):
        top=i
        left=j
        bottom=(2*n-1-1)-i
        right=(2*n-1-1)-j

        min_dist=min(top,left,right,bottom)
        print(n-min_dist,end="")
    print()