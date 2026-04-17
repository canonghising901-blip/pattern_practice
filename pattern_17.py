alphabets={
    1:'A',
    2:'B',
    3:'C',
    4:'D',
    5:'E',
    6:'F',7:'G',8:'H',9:'I',10:'J'
}
rows=4

for i in range(1,rows+1):
    
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(alphabets.get(j,None),end="")
    for j in range(i-1,0,-1):
        print(alphabets.get(j,None),end="")
    print()