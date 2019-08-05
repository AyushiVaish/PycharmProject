number = input("Enter your number")
print ("The number is " + str(number))
fact = 1
i=number
if( number == 1):
    print ("The factorial of " + str(number) + " is " + str(number))
else:
    while i>0:

            fact = i * fact
            i=i-1

    print ("The factorial of " + str(number) + " is " + str(fact))

