n=int(input("Enter a number for series:"))
n1=0
n2=1
print("{}\n{}".format(n1,n2))
for i in range(2,n+1):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
