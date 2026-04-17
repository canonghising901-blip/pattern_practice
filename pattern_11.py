rows=5

for i in range(1,rows+1):
    print("")
    if i%2!=0:
        start=1
    else:
        start=0
    for j in range(1,i+1):
        print(start,end="")
        start=1-start
