a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
max_val=a if(a>b and a>c) else b if (b>c) else c
print(max_val)
