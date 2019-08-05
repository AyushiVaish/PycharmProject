def multiplication(number):
    for i in range(range1,range2):
        multiplication = number * i
        print ( "The multiplication of " + str(number) + " is " + str(number) + " * " + str(i) + " = " + str(multiplication))



number = input("Enter your number")
print ("The number is " + str(number))
range1 = input("Enter the starting range")
range2 = input("Enter the ending range")
multiplication(number)