show_menu = True

menu = input("Choose your option to convert \n 1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius \n 3. Celsius to Kelvin \n 4. Kelvin to Celsius \n 5. Fahrenheit to Kelvin \n 6. Kelvin to Fahrenheit \n 0. Exit ")
while show_menu:
    if menu==1:
        celsius = input("Enter the temperature in celsius")
        result = celsius * 9/5 + 32
        print ("The temperature in Fahrenheit is " + str(result) )

    elif menu==2:
        fahrenheit =input ("Enter the temperature in Fahrenheut")
        celsius = 5/9 (fahrenheit-32)
        print ("The temperature in Celsius is " + str(celsius))

    elif menu == 3:
        celsius =  input("Enter the temperature in celsius")
        kelvin = celsius + 273
        print ("The temperature in Kelvin is " + str(kelvin))

    elif menu == 4:
        kelvin = input("Enter the temperature in Kelvin")
        celsius = kelvin - 273
        print ("The temperature in Celsius is " + str(celsius))

    elif menu == 5:
        fahrenheit = input ("Enter the temperature in Fahrenheut")
        kelvin = 5/9 (fahrenheit -32) + 273
        print ("The temperature in Kelvin is " + str(kelvin))

    elif menu == 6 :
        kelvin = input("Enter the temperature in Kelvin")
        fahrenheit = 9/5 (kelvin -273) + 32
        print ("The temperature in Fahrenheit is " + str(fahrenheit))

    else :
        show_menu == False