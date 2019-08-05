#def armstrong(number):


number = input("Enter your number")
print ("The number is " + str(number))
temp = number

b = 0
while temp > 0:
    a = temp % 10
    b = b + a ** 3
    temp = temp / 10
if (number == b):
    print ("The number " + str(number) + " is an Armstrong Number")
else:
    print ("The number " + str(number) + " is not an Armstrong Number")

#armstrong(number)