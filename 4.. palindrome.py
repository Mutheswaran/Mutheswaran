def palindrome(a):
    return a==a[::-1]
a=(input("enter the number:"))
s=palindrome(a)
e=a[::-1]
if s:
    print("true")
    print("Explanation:from left to right ,it reads ",a,"from right to left it becomes",e,"there fore it is  palindromic")
else:
    print("false")
    print("Explanation:from left to right ,it reads ",a,"from right to left it becomes",e,"there fore it is not palindromic")


