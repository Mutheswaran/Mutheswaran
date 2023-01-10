a=int(input("Enter the number of new loaves"))
x=a*185
b=int(input("enter the number of old loaves"))
y=(b*(185-(185*60/100)))
print("Regular Price=185.00")
print("cost of new loaves",x)
print("cost of old loaves",y)
print("total amount:",x+y)
