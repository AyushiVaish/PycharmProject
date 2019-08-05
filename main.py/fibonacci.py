def fibonacci(number):
    a=0
    b=1
    i=0
    if(number == 1):
        print(a)
    elif(number==2):
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        while i<number-2:
            c=a+b
            print(c)
            a=b
            b=c
            i=i+1
#print ("Fibonacci series of " + str(number) + "is" + str(fibonacci(number)))
number = input("Enter the required fibonacci series")
fibonacci(number)