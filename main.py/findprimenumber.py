number=input("Enter your number to be checked as prime number")
print ("The number is " + str(number))
if (number <= 1):
    print ("The number " + str(number) + " is not a prime number")
elif(number==2):
    print ("The number " + str(number) + " is a prime number")
else :
    for i in range(2,number):
        if (number % i == 0):
            print ("The number " + str(number) + " is not a prime number")
        else :
            print ("The number " + str(number) + " is  a prime number")