
a=int(input("enter 1st number :"))
b=int(input("enter 2nd number :"))
c=int(input("enter 3rd number :"))
#print(max(a,b,c))
#print(a if a>b and a>c else b if b>c and b>a else c)
max =a if a>b and a>c else b if b>c and b>a else c
print("max value :",max)
