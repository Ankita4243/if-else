year=int(input("enter the year:"))
if(year%4==0):
    print("this is leap year")
elif(year%100==0):
    print("this year is leap year")
elif(year%400==0):
    print("this year is leap year")
else:
    print("this year is not leap year")