import calendar
year=input("Enter the year to check whetherut is leap year or not")
print ("The year is " + str(year))
#result = calendar.isleap(year)
#print (result)
if(year % 4==0) :
    if(year % 100 ==0):
        if(year % 400 == 0):
            print ("{0} is a leap year ".format(year))
        else:
            print ("{0} is not a leap year ".format(year))
    else :
        print ("{0} is a leap year ".format(year))
else :
    print ("{0} is not a leap year ".format(year))