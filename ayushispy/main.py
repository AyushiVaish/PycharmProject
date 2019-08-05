from spy_details import spy_name,spy_age,spy_rating
spy_age=0
spy_rating=0.0
def spy_chat(spy_salutation,spy_name,spy_age,spy_rating):
    print "Here are your options " +spy_salutation +" " + spy_name
    show_menu="True"
    while show_menu:
        spy_choice=input("What do you want to choose: \n 1) Add a status \n 2)Add a friend \n 3) Send a secret message \n 4) Read a secret messages \n 5)Read all chats \n 6)Reas chats from selected SPY /n 0)Exit ")
        if spy_choice==1:
            print "Add a status"
        elif spy_choice==2:
            print "Add a friend"
        elif spy_choice==3:
            print "Send a secret message"
        elif spy_choice==4:
            print "Read a secret messages"
        elif spy_choice==5:
            print "Read all chats "
        elif spy_choice==6:
            print "Read chats from selected SPY"
        elif spy_choice==0:
            show_menu=="False"
        else:
            print "Invalid an option"
print "Hello"
spy_existing=raw_input("Are you a new user Y or N ?")
if spy_existing.upper()=="N":
    print "Welcome Back"
    spy_chat(spy_salutation,spy_name,spy_rating,spy_age)
elif spy_existing.upper()=="Y":
    spy_name = raw_input("Enter your name? ")
    if len(spy_name)>0:
        spy_salutation=raw_input("What Should we call you Mr. or Mrs. or Miss?")
        if spy_salutation=="Mr." or spy_salutation=="mr." or spy_salutation=="Miss" or spy_salutation=="miss" or spy_salutation=="Mrs." or spy_salutation=="mrs.":
            print "Welcome " + spy_salutation +" "+ spy_name + ".Please enter trhe following details."
            spy_age=input("What is your age ?")
            if  50>spy_age>15:
                print "You are an eligibile candidate."
                spy_rating=input("What is your rating ?")
                if spy_rating>=5:
                    print "Fabulous"
                elif 5<spy_rating<=4:
                    print "Excellent"
                elif 4<spy_rating<=3.5:
                    print "Very Good"
                elif 3.5<spy_rating<=2.5:
                    print "Need more to practice"
                else:
                    print "Bad Job"
                spy_online="True"
                print "Aunthenticaton completed.Welcome  " + spy_salutation +" "+ spy_name +" Your age is "+ str(spy_age)+ "and your rating is " + str(spy_rating)
                spy_chat(spy_salutation,spy_name,spy_age,spy_rating)
            else:
                print "You are not an eligible one."
        else :
             print "Please enter the valid detail"
    else :
        print "Please enter the valid name."
else:
    print "Ophs!!! Not permitted"