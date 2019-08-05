import math;
menu = True;
while menu:
    show_menu = input("What do you want to do \n 1.Addition \n 2.Subtraction  \n 3.Multiplication \n 4.Division \n 5.Remainder \n 6.Quotient \n 7.Exponent \n 8.SquareRoot \n 9.Ceil \n 10.Floor \n 11.Radians to degrees \n 12.Factorial of a number \n 13.Log of number with no specified base \n 14.log with base 10 \n 15.Degree to Radians \n 16.Sine in Radians \n 17.Sine Hyperbolic \n 18.Cosine in Radians \n 19.Cosine Hyperbolic \n 20.Tangent in Radians \n 21.Tangent Hyperbolic \n 0.Exit")

    if show_menu ==1:
        a = input("Enter your first number");
        b = input("Enter your second number");
        sum = a + b;
        print ("Sum of two numbers is " + str(sum));


    elif show_menu==2:
             a = input("Enter your first number");
             b = input("Enter your second number");
             sub = a - b;
             print ("Difference of two numbers is " + str(sub));


    elif show_menu==3:
        a = input("Enter your first number");
        b = input("Enter your second number");

        mul = a * b;
        print ("Multiplication of two numbers is " + str(mul));


    elif show_menu ==4 :
        a = input("Enter your first number");
        b = input("Enter your second number");

        div = a / b;
        print ("Division of two number is " + str(div));

    elif show_menu==5:
        a = input("Enter your first number");
        b = input("Enter your second number");

        remainder = a % b;
        print ("Remainder of two number is " + str(remainder));

    elif show_menu==6:
        a = input("Enter your first number");
        b = input("Enter your second number");

        quotient = a // b;
        print ("Quotient of two number is " + str(quotient));

    elif show_menu==7:
        a = input("Enter your  number");
        power = input("Enter your power");
        exponent = a ** power;
        print ("Exponential of a number is " + str(exponent));

    elif show_menu==8:
        a = input("Enter your  number");
        print(math.sqrt(a));

    elif show_menu==9:
        a = input("Enter your  number");
        print(math.ceil(a));

    elif show_menu==10:
        a = input("Enter your  number");
        print(math.floor(a));

    elif show_menu==11:
            Radians=input("Enter your radians to be converted to degerees")
            print (math.degrees(Radians))

    elif show_menu==12:
        a = input("Enter your  number");
        print(math.factorial(a))

    elif show_menu==13:
        a = input("Enter your  number");
        print(math.log(a, base=None))

    elif show_menu==14:
        a = input("Enter your  number");
        print(math.log10(a))

    elif show_menu == 15:
            Degrees = input("Enter your degree to be converted to radians")
            print (math.radians(Degrees))

    elif show_menu==16:
            Choose = input("Select your degree")
            sin=math.sin(math.radians(Choose))
            print(sin)

    elif show_menu == 17:
            Choose = input("Select your degree")
            sinh = math.sinh(math.radians(Choose))
            print(sinh)

    elif show_menu == 18:
            Choose = input("Select your degree")
            cos = math.cos(math.radians(Choose))
            print(cos)

    elif show_menu == 19:
            Choose = input("Select your degree")
            cosh = math.cosh(math.radians(Choose))
            print(cosh)

    elif show_menu == 20:
            Choose = input("Select your degree")
            tan = math.tan(math.radians(Choose))
            print(tan)

    elif show_menu == 21:
            Choose = input("Select your degree")
            tanh = math.tanh(math.radians(Choose))
            print(tanh)

    else :
            menu =False







