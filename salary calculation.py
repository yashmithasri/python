salary= float(input("salary: "))
hra = int(input("hra :"))
da =int(input("da : "))
if salary ==10000:
    da = (80/100)*10000
    hra = (20/100)* da
    print("da is :"+str(da))
    print("hra is : "+str(hra))
elif salary ==20000:
    da = (90/100)*20000
    hra = (25/100)*da
    print("da is "+str(da))
    print("hra is "+str(hra))
else:
    da=(95/100)*salary
    hra = (30/100)*da
    print("da is "+str(da))
    print("hra is "+str(hra))
