rows=4

for i in range(1,rows+1):
    if i==1 or i ==4:
        print("*"*rows)
    else:
        print("*"," "*(rows-4),"*")