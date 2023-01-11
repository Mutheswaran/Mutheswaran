a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
print("Which method did you want:")
print("1-addition")
print("2-subtraction")
print("3-multiplication")
print("4-division")
method=int(input("Enter the method number:"))
if(method==1):
    add=a+b
    print("addition:",add)
elif(method==2):
    sub=a-b
    print("subtraction:",sub)
elif(method==3):
    mul=a*b
    print("multiplication:",mul)
elif(method==4):
    div=a//b
    print("division:",div)
else:
    print("the deafault method")
