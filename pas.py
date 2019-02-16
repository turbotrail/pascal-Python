print("Enter the height of Pascal's traiangle in")
a=int(input())
b=(a*2)-1
c=(a-1)
cn=(a-1)
d=(b-1)
p=[p[:] for p in [[" "] * b] * a]
#print(p)
for i in range(a):
    t=c-i+2
    for j in range(b):
        if (i+j)==c or (i+j)==cn:
            p[i][j]=1
        if j<c+i and j>c-i and j==t:
            p[i][j]=p[i-1][j-1]+p[i-1][j+1]
            t=t+2               
    cn=cn+2
#print(p)
for l in p:
    for m in l:
        print(m,end = " ")
    print()
