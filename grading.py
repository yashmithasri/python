marks = float(input("please enter marks : "))
percentage = (marks/100)*100
if percentage>=90:
    print("grade A")
    print("your percentage is "+str(percentage))
elif percentage>=80 and marks <90 :
    print("grade b")
    print("your percentage is "+str(percentage))
elif percentage>=70 and marks<80:
    print("grade c")
    print("your percentage is "+str(percentage))
elif percentage>=60 and marks <70:
    print("grade d")
    print("your percentage is "+str(percentage))  
else:
    print("grade f")
    print("your percentage is "+str(percentage)) 
    print("u are failed") 
