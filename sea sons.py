month=input("Enter the month:")
date=int(input("Enter the date:"))
if month in ("januwary","febravary","march"):
    print("summer season")
elif month in ("april","may","june"):
    print("spring season")
elif month in ("july","august","september"):
    print("autumn season")
else:
    print("winter season")
if(month=="march")and(date>20):
    print("summer season")
elif(month=="june")and(date>21):
    print("spring season")
elif(month=="september")and(date>22):
    print("autumn season")
elif(month=="december")and(date>21):
    print("winter season")
